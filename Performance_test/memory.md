#### 内存带宽性能测试stream ####
[主页]
[http://www.cs.virginia.edu/stream/](http://www.cs.virginia.edu/stream/)

[FAQ]
[http://www.cs.virginia.edu/stream/ref.html](http://www.cs.virginia.edu/stream/ref.html)

[源码]
[http://www.cs.virginia.edu/stream/FTP/Code/](http://www.cs.virginia.edu/stream/FTP/Code/)

或者


使用stream-scaling项目，自动从[源码]下载编译stream.c测试

    git clone https://github.com/gregs1104/stream-scaling.git    
    ./stream-scaling

#### 内存随即访问测试RandomAccess ####

#### IBM测试工具集 ####
[https://github.com/thewmf/kvm-docker-comparison](https://github.com/thewmf/kvm-docker-comparison)

[https://github.com/thewmf/kvm-docker-comparison.git](https://github.com/thewmf/kvm-docker-comparison.git)

http://icl.cs.utk.edu/projectsfiles/hpcc/RandomAccess/

所有的测试工具

http://icl.cs.utk.edu/hpcc/
http://baike.baidu.com/view/485828.htm#3

下面是linpack运行的参数配置文件的例子，其中包括一个参数。
v 计算的点数，原则上是计算的点数越多，则会遍历多种计算的性能情况，更能找到最好的性能点，但是点数越多则运算时间越长。
v 点数的分布。即设定几个不同的阶数值，一般是在N附近的时候的阶数分布较为密，以便找到最佳性能数据。
v 每个计算点的计算次数，为了减少测试误差，增加每点的计算次数取其平均值，得到比较可信的性能数据。
v 设置内存的对齐尺寸，内存分配的时候的内存对其方式，可以提高内存的读取的效率，提高性能测试结果，但是设置过大会产生一定的内存空间的浪费，一般为4KB或8KB
