---
title: "Cuda"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Cuda is a library from Nvidia that supports massively parallel operations on GPUs.

Here is a good intro [article](https://devblogs.nvidia.com/parallelforall/even-easier-introduction-cuda/)

Note that everything requirecs "nvcc" a compiler driver for what every compiler you are using (in my case VC++)


# Installation
- You need to download and install the cuda tools.
- Seems most everything important lands in C:\ProgramData\NVIDIA Corporation\CUDA Samples\v9.0 by default
- While the documentation claims that sample binaries and utilities are installed, this is not true, you have to compile everything on your machine first.
- This is also required to do any compilation yourself, perhaps it first compiles some needed utilities first.

# C++
Upgrading to the latest Visual Studio (2017) was a bit of a pain. The command line bat file is hidden under:
    C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\Common7\Tools\vsDevCmd.bat

One you run that the environment is setup so you can run the C++ compiler:  cl.exe

    C:\Users\mike\source>cl
    Microsoft (R) C/C++ Optimizing Compiler Version 19.11.25547 for x86
    Copyright (C) Microsoft Corporation.  All rights reserved.

    usage: cl [ option... ] filename... [ /link linkoption... ]


