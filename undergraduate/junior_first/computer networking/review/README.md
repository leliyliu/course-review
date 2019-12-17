[TOC]

# 计算机网络

![tcpip](fig/refinal.png)

## 第一章 计算机网络概论

几个基本概念：

+ 信息、数据、信号
+ 串行通信与并行通信
+ 传输介质与信道
+ 信道带宽与信道容量
+ 传输速率
+ 信噪比
+ 误码率
+ 传输延迟
+ 网络协议
+ 报文、分组

多台计算机之间的连接，方式： 共享式连接 和 交换式连接

交换方式包括：电路交换与分组交换

对于网络的扩展方式：

+ 可以利用网桥对网络进行扩展，网桥包括了多种形式
+ 多交换机扩展，利用多个交换机改变网络结构

英特网的结构：

+ network edge: end systems running TCP/IP protocol and applications
+ access networks: wired, wireless communication links
+ network core: interconnected routers, running routing protocol and IP protocol

接入网络(access networks)：

+ residential access networks（住宅接入网络）
  + DSL: digital subscriber line
  + HFC: hybrid fiber coax(cable modem)
  + FTTH: fiber to the home
+ institutional access networks (school,company)（组织接入网络）
+ wireless access networks(WiFi, 4G/5G)（无线接入网络）

包交换网络中的一些核心问题:

1. 当同时又多个包同时到达同一个线路，路由器是如何处理的？（buffer, store and forward,queue,congest)  how does a router deal with the packets when packets arrive for the same output link at the same time ?
2. 路由器是如何知道一个包应该向何处转发的？(routing)  how does a router know which router to forward a packet to ? 
3. 一个接收器是如何知道正确的包的顺序的？ (eg. TCP) how does a receiver know the correct ordering of packets
4. 发送方是如何判断包丢失并且需要重传的？ (eg. TCP) how does a sender know which packet is lost and must be retransmitted



## 第二章 应用层

### 应用协议与进程通信模型

#### 应用协议

应用：通信和分发处理，运行在用户空间中，通过交换不同的信息来实现不同的应用，例如email,ftp,web等等。

应用协议：根据不同的应用需求定义不同的消息，并通过底层的协议进行信息的通信和传输（TCP,UDP)

#### 进程通信

进程通信中，进程是运行在一个主机上的程序，在同一个进程中，进程通信使用进程间通信方式（通过操作系统定义），而对于不同进程，则使用信息交互(exchanging message)，不同主机之间的通信模式主要分为：客户端/服务器模式 和p2p模式(个人对个人)。

##### Sockets

Sockets是在应用层和传输层之间的一个类似接口一样的东西，进程会将其消息发送到socket中，并以此方式进行传输。这个会在[网络编程方法](### 网络编程方法)中具体介绍。

##### 客户/服务器模型

服务器端：

+ 等待连接
+ 永远在线
+ 固定永久IP地址
+ 用于扩展的服务器集群

客户端：

+ 与服务器建立初始连接
+ 间歇性可连接
+ 动态IP地址分配
+ 客户端之间不直接交流

##### P2P 模型

没有固定的服务器，随意的直接相连，每台主机都是间歇性连接，并且可以改变IP地址。

##### 混合客户/服务器和p2p模型

![hybrid](fig/re2-1.png)

#### 地址分配

为了接受到相应的信息，每个进程都应该有相应的标识符，主机设备都拥有一个32位的特定IP地址，但是许多进程都需要运行在同一个主机上，故而还需要设置端口(port numbers)，对于一般的应用，都有其相对固定的端口，例如：

+ HTTP :  80
+ MAIL: 25

端口实际上有16位，一般而言，1-1023之间的端口号是分配管理的，如果我们需要设计一些新的应用，尽量不要使用这些端口号。

### 传输层服务对应用的支持

**在进行应用设计的时候，需要考虑到哪些点：data loss,timing 和 bandwidth，对于不同的应用而言，其对于数据是否有错误和损失是有不同的标准的，而同时，有些应用讲求实时性，而另一些则不需要；同样的，对于一些应用，它有最低带宽要求的限制，而对于另一些应用，则没有。**

例如：

![example](fig/re2-3.png)

#### Internet transport services

##### TCP（具体参考传输层）

面向连接的服务

可靠的传输服务

流量控制

拥塞控制

不提供：时间和最小带宽保障

##### UDP

不可靠的数据传输

不提供：连接建立，可靠性，流量控制，拥塞控制，时间和最小带宽保障

==为什么要提供UDP服务？==

**因为UDP服务非常简单，容易实现，在实际应用中有很大价值，而对于某些应用而言，确实不需要提供过于复杂的服务，只需要极为简单的服务即可，简单的消息处理能够减少处理的时间和复杂性。**

### 文件传输服务与协议

#### Whole-file transfer

用户首先获得当前本地一个文件的复制并操作这个副本，大多数这种文件的传输不是在本机之间进行的，也不是整个直接进行的。

相应的应用有：离线远端文件下载，软件和信息分发。

#### FTP：file transfer protocol

客户端使用TCP来与服务器建立连接。

特点：

+ 交互式：用户可使用命令行和服务器进行交互
+ 格式定义：客户端可以定义存储数据的类型和方式
+ 授权控制：客户端必须提供一个登陆的名字和密码

![ftp](fig/re2-4.png)

 双连接：控制连接和数据连接

![model](fig/re2-5.png)

![process](fig/re2-6.png)

主要理解ftp需要实现的功能：FTP主要需要实现文件的下载和上传，同时要考虑其自身的安全性，故而需要的操作主要是：

1. 文件的浏览和查找
2. 下载，上传功能（包括多个文件同时下载） 最基础的实现为建立队列，复杂的方式包括利用多线程方式进行
3. 登陆，选择下载文件
4. 文件下载内容和方式（binary file , text file）
5. ie..

### Web服务与协议

#### Web Client/Server Mode

**client**: **根据浏览的内容发出请求**，**并接受反馈信息和展示相应Web内容**

**server:服务器发送相应的请求的内容**

![mode](fig/re2-7.png)

![architecture](fig/re2-9.png)

可以看到，HTTP服务底层也是通过TCP协议实现的。

#### HTTP： HyperText Transfer Protocol

+ 标准的Web转换协议在Web服务器和客户端之间
+ HTTP 通常使用TCP连接（但是这不是在协议中规定好的）
+ HTTP是面向事务的客户机/服务器协议，每个事务都是独立处理的
+ 不高效但是简答
+ 链接到同一服务器和链接到其他服务器之间没有区别

服务器不维护关于过去客户端请求的信息

![http1.0](fig/re2-10.png)

![http1.02](fig/re2-11.png)

从http1.0 到http1.1 ，将非持续性的连接变为了持续性的连接，即不像上面所展示的那样，当server返回了相应请求的信息之后就会关闭TCP连接。因此，这样，能够减少整个HTTP工作时需要交互的信息量。 ==result: fewer RTTs,less slow start==

HTTP协议中传输的信息的格式为：

![format](fig/re2-12.png)

对于一个具体例子而言：

![request example](fig/re2-13.png)

![status](fig/re2-14.png)

#### 对于HTTP 1.0 的改进

对于一个无状态的HTTP连接而言，每一条请求都需要包含authorization，但是变为一个有状态的而言，（也就是现在使用的这种方式），那么可以利用cookies来保持这个连接的状态。

对于某些经常需要访问的网页而言，一般来说，客户端会对其进行cache 缓存，在这种情形下，会有这样的操作状况：向服务器端发送请求后，服务器端会根据客户端的相应请求，查看当前保存在客户端的结果是否为最新的，如果是，那么服务器不再发送相应内容，否则则进行发送 

![cache](fig/re2-15.png)

#### URL

对于一个URL(uniform resource locators)，其具体的格式为：

![url](fig/re2-16.png)

更多的例子：

![urls](fig/re2-17.png)

### 电子邮件服务与协议

#### 电子邮件系统

一个电子邮件系统包括三个主要部分： 用户代理，邮件服务器，简单邮件传输协议（smtp）

![system](fig/re2-18.png)

对于一个电子邮件的发送和接收过程而言，其具体连接方式为：

![smtp](fig/re2-19.png)

一个邮箱名应该为：local-part@domain-name

#### SMTP

同样是使用TCP协议来建立可靠的连接，应该包括三个阶段：

+ 握手
+ 信息的交换
+ 关闭连接

关于握手的一些具体交互信息，实际上可以参见之前做过的作业。

##### MIME编码

由于无法用ASCII编码表示所有的语言，故需要采用MIME编码方式来进行编码。

### 域名服务与协议

DNS: Domain Name System

由于对于网络的访问需要使用IP地址，但是我们一般习惯于使用名字来进行表示，故我们需要一个域名解析服务器来为我们解析域名 ： DNS

将名字和IP地址进行相应的映射：

+ 分配： 有一组服务器用于将网站名字解析为地址
+ 有效性：大多数名字可以本地被解析
+ 可靠性： 都会正确执行
+ 目的： 不要将地址限定为机器地址

#### DNS 域名服务器

##### 根目录域名服务器

##### 顶层域名服务器(top-level domain)

##### 授权域名服务器(authoritative)

##### 本地域名服务器(local)

DNS服务器请求地址转换的两种方式：

![地址转换](fig/re2-20.png)

![转换2](fig/re2-21.png)

#### Name server caching

为了降低查找对应IP地址的成本，一般而言，域名服务器都会对常用网站的映射进行缓存。故其具体步骤为：

![servercache](fig/re2-22.png)

![valid](fig/re2-23.png)

#### Host caching

除了域名服务器会对映射表进行缓存之外，主机也会对其进行缓存。

![host](fig/re2-24.png)

##### DNS 报文格式

![dns](fig/re2-25.png)

### 对等通信

#### P2P 与 客户-服务器的比较

![问题1](fig/re2-26.png)

对客户-服务器而言，时间为： $d_{cs} = max\{NF/u_s,F/min(d_i)\}$

而对于P2P而言，时间为： $d_{p2p}=max\{F/u_s,F/min(d_i),NF/(u_s + \sum u_i)\}$

可以看到，如果N越大，那么P2P模型对于文件的上传下载能提供更少的时间。

![res](fig/re2-27.png)

bittorrent 的例子。

对于P2P模型而言，不但是用于上传下载文件，同时还可以用于信息检索。文件传输是去中心化的，但是信息检索是高度中心化的。

### 网络编程方法



## 第三章 传输层

## 第四章 网络层

### 网络层功能

网络层协议在每个主机和路由之间都有。

##### 发送方(sending)

打包segments 到链路层

##### 接收方(receiving)

发送segments 到传输层

##### 路由(router)

校验，利用头部校验和进行校验，然后传递。

网络层主要有两大功能：路由和传递(routing  and forwarding)

#### 网络层的协议

网络层主要包括两种协议，IP协议和ICMP协议。对于IP协议而言，主要包括地址规定，数据报格式和包处理规定，对于其中的细节请参考[4.2](IP协议)。对于ICMP协议，其主要包括差错报告和路由器标识。

其中，路由协议主要是用于路径选择，主要包括RIP,OSPF,BGP等方式。

### IP协议

网络层提供的服务：

1. 面向无连接的服务(datagram-based)
   + 没有提前连接的建立被需要
   + 数据报的传递用目的主机地址标识
   + 每个数据报独立传输
2. 尽最大努力传递(unreliable service)
   + 数据报可以被长时间delay
   + 数据报可以被丢弃
   + 数据报乱序发送
   + 数据报冗余发送

#### IPv4数据包格式

![数据包格式](fig/re4-1.png)

IP地址包括网络号和主机号(net-id 和 host-id)

A类地址，B类地址，C类地址，D类地址，E类地址 0 , 10 , 110 , 1110 , 11110

如何获得一个IP地址：

+ 系统管理员中保存有ip地址
+ DHCP：Dynamic Host Configuration Protocol
  + host broadcasts "DHCP discover" msg
  + DHCP server responds with "DHCP offer" msg
  + host requests IP address: "DHCP request" msg
  + DHCP server sends address: "DHCP ack" msg
+ other protocol

网络连接（有不同的方式）有MTU(max transfer unit)，因此需要切割不同的数据包。

路由器转发数据包的过程：

1. 路由器决定目的地址的网络号
2. 如果为本地网络地址，则直接发送，否则转发
3. 检查网络号是否在路由表项中，如果在，则发送到相应端口，否则丢弃
4. TTL减1，并更新校验和
5. 传递到下一网络的接口中

#### IPv4地址问题及解决策略

无类地址划分（CIDR）

IP地址分为前缀和后缀两部分

##### CIDR路由聚合

主要考虑最长匹配原则。

NAT: network address translation

==motivation==：IP地址不够分配

+ 对所有设备而言，只有一个IP（或几个）
+ 可以改变设备的本地IP地址，而不改变外部网络
+ 可以不用改变设备的IP地址，而更换ISP服务
+ 设备的内部地址是不是外网可见的。

#### IPv6基础

##### IPv4局限性

+ IPv4地址资源枯竭
+ 路由成为互联网的瓶颈（网络数目增加，地址层次性差，数据包首部长度可变）
+ 缺乏服务质量保证
+ 配置较为繁琐

##### IPv4的改进措施

1. 无类型域间选路（CIDR）
2. 网络地址转换(NAT)

##### IPv6互联网的优势

+ 解决地址耗尽问题：更大的地址空间
+ 自动配置的支持（即插即用）
+ 改善网络性能
+ 方便各项业务开展
+ 安全性更高
+ 移动性支持

##### IPv6地址的表示方法

128位地址：由冒号分开的8组十六进制字段组成，CIDR IPv6前缀表示：（IPv6/前缀长度）

#### IPv6地址类型

单播地址

![地址类型](fig\re4-2.png)

### ICMP协议

 internet control message protocol

![ICMP](fig/re4-3.png)

![ICMPformat](fig/re4-4.png)

![tracer](fig/re4-5.png)

### 路由算法

通过图选择最短的到达路径。相关定义：

![抽象图](fig/re4-6.png)

主要包括链路状态路由算法，向量状态路由算法和.....

#### 链路状态算法

其实质是一个Dijkstra算法，一个节点知道其它所有节点（这是通过"link state broadcast"）实现的。

![具体算法](fig/re4-7.png)

![具体操作](fig/re4-8.png)

#### 距离向量算法

其实质上是Bellman-Ford算法。

![实现](fig/re4-9.png)

### 互联网路由协议

根据A,B,C类IP地址的划分，我们大概有2 million 个IP地址，那么很显然需要大量的空间。因此考虑Hierarchical Routing

##### Two-level routing 

###### Intra-AS routing

• all routers in same AS must run same intra-domain protocol
• routers in different AS can run different intra-domain routing
protocol
• gateway router: at “edge” of its own AS, has link(s) to router(s) in
other AS’es

###### Inter-AS routing

• routing among AS’es
• gateways perform inter-domain routing (as well as intra-domain
routing)

#### RIP

RIP协议是基于距离向量算法，使用“跳数”来衡量到达目标地址的路由距离

![RIP-1](fig/re4-10.png)

![RIP](fig/re4-11.png)

#### OSPF(open shortest path first)

使用链路状态算法

![OSPF](fig/re4-12.png)

使用OSPF的一些优点：

![advanceOSPF](fig/re4-13.png)

#### Internet inter-AS routing : BGP

border gateway protocol 提供

+ eBGP：获得网络的AS信息
+ iBGP：传递相应的AS信息到AS-internal 路由器
+ 决定一个"good" 路由

![BGPmessage](fig/re4-14.png)

### 软件定义网络SDN

逻辑中心管理层：

远程的控制中心和本地的路由器代理交互来形成一个路由表，进行路由传输。

一个逻辑中心的控制，能够更好地进行路由管理，避免路由器的一些细节配置，有更大的灵活性。

### 补充：RIP防止路由环路

#### 水平分割

    水平分割的概念
    由于路由器可能收到它自己发送的路由信息，而这种信息是无用的。
    
    水平分割的原理
    路由器从某个接口接收到的更新信息不允许再从这个接口发回去。
    
    水平分割的优点
    1，能够阻止路由环路的产生。
    2，减少路由器更新信息占用的链路带宽资源。
    水平分割(split horizons)的思想
    就是在路由信息传送过程中，不再把路由信息发送到接收到此路由信息的接口上。从而在一定程度上避免了环路的产生。

#### 毒性逆转（Poisoned Reverse）

毒性逆转实际上是一种改进的水平分割。

这种方法的运作原理是：路由器从某个接口上接收到某个网段的路由信息之后，并不是不往回发送信息了，而是发送，只不过是将这个网段的跳数设为无限大，再发送出去。

收到此种的路由信息后，接收方路由器会立刻抛弃该路由，而不是等待其老化时间到（Age Out）。这样可以加速路由的收敛。

#### 触发更新

若网络中没有变化，则按通常的30秒间隔发送更新信息。但若有变化，路由器就立即发送其新的路由表。这个过程叫做触发更新。

#### 抑制计时（holddown timer）

一条路由信息无效之后，一段时间内这条路由都处于抑制状态，即在一定时间内不再接收关于同一目的地址的路由更新。

如果，路由器从一个网段上得知一条路径失效，然后，立即在另一个网段上得知这个路由有效。这个有效的信息往往是不正确的，抑制计时避免了这个问题，而且，当一条链路频繁起停时，抑制计时减少了路由的浮动，增加了网络的稳定性。

## 链路层：链路、接入网和局域网（接口层原理和协议）

两种不同类型的链路层信道：广播信道和点对点通信链路。

### 接口层基础

接口层主要包括物理层和数据链路层两层：

+ 物理层：提供位流服务
  + 编码与解码
  + 时钟同步
  + 信号的发送与接收
  + 传输介质和拓扑定义
+ 数据链路层：提供可靠和不可靠的传输服务
  + 数据单元及寻址方式定义
  + 链路层差错检测
  + 链路层的复用和分用
  + 可靠数据传输
  + 共享式连接：提供介质访问控制方法

可以将接口技术按照范围分为三类：局域网，城域网和广域网，这里主要研究局域网。除此之外，还可以包括个人区域网和无线传感网络等。

### 局域网体系结构和组网方法

![局域网体系结构与数据封装](fig\re5-1)

![共享式和交换式局域网](fig\re5-2)

### 局域网编址与ARP协议

#### LLC和MAC地址

LLC地址是用于标识上层协议的，即是用于标识网络层的相应协议，现在网络层一般使用IP协议。而MAC地址被称为物理网络地址，简称物理地址，其实际上是标识了当前网络所在物理层的地址。

##### MAC地址和IP地址区分

IP地址实际上是一个网络层地址，它被用来传输数据报到目的网络

MAC地址是物理地址，被用来从一个接口传到另一个物理接口，故实际上，MAC地址需要在每一层都做相应的传输。

![image-20191211102400897](fig\re5-3)

每一个局域网中的网络信息中心都有一个特定的局域网地址（MAC地址），广播地址规定为：FF-FF-FF-FF

####  ARP：Address Resolution Protocol

每个在局域网上的IP结点都有一个ARP表项。一个ARP表项应该是这样一个三元组：<IP address; MAC address; TTL>

+ A知道B的IP地址，想知道B的物理地址
+ A广播ARP查询报文，包括了B的IP地址
+ B接收到ARP报文，回应给A其物理地址
+ A保存这样一个三元组

**ARP协议是一个插入即用的协议，它不需要网络管理的中介**

当不同局域网之间进行信息传输，路由的时候，A首先是将其发送到路由器R，并利用ARP协议进行查询MAC地址，并进行转发，同理，将由R查询后再次进行转发。

### 链路层差错控制

#### 循环冗余校验（CRC）

在数据链路层中，广泛使用==循环冗余校验（Cyclic Redundancy Check）==

计算方法：

![image-20191211105533255](fig\re5-4)

###### 生成多项式G在以太网中为：$G = x^{32}+x^{26}+x^{23}+x^{22}+x^{16}+x^{12}+x^{11}+x^{10}+x^8+x^7+x^5+x^4+x^2+x+1$

### 共享式以太网

#### 以太网的发展

![image-20191211110302450](fig\re5-5)

#### 共享式以太网连接方式与功能

服务：面向非连接的不可靠服务

功能：

+ 物理层：信号编码、时钟同步等，如差分曼切斯特编码
+ 介质访问控制层：介质访问控制，差错校验
+ 逻辑链路控制层：复用与分用

相应帧结构：

![image-20191211111659782](fig\re5-6)

介质访问控制方法：CSMA/CD

![image-20191211112618045](fig\re5-7)

其具体算法可以实现如下：

```
sense channel, f if idle
	then {
		transmit and monitor the channel;
		If detect another transmission
			then {
                abort and send jam signal;
                update # collisions;
                delay as required by binary exponential backoff algorithm;
                goto A A
                }
			else {done with the frame; set collisions to zero}
	}
		else {wait until ongoing transmission is over and goto A}
```

![image-20191211113105804](fig\re5-8.png)

而对于以太帧的接受而言，其应该为：

![image-20191211113210965](fig\re5-9.png)

### 交换式以太网



### 虚拟局域网

### 无线局域网

