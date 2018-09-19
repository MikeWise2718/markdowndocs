---
title: "Tensorflow On Azure"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Lessons learned on Tensorflow on Azure


# Non-GPU Azure
Steps:
* Allocated D2 16 GB Mem, 30 GB SSD Premium OS Disk, 1 TB SSD extra disk, all inbound ports open
* In Azure portal configured a dynamic dns name
* Added entry in putty and set default background color (purple)
* cloned ububin into home directory and renamed
* edited `~/.bashrc` and uncommented `force_color_prompt=yes` on line 46
* did an `echo $PATH` to make sure `/home/mike/bin` was in path
* Installed xrdp
    ** Instructions <https://websiteforstudents.com/connect-to-ubuntu-16-04-17-10-18-04-desktop-via-remote-desktop-connection-rdp-with-xrdp/>
    ** `sudo apt install xrdp`
    ** `sudo systemctl enable xrdp` 
* Then this:<https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop>
    ** `suto apt-get install xfce4`
    ** reboot the server
    ** `echo xfce4-session >~/.xsession`
    ** RDP in using the DNS address and your user
