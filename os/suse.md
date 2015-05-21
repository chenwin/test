#### 安装zypper ####
    rpm -ivh libzypp-9.34.0-0.7.15.x86_64.rpm
    rpm -ivh zypper-1.6.307-0.7.12.x86_64.rpm

#### 建立本地源 ####
    vi /etc/zypp/repos.d/all.repo
    写入下面的内容
    [all]
    enabled=1
    autorefresh=0
    baseurl=dir:///home/Icehouse/SLE_11_SP3
    type=plaindir

#### 刷新源 ####
    # zypper refresh
    Retrieving repository 'all' metadata [done]
    Building repository 'all' cache [done]
    All repositories have been refreshed.
