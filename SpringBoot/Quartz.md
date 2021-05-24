\> 本文由 \[简悦 SimpRead\](http://ksria.com/simpread/) 转码， 原文地址 \[www.jianshu.com\](https://www.jianshu.com/p/a99b80021be6)

## 简介

**Quartz 是一个很牛的任务调度框架，通过它我们可以实现诸如: 定时活动、延时活动、订单状态延时检测、服务器状态定时检测等，时间调度任务功能。**

下面我们介绍一下它在 SpringBoot 中的使用：

* [简介](#简介)
* [快速集成](#快速集成)
  + [1. 首先引入 maven 依赖](#1-首先引入-maven-依赖)
  + [2. 配置 Quartz](#2-配置-quartz)

## 1、快速集成

快速集成体验一下 Quartz 的功能吧。

### 1. 首先引入 maven 依赖

``` xml
<!--Quartz-->
        <dependency>
            <groupId>org.quartz-scheduler</groupId>
            <artifactId>quartz</artifactId>
            <version>2.2.1</version>
            <exclusions>
                <exclusion>
                    <artifactId>slf4j-api</artifactId>
                    <groupId>org.slf4j</groupId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context-support</artifactId>
        </dependency>
```

### 2. 配置 Quartz

#### 1、Quartz 的 config 配置类：SchedulerConfig

SchedulerConfig 类通过 **@Configuration** 自动装载配置。这里它配置了两种 Bean 工厂，一个是 **JobFactory** ，另一个是 **SchedulerFactoryBean**。


##### 1、JobFactory

我们使用@Autowired自动注入对象时实际上调用的是AdaptableJobFactory 下的这个方法，通过反射创建的

![20191015214057660](https://cdn.jsdelivr.net/gh/Eakamm/ImageBed/JavaLearn/20191015214057660.png)

job对象在spring容器加载时候，能够注入bean，但是调度时，job对象会重新创建，那么我们这个对象的实例化就没有经过Spring的处理，也就不再IOC容器当中，因为Spring要求注入的对象和被注入的对象必须都要在IOC容器中，此时就是导致已经注入的对象丢失，因此报空指针异常。

这时候我们可以创建一个AutowiringSpringBeanJobFactory类继承SpringBeanJobFactory（实现了JobFactory接口），重写createJobInstance方法，手动的将创建的对象添加到IOC容器当中

``` java
/**
 * 自动注入的jobBean工厂
 */
public class AutowiringSpringBeanJobFactory extends SpringBeanJobFactory
        implements ApplicationContextAware {

    private transient AutowireCapableBeanFactory beanFactory;

    @Override
    public void setApplicationContext(final ApplicationContext context) {

        beanFactory = context.getAutowireCapableBeanFactory();
    }

    @Override
    protected Object createJobInstance(final TriggerFiredBundle bundle) throws Exception {
        final Object job = super.createJobInstance(bundle);
        beanFactory.autowireBean(job);
        return job;
    }
}
```

**AutowiringSpringBeanJobFactory 工厂类**将负责生成实现了 Job 接口的类的实例对象

##### 2、SchedulerFactoryBean

**jobFactory(ApplicationContext applicationContext)** 是将AutowiringSpringBeanJobFactory对象放入IOC容器中。

* quartzProperties 配置参数可以自由配置 Quartz 的一些基本参数属性，比如配置调度线程数，调度线程池类型等，这里只配置了一个基本使用参数，如果需要更多请查阅官网。

``` java
/**
 * 定时配置（可以配置静态定时任务）
 */
@Configuration
public class SchedulerConfig {

    @Bean
    public JobFactory jobFactory(ApplicationContext applicationContext) {
        AutowiringSpringBeanJobFactory jobFactory = new AutowiringSpringBeanJobFactory();

        jobFactory.setApplicationContext(applicationContext);

        return jobFactory;
    }

    //SchedulerFactoryBean
    @Bean
    public SchedulerFactoryBean schedulerFactoryBean(JobFactory jobFactory, Trigger simpleJobTrigger)
            throws IOException{
        SchedulerFactoryBean factory = new SchedulerFactoryBean();
        Properties properties = new Properties();
        // quartz参数
        Properties prop = new Properties();
        // 线程池配置
        prop.put("org.quartz.threadPool.class", "org.quartz.simpl.SimpleThreadPool");
        prop.put("org.quartz.threadPool.threadCount", "20");
        prop.put("org.quartz.threadPool.threadPriority", "5");
        // JobStore配置
        prop.put("org.quartz.jobStore.class", "org.quartz.impl.jdbcjobstore.JobStoreTX");

        factory.setJobFactory(jobFactory);
        factory.setQuartzProperties(properties);
        //factory.setTriggers(simpleJobTrigger);

        return factory;
    }
}
```

### 2、quartz.properties

``` java
#------配置调度器的线程池
#线程池类
org.quartz.threadPool.class = org.quartz.simpl.SimpleThreadPool
#线程个数
org.quartz.threadPool.threadCount = 3

#------配置任务调度现场数据保存机制，默认保存在内存
org.quartz.jobStore.class = org.quartz.simpl.RAMJobStore
```

## 2、自定义定时任务

### 1、创建一个自定义的任务

创建 ScheduledJob.java 并实现 Job 接口，它是我们之后任务被调度后执行业务逻辑的主要类，通过 execute() 方法执行：

``` java
import org.jboss.logging.Logger;
import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

/**
 * 自定义定时任务
 */
public class ScheduledJob implements Job {

    private static final Logger logger= Logger.getLogger(ScheduledJob.class);

    @Override
    public void execute(JobExecutionContext jobExecutionContext) throws JobExecutionException {

        //执行任务逻辑....
        logger.info("执行自定义定时任务");
    }
}
```

### 2、自定义开启关闭任务的管理器类

为了之后项目中使用方便我们抽象出一个任务调度管理类 SchedulerManager.java，我们开启、暂停、恢复、停止、移除所有任务额功能都是通过它去执行。

``` java
import org.quartz.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.quartz.SchedulerFactoryBean;
import org.springframework.stereotype.Component;

/*
 * 此处可以注入数据库操作，查询出所有的任务配置
 */
@Component
public class SchedulerManager {

    @SuppressWarnings("SpringJavaInjectionPointsAutowiringInspection")
    @Autowired
    private SchedulerFactoryBean schedulerFactoryBean;
    private JobListener scheduleListener;

    /**
     * 开始定时任务
     * @param jobName
     * @param jobGroup
     * @throws SchedulerException
     */
    public void startJob(String cron,String jobName,String jobGroup,Class<? extends Job> jobClass) throws SchedulerException
    {
        Scheduler scheduler = schedulerFactoryBean.getScheduler();
        if(scheduleListener==null){
            scheduleListener=new SchedulerListener();
            scheduler.getListenerManager().addJobListener(scheduleListener);
        }
        JobKey jobKey=new JobKey(jobName,jobGroup);
        if(!scheduler.checkExists(jobKey))
        {
            scheduleJob(cron,scheduler,jobName,jobGroup,jobClass);
        }
    }

    /**
     * 移除定时任务
     * @param jobName
     * @param jobGroup
     * @throws SchedulerException
     */
    public void deleteJob(String jobName,String jobGroup) throws SchedulerException
    {
        Scheduler scheduler = schedulerFactoryBean.getScheduler();
        JobKey jobKey=new JobKey(jobName,jobGroup);
        scheduler.deleteJob(jobKey);
    }
    /**
     * 暂停定时任务
     * @param jobName
     * @param jobGroup
     * @throws SchedulerException
     */
    public void pauseJob(String jobName,String jobGroup) throws SchedulerException
    {
        Scheduler scheduler = schedulerFactoryBean.getScheduler();
        JobKey jobKey=new JobKey(jobName,jobGroup);
        scheduler.pauseJob(jobKey);
    }
    /**
     * 恢复定时任务
     * @param jobName
     * @param jobGroup
     * @throws SchedulerException
     */
    public void resumeJob(String jobName,String jobGroup) throws SchedulerException
    {
        Scheduler scheduler = schedulerFactoryBean.getScheduler();
        JobKey triggerKey=new JobKey(jobName,jobGroup);
        scheduler.resumeJob(triggerKey);
    }
    /**
     * 清空所有当前scheduler对象下的定时任务【目前只有全局一个scheduler对象】
     * @throws SchedulerException
     */
    public void clearAll() throws SchedulerException {
        Scheduler scheduler = schedulerFactoryBean.getScheduler();
        scheduler.clear();
    }

    /**
     * 动态创建Job
     * 此处的任务可以配置可以放到properties或者是放到数据库中
     * Trigger:name和group 目前和job的name、group一致，之后可以扩展归类
     * @param scheduler
     * @throws SchedulerException
     */
    private void scheduleJob(String cron,Scheduler scheduler,String jobName,String jobGroup,Class<? extends Job> jobClass) throws SchedulerException{
        /*
         *  此处可以先通过任务名查询数据库，如果数据库中存在该任务，更新任务的配置以及触发器
         *  如果此时数据库中没有查询到该任务，则按照下面的步骤新建一个任务，并配置初始化的参数，并将配置存到数据库中
         */
        JobDetail jobDetail = JobBuilder.newJob(jobClass).withIdentity(jobName, jobGroup).build();
        // 每5s执行一次
        CronScheduleBuilder scheduleBuilder = CronScheduleBuilder.cronSchedule(cron);
        /*
         * CronTrigger为我们提供了执行任务的触发器
         */
        CronTrigger cronTrigger = TriggerBuilder.newTrigger().withIdentity(jobName, jobGroup).withSchedule(scheduleBuilder).build();

        scheduler.scheduleJob(jobDetail,cronTrigger);
    }

}
```

### 3、任务监听器

创建一个任务的监听器

``` java
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;
import org.quartz.JobListener;

public class SchedulerListener implements JobListener {
    public static final String LISTENER_NAME = "QuartSchedulerListener";

    @Override
    public String getName() {
        return LISTENER_NAME; //must return a name
    }

    //任务被调度前
    @Override
    public void jobToBeExecuted(JobExecutionContext context) {

        String jobName = context.getJobDetail().getKey().toString();
        System.out.println("jobToBeExecuted");
        System.out.println("Job : " + jobName + " is going to start...");

    }

    //任务调度被拒了
    @Override
    public void jobExecutionVetoed(JobExecutionContext context) {
        System.out.println("jobExecutionVetoed");
        //可以做一些日志记录原因

    }

    //任务被调度后
    @Override
    public void jobWasExecuted(JobExecutionContext context,
                               JobExecutionException jobException) {
        System.out.println("jobWasExecuted");

        String jobName = context.getJobDetail().getKey().toString();
        System.out.println("Job : " + jobName + " is finished...");

        if (jobException!=null&&!jobException.getMessage().equals("")) {
            System.out.println("Exception thrown by: " + jobName

                    + " Exception: " + jobException.getMessage());

        }

    }
}
```

### 4、涉及到 Quartz 的一些概念，简单说明一下

**具体详见我的另一博文：**[Quartz作业调度](https://eakamm.github.io/post/quartz-zuo-ye-diao-du)

**Job:** 被执行的任务

**Scheduler:** 负责调度任务，如：开始 / 结束一个调度

**Trigger:** 负责执行任务的触发器（这里我用的是 CronTrigger 可以用 cron 表达式去执行任务的触发器）如："0/5 * * * * ?" // 每五秒执行一次，具体使用方法可以查阅一下官网。

**JobDetail:** 封装 Job，Scheduler 真正调度的对象，包括 Job 名称，组等信息。

**JobListener:** 任务执行的监听器，可以监听到任务执行前、后以及未能成功执行抛出异常。

### 5、使用示例

这里我写了一个简单的 Controller 去开启 / 停止任务调度：

``` java
import com.yu.scloud.baseframe.frame.utils.quartz.ScheduledJob;
import com.yu.scloud.baseframe.frame.utils.quartz.SchedulerManager;
import org.quartz.SchedulerException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/quartz")
public class QuartzController{

    @Autowired
    public SchedulerManager myScheduler;

    @RequestMapping(value = "/job2",method = RequestMethod.GET)
    public String scheduleJob2()
    {
        try {
            myScheduler.startJob("0/5 * * * * ?","job2","group2", ScheduledJob.class);//每五秒执行一次
            //0 0/5 14 * * ?在每天下午2点到下午2:55期间的每5分钟触发
            //0 50 14 * * ?在每天下午2点50分5秒执行一次
//            myScheduler.startJob("5 50 14 * * ?","job2","group2", ScheduledJob.class);
            return "启动定时器成功";
        } catch (SchedulerException e) {
            e.printStackTrace();
        }
        return "启动定时器失败";
    }
    @RequestMapping(value = "/del\_job2",method = RequestMethod.GET)
    public String deleteScheduleJob2()
    {
        try {
            myScheduler.deleteJob("job2","group2");
            return "删除定时器成功";
        } catch (SchedulerException e) {
            e.printStackTrace();
        }
        return "删除定时器失败";
    }

}
```

启动服务，访问就会开启一个定时任务，可以打开控制台查看打印信息。OK! 关于在 SpringBoot 中 Quartz 定时任务调度的使用，就介绍到这里。
