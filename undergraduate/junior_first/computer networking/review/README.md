[TOC]

# 计算机网络

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