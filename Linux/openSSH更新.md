## openSSH的升级安装

升级前多开几个ssh窗口，防止错误/出现问题后无法连接到服务器

### 1、备份

```sh
cp /usr/bin/ssh /usr/bin/ssh.bak
cp /usr/sbin/sshd /usr/sbin/sshd.bak
mv /etc/ssh /etc/ssh.bak
# 进入安装包位置解压
tar -zxvf openssh-8.9p1.tar.gz
cd openssh-8.9p1
./configure --prefix=/usr/ --sysconfdir=/etc/ssh --with-ssl-dir=/usr/local/ssl --with-zlib --with-md5-passwords
make && make install
```

### 2、修改启动文件和pam
```sh
cp ./contrib/redhat/sshd.init /etc/init.d/sshd
cp -a contrib/redhat/sshd.pam /etc/pam.d/sshd.pam
mv /usr/lib/systemd/system/sshd.service /usr/lib/systemd/system/sshd.service_bak
ssh -V
#执行ssh -V 应该能看到新的版本了,重新启动ssh
systemctl daemon-reload
systemctl restart sshd
systemctl status sshd
```


即可完成OPENSSH的安装，SSH升级完成

###  3、升级后密码无法登录

密码无法登录的话修改ssh配置文件需要调整，打开ssh配置文件

```sh
vi /etc/ssh/sshd_config
```
打开如下功能
```shell
PermitRootLogin yes   #限制root用户登录，如果使用的是root用户，那么就需要打开
PubkeyAuthentication yes   #打开秘钥验证
PasswordAuthentication yes  #打开密码验证
```