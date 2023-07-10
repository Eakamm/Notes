# 更新Nginx版本

### 1、手动编译安装nginx

以离线源码更新nginx为例

```sh
[root@VM000000505 ~] tar -zxvf nginx-1.24.0.tar.gz
[root@VM000000505 ~] cd nginx-1.24.0
#查询nginx配置参数
[root@VM000000505 nginx-1.24.0] nginx -V
--prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module --user=nginx --group=nginx
[root@VM000000505 nginx-1.24.0] ./configure --with-http_stub_status_module --with-http_ssl_module --user=nginx --group=nginx
[root@VM000000505 nginx-1.24.0] make && make install
[root@VM000000505 nginx-1.24.0] ls /usr/local/nginx/sbin/
nginx  nginx.old
```

出现新nginx与旧nginx的备份

### 2、手动更新

考虑到新版本的nginx可能会有问题，采用手动更新方式，保留新老两个进程，方便回滚

```sh
[root@VM000000505 nginx-1.24.0] ps -ef | grep nginx
root      25401 185365  0 14:49 pts/0    00:00:00 grep --color=auto nginx
# 找到master的任务的pid
root      85765      1  0  2022 ?        00:00:00 nginx: master process ./nginx
nginx    220377  85765  0 Apr04 ?        00:00:11 nginx: worker process
#发送一个指令，启动新版本nginx进程
[root@VM000000505 nginx-1.24.0] kill -USR2 85765
[root@VM000000505 nginx-1.24.0] ps -ef | grep nginx
nginx     50071  85765  0 16:19 ?        00:00:00 nginx: worker process
#新版本进程
root      50620  85765  0 16:21 ?        00:00:00 nginx: master process ./nginx
nginx     50621  50620  0 16:21 ?        00:00:00 nginx: worker process
root      50627  47592  0 16:22 pts/3    00:00:00 grep --color=auto nginx
#老版本进程
root      85765      1  0  2022 ?        00:00:00 nginx: master process ./nginx
nginx    220377  85765  0 Apr04 ?        00:00:11 nginx: worker process
#停止老版本nginx工作进程，只保留master进程
[root@VM000000505 nginx-1.24.0] kill -WINCH 85765
[root@VM000000505 nginx-1.24.0] ps -ef | grep nginx
root      50620  85765  0 16:21 ?        00:00:00 nginx: master process ./nginx
nginx     50621  50620  0 16:21 ?        00:00:00 nginx: worker process
root      85765      1  0  2022 ?        00:00:00 nginx: master process ./nginx

```



