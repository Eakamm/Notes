# 安装lua-nginx-module模块

1、下载

```cmd
wget https://github.com/vision5/ngx_devel_kit/archive/refs/tags/v0.3.1.tar.gz
tar -zxvf ngx_devel_kit-0.3.1.tar.gz

wget https://github.com/openresty/lua-nginx-module/archive/refs/tags/v0.10.19.tar.gz
tar -zxvf lua-nginx-module-0.10.19.tar.gz
```

## 2、安装luajit



## 3、配置luajit

```cmd
#编辑profile文件
[root@VM_32_3_centos objs]# vim /etc/profile
# 在底部添加lua的包路径
export LUA_PATH="/usr/local/servers/openresty-1.19.3.1/nginx/lua/?.lua;/usr/local/servers/openresty-1.19.3.1/lualib/?.lua;;"
export LUAJIT_LIB=/usr/local/servers/openresty-1.19.3.1/luajit/lib
export LUAJIT_INC=/usr/local/servers/openresty-1.19.3.1/luajit/include/luajit-2.1

#生效配置文件
root@VM_32_3_centos $ source /etc/profile

```

## 4、生成新的nginx

### 1、找到nginx源文件

我们需要通过nginx源文件重新编译生成nginx，如果找不到源文件，可以查看当前nginx版本,去官网下载相应的源码。

```cmd
[root@VM_32_3_centos objs]# nginx -V
nginx version: nginx/1.16.1
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-44) (GCC) 
built with OpenSSL 1.1.1k  25 Mar 2021
TLS SNI support enabled
configure arguments: --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC' --with-ld-opt='-Wl,-z,relro -Wl,-z,now -pie' 	
```

复制`configure arguments:`后面的参数，这是当前nginx的配置，我们接下来要在这个基础上添加新的模块

### 2、生成新的nginx

我们在重新编译nginx的时候要添加

`--add-module=/usr/local/servers/ngx_devel_kit-0.3.1/ --add-module=/usr/local/servers/lua-nginx-module-0.10.19/ --with-openssl=/usr/local/servers/openssl-1.1.1k`

如果openssl之前已经配置过，就不需要添加了

完整代码：

```cmd
./configure --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC' --with-ld-opt='-Wl,-z,relro -Wl,-z,now -pie' --add-module=/usr/local/servers/ngx_devel_kit-0.3.1/ --add-module=/usr/local/servers/lua-nginx-module-0.10.19/ --with-openssl=/usr/local/servers/openssl-1.1.1k
```

