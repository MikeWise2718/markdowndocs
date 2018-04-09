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
