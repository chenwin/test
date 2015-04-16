#### Native、Docker容器和KVM虚拟机CPU、内存性能对比测试 ####
声明：  
本博客欢迎转发，但请保留原作者信息!  
博客地址：http://www.51gocloud.com  
内容系本人学习、研究和总结，如有雷同，实属荣幸！

##### CPU性能测试 #####

CPU性能测试主流测试工具为Linpick，采用高斯消元法求解N元一次稠密线性代数方程组，来评价高性能计算机的浮点性能。

本次测试使用针对intel cpu优化过的版本，Linpick下载地址如下

http://registrationcenter.intel.com/irc_nas/5232/l_lpk_p_11.2.2.010.tgz

运行解压目录下的/linpack_11.2.2/benchmarks/linpack/runme_xeon64
会计算1000阶到45000阶的稠密线性代数方程组

测试步骤，根据实际numactl --hardware的情况，分为2组测试，Native和Docker时
    1 socket 1 numa情况
    numactl --physcpubind=1,3,5,7,9,11,13,15,17,19,21,23 --localalloc ./runme_xeon64
    
    2 socket 2 numa情况
    numactl --physcpubind=0-23 --interleave=0,1 ./runme_xeon64


KVM虚拟机时，是在启动参数做控制，在内部执行./runme_xeon64即可
    1 socket 1 numa情况
    numactl --physcpubind=1,3,5,7,9,11,13,15,17,19,21,23 /usr/libexec/qemu-kvm
    
    2 socket 2 numa情况
    numactl --physcpubind=0-23 --interleave=0,1 /usr/libexec/qemu-kvm

为了保证测试的一致性，host和容器、虚拟机都采用CentOS7 x86_64系统

环境的CPU信息Intel(R) Xeon(R) CPU E5645  @ 2.40GHz 2核24 cpu，2 socket 2 numa下测试结果如下
结果取平均值，单位为Average (Gflops)

    Size 	LDA   	Align	Native		Docker容器	KVM虚拟机
    1000	1000	4		15.0447		7.9979		14.7962
    2000	2000	4		37.1137		15.3798		31.9375
    5000	5008	4		66.7433		61.2764		26.0675
    10000	10000	4		66.0362		74.2456		34.6119
    15000	15000	4		90.0891		78.9916		37.2572
    18000	18008	4		89.7938		92.0565		37.7084
    20000	20016	4		91.0615		91.2076		38.0796
    22000	22008	4		92.7752		86.0396		37.0483
    25000	25000	4		94.2644		94.5307		37.3008
    26000	26000	4		92.4121		94.6419		37.3398
    27000	27000	4		93.7685		93.7615		37.4003
    30000	30000	1		94.5025		95.1876		37.4814
    35000	35000	1		93.4128		93.1904		37.6363
    40000	40000	1		94.7671		95.181		38.6363
    45000	45000	1		95.3708		95.3003		38.6485

测试结论：
Docker与Native的CPU性能基本相同，KVM虚拟机与两者有较大差距

##### 内存性能测试 #####
内存测试分为内存带宽性能测试（Stream）和随机内存访问测试 （RandomAccess）。
采用IBM的测试工具集
git clone https://github.com/thewmf/kvm-docker-comparison.git

测试步骤同上,


环境的内存信息Kingston DDR3 1333MHz 8G*6共48G

###### 内存带宽测试 ######
copy/scale/add/Triad对应四种测试内存的方式

1 socket 1 numa情况，单位Rate (GB/s)

    Function	Native	Dokcer容器	KVM虚拟机
    Copy:   	9.6354	9.6394		9.374
    Scale:  	9.6487	9.6471		9.322
    Add:		10.1717	10.1726		9.8141
    Triad:  	10.1353	10.1508		9.8328

2 socket 2 numa情况，单位Rate (GB/s)

    Function	Native	Dokcer容器	KVM虚拟机
    Copy:   	16.7581	16.3654		14.5261
    Scale:  	16.7292	16.376		14.6376
    Add:		18.7625	18.4028		16.3504
    Triad:  	18.7334	18.2576		16.2031

测试结论：
Docker与Native的内存带宽性能基本相同，KVM虚拟机与两者略有差距

###### 内存随机访问测试 ######
kvm-docker-comparison项目把内存写死了，会报错Cannot allocate memory: Cannot allocate memory

需要重新修改./RandomAccess/gups.c

totalMem = params->HPLMaxProcMem; 取消注释即可，同时注释掉下面一行写死的totalMem。

1 socket 1 numa情况，单位Updates per second [GUP/s]

    Native	  		Dokcer容器		KVM虚拟机
    0.041168698		0.039203536		0.034275562
    0.038914879		0.037857565		0.032991751
    0.039253397		0.041495306		0.034591057
    0.038486103		0.039736963		0.035324828
    0.039040533		0.037707405		0.03335802

2 socket 2 numa情况，单位Updates per second [GUP/s]

    Native	  		Dokcer容器		KVM虚拟机
    0.015721764		0.015956521		0.01485213
    0.016026846		0.015556186		0.015797386
    0.015737673		0.015876744		0.01497277
    0.015933741		0.015789459		0.015364381
    0.015755006		0.015456171		0.015490426

测试结论:
内存随机访问Native最好，docker次之，虚拟机最差。

备注：
linpack在kvm-docker-comparison里也有，但算的是45000阶10次，耗时太久约9个小时，故使用intel的。
