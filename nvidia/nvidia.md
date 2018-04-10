---
title: "Nvidia Graphics Cards"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Nvidia Graphis cards are ubiquitous now, I have like 3-4 devices running them at home.

# Surface Book
- The Surface Book uses some undocumented Nvidia version
- There are no Ubunutu drivers for the Nvidia Surface Book, perhaps Microsoft wanted that.

# Drivers
- you can find a list of available drivers here: http://www.nvidia.de/Download/Find.aspx
- install instructions: https://askubuntu.com/questions/851069/latest-nvidia-driver-on-ubuntu-16-04
- also these: https://askubuntu.com/questions/149206/how-to-install-nvidia-run

```
Official Instructions

Download the driver version 375.20 from here
1. $ chmod 777 NVIDIA-Linux-x86_64-375.20.run
2. $ sudo sh NVIDIA-Linux-x86_64-375.20.run
3. $ sudo apt-get update
4. $ sudo apt-get upgrade
```
# CUDA on Ubuntu
- Only got cuda to work after installing the drivers in the GUI, and then reinstalling them with the Nvidia run file
- There is a script to copy the samples to your local directory in `/usr/local/cuda-8-0/bin`
  - Example usage: `mike@Abra:/usr/local/cuda-8.0/bin$ ./cuda-install-samples-8.0.sh /home/mike`
- It didn't really get my installed driver (384.130) as compile failures and the following command show:
```
mike@Abra:~/NVIDIA_CUDA-8.0_Samples$ find . -path '*.mk' -type f -exec grep -i 'UBUNTU_PKG_NAME =' {} +
./7_CUDALibraries/randomFog/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./6_Advanced/FunctionPointers/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./common/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/volumeFiltering/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/volumeRender/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/simpleGLES_screen/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/simpleGLES_EGLOutput/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/simpleGLES/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/simpleTexture3D/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/marchingCubes/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/Mandelbrot/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/bindlessTexture/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./2_Graphics/simpleGL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/SobelFilter/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/recursiveGaussian/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/cudaDecodeGL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/boxFilter/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/postProcessGL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/simpleCUDA2GL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/bicubicTexture/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/EGLStreams_CUDA_Interop/findegl.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/imageDenoising/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./3_Imaging/bilateralFilter/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
./5_Simulations/nbody_screen/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-367"
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
./2_Graphics/simpleGLES_screen/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./2_Graphics/simpleGLES_EGLOutput/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./2_Graphics/simpleGLES/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./2_Graphics/simpleTexture3D/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./2_Graphics/marchingCubes/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./2_Graphics/Mandelbrot/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./2_Graphics/bindlessTexture/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./2_Graphics/simpleGL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/SobelFilter/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/recursiveGaussian/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/cudaDecodeGL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/boxFilter/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/postProcessGL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/simpleCUDA2GL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/bicubicTexture/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/EGLStreams_CUDA_Interop/findegl.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/imageDenoising/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./3_Imaging/bilateralFilter/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/nbody_screen/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/nbody/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/fluidsGLES/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/smokeParticles/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/nbody_opengles/findgleslib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/oceanFFT/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/fluidsGL/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"
./5_Simulations/particles/findgllib.mk:    UBUNTU_PKG_NAME = "nvidia-384"

```

# CUDNN
- Have had a lot of intermittent initialization problems with CUDNN
- Typical error message is:
```
2018-04-09 12:49:41.267921: E tensorflow/stream_executor/cuda/cuda_dnn.cc:385] could not create cudnn handle: CUDNN_STATUS_NOT_INITIALIZED
2018-04-09 12:49:41.267974: E tensorflow/stream_executor/cuda/cuda_dnn.cc:393] possibly insufficient driver version: 384.111.0
2018-04-09 12:49:41.267985: E tensorflow/stream_executor/cuda/cuda_dnn.cc:352] could not destroy cudnn handle: CUDNN_STATUS_BAD_PARAM
2018-04-09 12:49:41.267993: F tensorflow/core/kernels/conv_ops.cc:717] Check failed: stream->parent()->GetConvolveAlgorithms( conv_parameters.ShouldIncludeWinogradNonfusedAlgo<T>(), &algorithms)
```
- Here is my `nvidia-smi` output when this is happening:
```
Mon Apr  9 12:47:04 2018
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 384.111                Driver Version: 384.111                   |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 106...  Off  | 00000000:01:00.0 Off |                  N/A |
|  0%   47C    P0    24W / 200W |    222MiB /  6072MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      2023      G   /usr/lib/xorg/Xorg                           149MiB |
|    0      3375      G   compiz                                        70MiB |
+-----------------------------------------------------------------------------+
```
- A reboot sometimes makes it go away, but sometimes not.
- Tried cycling the power, didn't help either.
- Killing the Xorg process did not help either.
- resetting the graphics card did not help (had to stop Xorg first)
   - `sudo service lightdm stop`
   - `sudo nvidia-smi -r`
```
(tf27gpu) mike@Abra:~/tfrepos/models/research/object_detection$ nvidia-smi
Mon Apr  9 13:39:11 2018
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 384.111                Driver Version: 384.111                   |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 106...  Off  | 00000000:01:00.0 Off |                  N/A |
|  0%   47C    P0    25W / 200W |      0MiB /  6072MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
(tf27gpu) mike@Abra:~/tfrepos/models/research/object_detection$ sudo nvidia-smi -r
GPU 00000000:01:00.0 was successfully reset.
```
