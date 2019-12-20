[TOC]

# 操作系统五十问

---

### 1. 并发和并行的区别？

如果某个系统支持两个或者多个动作（Action）**同时存在**，那么这个系统就是一个**并发系统**。如果某个系统支持两个或者多个动作**同时执行**，那么这个系统就是一个**并行系统**。并发系统与并行系统这两个定义之间的关键差异在于**“存在”**这个词。

在并发程序中可以同时拥有两个或者多个线程。这意味着，如果程序在单核处理器上运行，那么这两个线程将交替地换入或者换出内存。这些线程是同时“存在”的——每个线程都处于执行过程中的某个状态。如果程序能够并行执行，那么就一定是运行在多核处理器上。此时，程序中的每个线程都将分配到一个独立的处理器核上，因此可以同时运行。

能够得出结论——**“并行”概念是“并发”概念的一个子集**。也就是说，你可以编写一个拥有多个线程或者进程的并发程序，但如果没有多核处理器来执行这个程序，那么就不能以并行方式来运行代码。因此，凡是在求解单个问题时涉及多个执行流程的编程模式或者执行行为，都属于并发编程的范畴。

一般我们意义上的并发，是指存在多个线程或进程，系统通过调用，让你感受到每个进程（或者说多个线程）在同时执行的，但是实际上并不是，总而言之，并发是一种调度，它使得多个线程能够恰到好处的看似同时但实则有时间顺序地执行。

### 2. 什么是多道程序设计技术？

[多道程序设计](https://baike.baidu.com/item/多道程序设计)技术是指在内存同时放若干道程序，使它们在系统中并发执行，共享系统中的各种资源。当一道程序暂停执行时，CPU立即转去执行另一道程序。

[特点]：多道、宏观上并行（不同的作业分别在CPU和外设上执行）、微观上串行（在单CPU上交叉运行）。

[[多道批处理系统](https://baike.baidu.com/item/多道批处理系统)]：将[多道程序设计](https://baike.baidu.com/item/多道程序设计)技术应用于批处理系统，就形成多道批处理系统。

[多道程序设计](https://baike.baidu.com/item/多道程序设计)技术 对 操作系统的形成起到的作用：

操作系统在引入[多道程序设计](https://baike.baidu.com/item/多道程序设计)技术后，使得系统具有了多道，宏观上并行，微观上串行的特点。

[多道程序设计](https://baike.baidu.com/item/多道程序设计)主要是使OS能更好地对计算机进行管理 。

使计算机的硬件资源得到更充分的利用 。

在OS中引入[多道程序设计](https://baike.baidu.com/item/多道程序设计)技术带来的好处：

1. 提高CPU的利用率

2. 提高内存和I/O设备利用率

3. 增加系统[吞吐量](https://baike.baidu.com/item/吞吐量)

多道程序设计必须有[硬件基础](https://baike.baidu.com/item/硬件基础)作为保证，即内存。

所谓多道程序设计指的是允许多个程序同时进入一个计算机系统的[主存储器](https://baike.baidu.com/item/主存储器)并启动进行计算的方法。也就是说，计算机内存中可以同时存放多道（两个以上相互独立的）程序，它们都处于开始和结束之间。从宏观上看是并行的，[多道程序](https://baike.baidu.com/item/多道程序/8192392)都处于运行中，并且都没有运行结束；从微观上看是串行的，各道程序轮流使用CPU，交替执行。引入[多道程序设计技术](https://baike.baidu.com/item/多道程序设计技术)的根本目的是为了提高CPU的利用率，充分发挥计算机系统部件的[并行性](https://baike.baidu.com/item/并行性)，现代计算机系统都采用了多道程序设计技术。

实际上，这种多道程序设计的基础在很大程度上是虚拟内存的出现以及内存自身的扩大，只有在这种情况下，内存才能使得多个程序能够较好的运行在内存之中。

3.操作系统中内核与shell的关系

#### 操作系统

**操作系统**（英语： **O**perating **S**ystem，缩写： **OS**）是管理[电脑](https://zh.wikipedia.org/wiki/计算机)[硬体](https://zh.wikipedia.org/wiki/硬件)与[软体](https://zh.wikipedia.org/wiki/软件)资源的[系统软体](https://zh.wikipedia.org/wiki/系统软件)，同时也是电脑系统的核心与基石。操作系统需要处理如管理与组态[记忆体](https://zh.wikipedia.org/wiki/内存)、决定系统资源供需的优先次序、控制输入与输出装置、操作[网路](https://zh.wikipedia.org/wiki/计算机网络)与管理[档案系统](https://zh.wikipedia.org/wiki/文件系统)等基本事务。操作系统也提供一个让使用者与系统互动的操作介面。

操作系统的型态非常多样，不同机器安装的操作系统可从简单到复杂，可从[移动电话](https://zh.wikipedia.org/wiki/移动电话)的[嵌入式系统](https://zh.wikipedia.org/wiki/嵌入式系统)到[超级电脑](https://zh.wikipedia.org/wiki/超级计算机)的[大型操作系统](https://zh.wikipedia.org/wiki/超级计算机#.E6.93.8D.E4.BD.9C.E7.B3.BB.E7.BB.9F)。许多操作系统制造者对它涵盖范畴的定义也不尽一致，例如有些操作系统整合了[图形化使用者界面](https://zh.wikipedia.org/wiki/图形用户界面)，而有些仅使用[命令行界面](https://zh.wikipedia.org/wiki/命令行界面)，而将图形化使用者介面视为一种非必要的应用程式。

其主要功能有：进程管理，内存管理，文件系统，网络，安全，使用者界面和驱动程序等。

#### 内核

**核心**（英语：**Kernel**，又称**内核**）在[计算机科学](https://zh.wikipedia.org/wiki/計算機科學)中是一个用来管理[软体](https://zh.wikipedia.org/wiki/軟體)发出的资料[I/O](https://zh.wikipedia.org/wiki/I/O)（输入与输出）要求的电脑[程式](https://zh.wikipedia.org/wiki/程式)，将这些要求转译为资料处理的指令并交由[中央处理器](https://zh.wikipedia.org/wiki/中央處理器)（CPU）及[电脑](https://zh.wikipedia.org/wiki/電腦)中其他[电子元件](https://zh.wikipedia.org/wiki/電子元件)进行处理，是现代[作业系统](https://zh.wikipedia.org/wiki/操作系统)中最基本的部分。它是为众多[应用程式](https://zh.wikipedia.org/wiki/应用程序)提供对[电脑](https://zh.wikipedia.org/wiki/计算机)[硬体](https://zh.wikipedia.org/wiki/硬件)的安全存取的一部分[软体](https://zh.wikipedia.org/wiki/软件)，这种存取是有限的，并由核心决定一个[程式](https://zh.wikipedia.org/wiki/程序)在什么时候对某部分硬体操作多长时间。直接对硬体操作是非常复杂的。所以核心通常提供一种[硬体抽象](https://zh.wikipedia.org/wiki/硬件抽象)的方法，来完成这些操作。有了这个，通过[进程间通信](https://zh.wikipedia.org/wiki/进程间通信)机制及[系统调用](https://zh.wikipedia.org/wiki/系统调用)，应用行程可间接控制所需的硬体资源（特别是处理器及IO装置）。

##### 单核心

单核心结构在硬体之上，定义了一个高阶的抽象介面，应用一组[原语](https://zh.wikipedia.org/w/index.php?title=原语&action=edit&redlink=1)（或者叫[系统呼叫](https://zh.wikipedia.org/wiki/系统调用)（System call））来实现作业系统的功能，例如[进程管理](https://zh.wikipedia.org/wiki/进程管理)，[文件系统](https://zh.wikipedia.org/wiki/文件系统)，和[内存管理](https://zh.wikipedia.org/w/index.php?title=存储管理&action=edit&redlink=1)等等，这些功能由多个执行在核心态的[模组](https://zh.wikipedia.org/wiki/模块)来完成。

尽管每一个模组都是单独地服务这些操作，核心代码是高度整合的，而且难以编写正确。因为所有的模组都在同一个核心空间上执行，一个很小的bug都会使整个系统崩溃。然而，如果开发顺利，单核心结构就可以从执行效率上得到好处。

很多现代的单核心结构核心，如[Linux](https://zh.wikipedia.org/wiki/Linux内核)和[FreeBSD](https://zh.wikipedia.org/wiki/FreeBSD)核心，能够在执行时将模组调入执行，这就可以使扩充核心的功能变得更简单，也可以使核心的核心部分变得更简洁。

##### 混合核心

混合核心的设计理念来自微核心，只不过它让一些微核结构执行在用户空间的代码执行在核心空间，这样让核心的执行效率更高些。这是一种妥协做法，[微软](https://zh.wikipedia.org/wiki/微软)[视窗](https://zh.wikipedia.org/wiki/Windows)就是一个典型的例子。另外还有XNU，执行在[苹果](https://zh.wikipedia.org/wiki/苹果电脑)[Mac OS X](https://zh.wikipedia.org/wiki/Mac_OS_X)上的核心，也是一个混合核心。[林纳斯·托瓦兹](https://zh.wikipedia.org/wiki/林纳斯·托瓦兹)认为混合核心这种分类只是一种市场行销手法，因为它的架构实作与运作方式接近于宏核心。

#### shell

**壳层**（英语：**Shell**）在[电脑科学](https://zh.wikipedia.org/wiki/電腦科學)中指「为使用者提供使用者介面」的软体，通常指的是[命令列介面](https://zh.wikipedia.org/wiki/命令行界面)的解析器。一般来说，这个词是指[操作系统](https://zh.wikipedia.org/wiki/作業系統)中提供存取[核心](https://zh.wikipedia.org/wiki/内核)所提供之服务的程式。Shell也用于泛指所有为用户提供操作界面的程式，也就是程式和用户[互动](https://zh.wikipedia.org/w/index.php?title=交互&action=edit&redlink=1)的层面。因此与之相对的是[核心](https://zh.wikipedia.org/wiki/内核)（英语：**Kernel**），核心不提供和用户的互动功能。

![shell](fig/re1-1.png)

故而，实际上shell 是对于外层用户的一层封装，一般而言，大多数程序都是通过它来实现对于内核的调用（当然如果自己的程序也进行了内核调用那就并非如此），但是一般而言，可以理解为，shell 是用户开启的进程的父进程，那么所有的系统调用也都是最初来自于shell。

更详尽的理解可以参考我的对于shell的相关实现： [stupid shell](https://github.com/leliyliu/project_implementation/tree/master/shell_in_c)

### 4. 中断，异常和系统调用的区别与联系

系统调用（system call）

应用程序主动向操作系统发出的服务请求

异常(exception)

非法指令或者其他原因导致当前指令执行失败   (如：内存出错)后的处理请求

中断(hardware interrupt)

来自硬件设备的处理请求

![fig](fig/re1-2.png)

    源头
    
    中断：外设引起
    
    异常：应用程序意想不到的行为
    
    系统调用：应用程序请求操作系统提供服务
    
    响应方式
    
    中断：异步
    
    异常：同步
    
    系统调用：异步或同步


​    
​    
​    处理机制
​    
​    中断：持续，对用户应用程序是透明的
​    
    异常：杀死或者重新执行意想不到的应用程序指令
    
    系统调用：等待和持续
    
    接下来我们详细介绍一些中断的处理机制，处理机制包括硬件处理和软件处理
    
    硬件处理
    
    依据内部或者外部事件设置中断标志，然后依据中断向量调用相应的中断服务例程。
    
    软件处理
    
    首先进行现场保存（由编译器完成），然后进行中断服务处理（中断服务例程完成），接着清除中断标记（中断服务例程），最后进行现场恢复（编译器）。

### 5. 函数调用的具体过程

函数调用过程中，需要做这样几件事情：

在x86的计算机系统中，内存空间中的栈主要用于保存函数的参数，返回值，返回地址，本地变量等。一切的函数调用都要将不同的数据、地址压入或者弹出栈。因此，为了更好地理解函数的调用，我们需要先来看看栈是怎么工作的。

#### 栈帧

栈帧，也就是stack frame，其本质就是一种栈，只是这种栈专门用于保存函数调用过程中的各种信息（参数，返回地址，本地变量等）。栈帧有栈顶和栈底之分，其中栈顶的地址最低，栈底的地址最高，SP(栈指针)就是一直指向栈顶的。在x86-32bit中，我们用 `%ebp` 指向栈底，也就是基址指针；用 `%esp` 指向栈顶，也就是栈指针。下面是一个栈帧的示意图：

![栈帧](fig/re1-3.png)

一般来说，我们将 `%ebp` 到 `%esp` 之间区域当做栈帧（也有人认为该从函数参数开始，不过这不影响分析）。并不是整个栈空间只有一个栈帧，每调用一个函数，就会生成一个新的栈帧。在函数调用过程中，我们将调用函数的函数称为“调用者(caller)”，将被调用的函数称为“被调用者(callee)”。在这个过程中，1）“调用者”需要知道在哪里获取“被调用者”返回的值；2）“被调用者”需要知道传入的参数在哪里，3）返回的地址在哪里。同时，我们需要保证在“被调用者”返回后，`%ebp`, `%esp` 等寄存器的值应该和调用前一致。因此，我们需要使用栈来保存这些数据。

#### 函数调用实例

```c
int MyFunction(int x, int y, int z)
{
    int a, b, c;
    a = 10;
    b = 5;
    c = 2;
    ...
}

int TestFunction()
{
    int x = 1, y = 2, z = 3;
    MyFunction1(1, 2, 3);
    ...
}
```

```asm
_MyFunction:
    push %ebp            ; //保存%ebp的值
    movl %esp, $ebp      ; //将%esp的值赋给%ebp，使新的%ebp指向栈顶
    movl -12(%esp), %esp ; //分配额外空间给本地变量
    movl $10, -4(%ebp)   ; 
    movl $5,  -8(%ebp)   ; 
    movl $2,  -12(%ebp)  ; 
```

