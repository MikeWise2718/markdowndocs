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
- Seems most everything important lands in `C:\ProgramData\NVIDIA Corporation\CUDA Samples\v9.0` by default
- While the documentation claims that sample binaries and utilities are installed, this is not true, you have to compile everything on your machine first.
- This is also required to do any compilation yourself, perhaps it first compiles some needed utilities first.




# C++
Upgrading to the latest Visual Studio (2017) was a bit of a pain. The command line bat file is hidden under:
    `C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\Common7\Tools\vsDevCmd.bat`

One you run that the environment is setup so you can run the C++ compiler:  cl.exe
```
    C:\Users\mike\source>cl
    Microsoft (R) C/C++ Optimizing Compiler Version 19.11.25547 for x86
    Copyright (C) Microsoft Corporation.  All rights reserved.

    usage: cl [ option... ] filename... [ /link linkoption... ]

And so on...
```

# Downgrading on Ubuntu 18
Got it from here: (https://dmitry.ai/t/topic/33)

```
apt-get --purge remove "*cublas*" "cuda*"
reboot
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
apt install cuda-10-0
reboot
```

# CUDA 8 on Ubuntu 18
- Only got cuda to work after installing the drivers in the GUI, and then reinstalling them with the Nvidia run file
- There is a script to copy the samples to your local directory in `/usr/local/cuda-8-0/bin`
  - Example usage: `mike@Abra:/usr/local/cuda-8.0/bin$ ./cuda-install-samples-8.0.sh /home/mike`
- It didn't really get my installed driver (384.130) as compile failures and the following command show:
- This is how I found things: `find . -path '*.mk' -type f -exec grep -i 'UBUNTU_PKG_NAME =' {} +`
```
mike@Abra:~/NVIDIA_CUDA-8.0_Samples$ find . -path '*.mk' -type f -exec grep -i 'UBUNTU_PKG_NAME =' {} +
./7_CUDALibraries/randomFog/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./6_Advanced/FunctionPointers/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./common/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/volumeFiltering/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
......
......
./5_Simulations/nbody/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./5_Simulations/fluidsGLES/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./5_Simulations/smokeParticles/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./5_Simulations/nbody_opengles/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./5_Simulations/oceanFFT/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./5_Simulations/fluidsGL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./5_Simulations/particles/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
```
- This is how you replace it
   - `find . -path '*.mk' -type f -exec sed -i 's/nvidia-367/nvidia-384/g' {} \;`
```
mike@Abra:~/NVIDIA_CUDA-8.0_Samples$ find . -path '*.mk' -type f -exec sed -i 's/nvidia-367/nvidia-384/g' {} \;
mike@Abra:~/NVIDIA_CUDA-8.0_Samples$ find . -path '*.mk' -type f -exec grep -i 'UBUNTU_PKG_NAME =' {} +
./7_CUDALibraries/randomFog/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./6_Advanced/FunctionPointers/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./common/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./2_Graphics/volumeFiltering/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./2_Graphics/volumeRender/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
......
......
./5_Simulations/nbody/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/fluidsGLES/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/smokeParticles/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/nbody_opengles/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/oceanFFT/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/fluidsGL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/particles/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"

```


# Linux 22.04
- Installing CUDA 11.8
- No longer has integrated samples had to get from seperate repo
  - installed into a local dir `~/ov/cuda-samples`
  - `git clone https://github.com/NVIDIA/cuda-samples.git`
  - `make`
  - Compiled seeminly okay - binary in `/ov/cuda-samples/bin/x86_64/linux/release`
- However there were no visuals (was looking for oceanFFT) - turnes out meas was not installed
  -`install libglu1-mesa libxi-dev libxmu-dev libglu1-mesa-dev`
- ALso had to install glut
  - `sudo apt-get install freeglut3 freeglut3-dev`
- Redid `make` and everything was there
- Still had some errors

```

```