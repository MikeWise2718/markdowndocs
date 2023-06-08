---
title: "Hyper-V"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Stable-Diffusion


https://www.dexerto.com/tech/how-to-install-stable-diffusion-2124809/

# Hyper-V GPU

GitHub - jamesstringerparsec/Easy-GPU-PV: A Project dedicated to making GPU Partitioning on Windows easier!

https://www.tenforums.com/virtualization/195745-tutorial-passing-through-gpu-hyper-v-guest-vm.html


```
git clone 

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\Update-VMGpuPartitionDriver.ps1 -VMName "Prawnip" -GPUName "AUTO"
```

Note: Had to disable checkpoints on the VM otherwise it wouldn't start. Right click on the VM and look for the Checkpoints options.