7.0
修改主机名
hostnamectl set-hostname XXX
hostnamectl status

修改IP
nmtui图形界面修改，重启网络服务生效

修改网卡名为eth形式
vi /boot/grub2/grub.cfg在quiet LANG=en_US.UTF-8后面增加
net.ifnames=0 biosdevname=0
重启主机生效或执行：grub2-mkconfig -o /boot/grub2/grub.cfg

关闭selinx 
/etc/sysconfig/selinux 中 追加 SELINUX=disabled

配置本地dns
nameserver 8.8.8.8
nameserver 8.8.4.4

