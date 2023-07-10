> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/qq_41702466/article/details/109222366)

**前言**  
        老样子，先来讲讲我所遇到的问题，大概是需要外网访问一个内网服务器，想通过这台内网服务器访问到到另外一台内网服务器（两台内网服务器互通），可以说是跨服务器访问。咨询过大佬后自己在总结一下。大佬一听，立马跟我说，这个很简单，需要 [nginx](https://so.csdn.net/so/search?q=nginx&spm=1001.2101.3001.7020) 做反向代理即可，那么如何操作呢，接下来回顾一下。  
        首先情况摸清楚：两台服务器，一台外网可访问到的内网服务器一【10.25.7.169:8070】，另一台外网不可访问到的内网服务器二【10.25.12.188:8080】。我们要让外网去访问服务器一，然后通过 nginx 做[反向代理](https://so.csdn.net/so/search?q=%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86&spm=1001.2101.3001.7020)，间接访问服务器二。首先要在服务器一上安装 nginx。

linux 离线安装 Nginx 详细步骤
---------------------

### 一、 [下载 nginx 安装环境](https://download.csdn.net/download/qq_41702466/13011728)：gcc、g++、pcre、zlib、nginx  
#### 1、gcc

```shell
##	安装nginx需要将官网下载的源码进行编译，编译一以来gcc和g++，如果没有gcc环境，需要安装gcc
##	下载好所需要的文件后上传至服务器，进入gcc的根目录执行如下操作，
##	当执行下面语后，系统会总动选出所需要的依赖包进行安装不需要的就会自动清理。

[root@xjxx-wwapp gcc]#rpm -Uvh *.rpm --nodeps --force

##	最后查询一下是否安装成功

[root@xjxx-wwapp gcc]#gcc -v
[root@xjxx-wwapp gcc]#g++ -v
##	如果出现他们各自的版本号，说明安装成功
```

#### 2、pcre

```shell
##	pcre是一个库，包括perl兼容的正则表达式库
##	nginx的http模块使用pcre来解析正则表达式，所以需要在linux上安装pcre库。
##	同样进入到pcre根目录下执行如下命令。

[root@xjxx-wwapp pcre]#rpm -ivh pcre-8.32-17.el7.x86_64.rpm --force
[root@xjxx-wwapp pcre]#rpm -ivh pcre-devel-8.32-17.el7.x86_64.rpm --force
```

#### 3、zlib

```shell
##	zlib库提供了很多种压缩和解压缩的方式，nigin使用zlib对http包的内容进行gzip。

[root@xjxx-wwapp zlib]#rpm -ivh zlib-1.2.7-18.el7.x86_64.rpm    --force
[root@xjxx-wwapp zlib]#rpm -ivh zlib-devel-1.2.7-18.el7.x86_64.rpm   --force
```

#### 4、nginx

```shell
##	进入nginx的根目录解压

[root@xjxx-wwapp nginx]#tar -xzvf nginx-1.18.0.tar.gz

##	将源码移动到对应目录下

[root@xjxx-wwapp nginx]#sudo mv nginx-1.18.0 /usr/local/
[root@xjxx-wwapp nginx]#cd /usr/local/nginx-1.18.0/
[root@xjxx-wwapp nginx-1.18.0]#./configure

##	编译

[root@xjxx-wwapp nginx-1.18.0]#make

##	安装

[root@xjxx-wwapp nginx-1.18.0]#make	install

##	运行nginx

[root@xjxx-wwapp nginx-1.18.0]#cd sbin/
[root@xjxx-wwapp sbin]#./nginx

##	检查是否安装正确

[root@xjxx-wwapp sbin]#/usr/local/nginx-1.18.0/sbin/nginx -t

##	nginx的启动、停止、退出、重新加载配置文件的命令

[root@xjxx-wwapp sbin]#/./nginx
[root@xjxx-wwapp sbin]#/./nginx -s stop
[root@xjxx-wwapp sbin]#/./nginx -s quit
[root@xjxx-wwapp sbin]#/./nginx -s reload
```

### 二、配置 nginx 反向代理

```nginx
##	进入nginx配置文件
[root@xjxx-wwapp conf]#vim nginx.conf

##	复制一组server，然后进行如下修改
server {
		##	监听8080端口
        listen 8080;
        server_name localhost;
		
		##	路由1配置：如果请求的url包含/，走本地的8070端口访问
        location / {
            proxy_pass http://127.0.0.1:8070;
            proxy_connect_timeout 300s;
            proxy_send_timeout 900;
            proxy_read_timeout 900;
            proxy_buffer_size 32k;
            proxy_buffers 4 64k;
            proxy_busy_buffers_size 128k;
            proxy_redirect off;
            proxy_hide_header Vary;
            proxy_set_header Accept-Encoding '';
            proxy_set_header Referer $http_referer;
            proxy_set_header Cookie $http_cookie;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
		
		##	路由2配置：如果url遇到/appFileDownLoad/的请求，走另外一台内网服务器的8080端口
        location /appFileDownLoad/ {
			##	rewrite 重写当前路径，去掉/appFileDownLoad/标记
            rewrite ^/appFileDownLoad/(.*) /$1 break;
            proxy_pass http://10.25.12.188:8080;
        }
}
```

### 三、示例：

​		假设我们通过外网访问到一个请求：http:// 外网ip:9527/HVPS/MainServlet/op=report&pid=MAX_DAY，外网访问到内网服务器一【10.25.7.169:8070】，通过 nginx 反向代理，根据请求 url 发现，并没有特殊的标记，然后 nginx 将请求发送给本地；  
​		再假设我们通过外网访问一个请求：http:// 外网 ip:9527/appFileDownLoad/norone/fileDownLoad.do?type=reportDoc&file=1603247989056.xls，外网访问到内网服务器一【10.25.7.169:8070】，通过 nginx 反向代理，根据请求 url 发现，有特殊标记 / appFileDownLoad/，然后 nginx 将请求发送给内网服务器二【http://10.25.12.188】  
到此为止，我的问题就已经解决了。