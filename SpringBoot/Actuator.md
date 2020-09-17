# Actuactor

## 1、导入Actuator

pom.xml中导入包

``` xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>

```

在Spring2.x以上版本需要配置application.yml文件暴露所有监管点：

``` yml
management:
  endpoints:
    web:
      base-path: /actuator
      exposure:
        include: "*"
```

在Spring2.x以上版本的访问路经也有不同 `http://localhost:8080/actuator/beans`

| ID                                                      | Description                                                                                                                                                                  | Enabled by default |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| auditevents                                             | Exposes audit events information for the current application\.                                                                                                               | Yes                |
| beans                                                   | Displays a complete list of all the Spring beans in your application\.                                                                                                       | Yes                |
| conditions                                              | Shows the conditions that were evaluated on configuration and auto\-configuration                                                                                            |                    |
| classes and the reasons why they did or did not match\. | Yes                                                                                                                                                                          |                    |
| configprops                                             | Displays a collated list of all @ConfigurationProperties\.                                                                                                                   | Yes                |
| env                                                     | Exposes properties from Spring’s ConfigurableEnvironment\.                                                                                                                   | Yes                |
| flyway                                                  | Shows any Flyway database migrations that have been applied\.                                                                                                                | Yes                |
| health                                                  | Shows application health information\.                                                                                                                                       | Yes                |
| httptrace                                               | Displays HTTP trace information \(by default, the last 100 HTTP request\-response                                                                                            |                    |
| exchanges\)\.                                           | Yes                                                                                                                                                                          |                    |
| info                                                    | Displays arbitrary application info\.                                                                                                                                        | Yes                |
| loggers                                                 | Shows and modifies the configuration of loggers in the application\.                                                                                                         | Yes                |
| liquibase                                               | Shows any Liquibase database migrations that have been applied\.                                                                                                             | Yes                |
| metrics                                                 | Shows ‘metrics’ information for the current application\.                                                                                                                    | Yes                |
| mappings                                                | Displays a collated list of all @RequestMapping paths\.                                                                                                                      | Yes                |
| scheduledtasks                                          | Displays the scheduled tasks in your application\.                                                                                                                           | Yes                |
| sessions                                                | Allows retrieval and deletion of user sessions from a Spring Session\-backed session store Not available when using Spring Session’s support for reactive web applications\. | Yes                |
| shutdown                                                | Lets the application be gracefully shutdown\.                                                                                                                                | No                 |
| threaddump                                              | Performs a thread dump\.                                                                                                                                                     | Yes                |

## 2、beans

## 3、conditions（旧版本autoconfig）

/conditions端点能告诉你为什么会有这个Bean，或者为什么没有这个Bean。

## 4、metrics(运行时度量)

Actuator提供了一系列端点，让你能在运行时快速检查应用程序。

### 4.1 获取已知度量名

[点击该链接可以获取到已知的度量名](http://localhost:8080/actuator/metrics)

```url
http://localhost:8080/actuator/metrics
``` 

### 4.2 获取相应度量
