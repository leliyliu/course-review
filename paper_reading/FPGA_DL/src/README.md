# 论文学习

---

## review

### [An Overview of FPGA Based Deep Learning Accelerators: Challenges and Opportunities](08855594.pdf)

### [FPGA-Based Accelerators of Deep Learning Networks for Learning and Classification: A Review](FPGA-Based Accelerators of Deep Learning.pdf)

### [Deep Learning on FPGAs: Past, Present, and Future](Lacey, Taylor, Areibi - 2016 - Deep Learning on FPGAs Past, Present, and Future.pdf)



## implementation

### [Automatic Generation of Multi-precision Multi-arithmetic CNN Accelerators for FPGAs](1910.10075.pdf)

19年的新成果，The generated design is pipelined and each convolution layer uses different arithmetics at various precisions. 提出tomato架构，对于每一层使用不同的精度和不用的计算模式进行相应的计算。可以在FPGA上实现基于算法的对于每层网络计算的灵活调整。the first multi-precision multi-arithmetic autogeneration framework for CNNs.同时还可以使用multi-FPGA计算。

### [LUTNet: Learning FPGA Configurations for Highly Efficient Neural Network Inference](1910.12625.pdf)

利用FPGA中的LUT实现的binary 的network ，大量减少了计算量，使用逻辑计算的方式来实现数值计算。

### [Lowering Dynamic Power of a Stream-based CNN Hardware Accelerator](2019L-Duvindu-MMSP.pdf)

lower the dynamic power of a stream-based CNN hardware accelerator by reducing the computational redundancies in the CNN layers 这里主要是使用了一种流式的方式来减少FPGA中的功耗。

### [An FPGA-Based Hardware Accelerator for CNNs Using On-ChipMemories Only: Design and Benchmarking with Intel Movidius
Neural Compute Stick](7218758.pdf)



### [Design and Implementation of a Low-power, Embedded CNN Accelerator on a Low-end FPGA](08875030.pdf)

### [T-DLA: An Open-source Deep Learning Accelerator for Ternarized DNN Models on Embedded FPGA](Chen et al. - 2019 - T-DLA An Open-source Deep Learning Accelerator for Ternarized DNN Models on Embedded FPGA.pdf)

### [A Deep Learning Inference Accelerator Based on Model Compression on FPGA](Jing, Liu, Yu - 2019 - A Deep Learning Inference Accelerator Based on Model Compression on FPGA.pdf)

### [DLAU: A Scalable Deep Learning Accelerator Unit on FPGA](Wang et al. - 2017 - DLAU A scalable deep learning accelerator unit on FPGA.pdf)

### [Optimizing FPGA-based Accelerator Design for Deep Convolutional Neural Networks](Zhang - 2015 - Optimizing FPGA-based Accelerator Design for Deep.pdf)

### [Squeezing the last MHz for CNN acceleration on FPGAs](08871619.pdf)



## compression

### [MetaQuant: Learning to Quantize by Learning to Penetrate Non-differentiable Quantization](8647-metaquant-learning-to-quantize-by-learning-to-penetrate-non-differentiable-quantization.pdf)

a faster convergence rate and better performance。 一个压缩的方法，能够更快的收敛，用更少的迭代次数。

### [Optimizing Weight Value Quantization for CNN Inference](08852331.pdf)

### [Deep Learning with Limited Numerical Precision](Gupta et al. - 2015 - Deep learning with limited numerical precision.pdf)

### [YOLO Nano: a Highly Compact You Only Look Once Convolutional Neural Network for Object Detection](mini_yolo.pdf)



## related work

### [Accelerating HotSpots in Deep Neural Networks on a CAPI-based FPGA](08855410.pdf)

### [High-performance Convolutional Neural Network Accelerator Based on Systolic Arrays and Quantization](08868327.pdf)

### [Fast Convolutional Neural Networks in Low Density FPGAs Using Zero-Skipping and Weight Pruning](electronics-08-01321-v2.pdf)

### [Optimality Assessment of Memory-Bounded ConvNets Deployed on Resource-Constrained RISC Cores](08877713.pdf)

