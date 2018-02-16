---
title: "Nvidia Jetson Embedded Board"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- The Nvidia Jetson TX2 is an embeded ARM device for High Performance Computing on the IoT edge. 
- It runs Linux 4 Tegra (L4T) which is an Ubuntu derived Linux distirubtion running on ARM.
- The actualy module is quite small, but the Dev Kit contains a carrier board which is a little ITX form factor main board that hosts it.
* You can pretty much only manage it with another Ubunut computer.
* I suppose you could get it to work from a VM - but since Hyper-V doesn't play that well with USB devices, it might be a challenge.
* A lot of information carries over from the Jetson TX1 which had the same carrier board.
* It only runs with Docker as of Jetpack 28.2 released for preview in Dec 2017
* Useful Docs:
  * Uboxing the TX2 is [here](https://www.youtube.com/watch?v=kl2rMlHde4k)
  * Putting Jetson in [forced recovery mode](https://www.youtube.com/watch?v=4JUWS9i_FCQ)
  * Installing Docker is [here](https://github.com/Technica-Corporation/Tegra-Docker)

# Installation
* Docs (not that up-to-date) are [here](http://docs.nvidia.com/jetpack-l4t/2_1/content/developertools/mobile/jetpack/jetpack_l4t/2.0/jetpack_l4t_install.htm)
* They assume you are doing this from another Ubunut computer called the "host", the Jetson is called the "target"
* Apparently it comes with the operating system installed, but I never saw it, somehow I only got my HDMI monitor to display it after I had flashed it once.
* You download a Jetpack, this has three parts
  * An installation of various things on the Ubuntu Host computer
  * The machine gets flashed with the new version of L4T which goes over a USB/Micro-USB cable.
  * Post installation steps install things like CUDA, etc after that which require that the machines talk over IP.
* To redo an installation you need to nuke a hidden install directory that is owned by a "dip" user.
* It can be difficult to figure out what ethernet interfaces are what, the two shorter ones turned out to run over the USB cable, the longer one turned out to be running from my usb/ethernet adapter, and the one starting with "w" was the wifi.
* Details about what the post-installation does can only be obtained by inspecting the code in that directory.
* To understand the installation steps
* It seems that there is no documented way to put CUDA on this thing without installing a jetpack, this seems wierd.
