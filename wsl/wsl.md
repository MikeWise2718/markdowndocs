---
title: "WSL"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Windows Subsystem for Linux
Note that to get a preview of this document in VS Code use Ctrl-Shift-V
- A useful guide - (https://www.sitepoint.com/wsl2/)

- DON'T INSTALL CUDA on WSL - see this for how to do it right:
   - `https://docs.nvidia.com/cuda/wsl-user-guide/index.html`
# Commands
- `wsl --list`
```
C:\Users\mwise>wsl --list
Windows Subsystem for Linux Distributions:
docker-desktop-data (Default)
docker-desktop
```
-
- `wsl --unregister <distroName>`  # to delete a distro
   - some places say you should delete it from the `System\Applications` list first
   - this will not remove wsl, to do that you have to go to `Apps&Features` and disable it


- `wsl -l -o` to list available distributions
```
C:\Users\mwise>wsl -l -o
The following is a list of valid distributions that can be installed.
Install using 'wsl.exe --install <Distro>'.

NAME                                   FRIENDLY NAME
Ubuntu                                 Ubuntu
Debian                                 Debian GNU/Linux
kali-linux                             Kali Linux Rolling
Ubuntu-18.04                           Ubuntu 18.04 LTS
Ubuntu-20.04                           Ubuntu 20.04 LTS
Ubuntu-22.04                           Ubuntu 22.04 LTS
Ubuntu-24.04                           Ubuntu 24.04 LTS
OracleLinux_7_9                        Oracle Linux 7.9
OracleLinux_8_7                        Oracle Linux 8.7
OracleLinux_9_1                        Oracle Linux 9.1
openSUSE-Leap-15.5                     openSUSE Leap 15.5
SUSE-Linux-Enterprise-Server-15-SP4    SUSE Linux Enterprise Server 15 SP4
SUSE-Linux-Enterprise-15-SP5           SUSE Linux Enterprise 15 SP5
openSUSE-Tumbleweed                    openSUSE Tumbleweed
```

- `wsl --install -d Ubuntu-22.04` # Install Ubu22  - takes about 3 minutes
```
C:\Users\mwise>wsl --install -d Ubuntu-22.04
Installing: Ubuntu 22.04 LTS
Ubuntu 22.04 LTS has been installed.
Launching Ubuntu 22.04 LTS...
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: mike
New password:
Retype new password:
passwd: password updated successfully
The operation completed successfully.
Installation successful!
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.146.1-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


This message is shown once a day. To disable it please create the
/home/mike/.hushlogin file.
user@host:~$ ls
user@host:~$ ls -ali
total 24
  477 drwxr-x--- 3 mike mike 4096 Jun 17 13:35 .
16386 drwxr-xr-x 3 root root 4096 Jun 17 13:35 ..
29542 -rw-r--r-- 1 mike mike  220 Jun 17 13:35 .bash_logout
 1026 -rw-r--r-- 1 mike mike 3771 Jun 17 13:35 .bashrc
29615 drwx------ 2 mike mike 4096 Jun 17 13:35 .cache
29617 -rw-r--r-- 1 mike mike    0 Jun 17 13:35 .motd_shown
29545 -rw-r--r-- 1 mike mike  807 Jun 17 13:35 .profile
user@host:~$
```
- On 5 Nov 2024 - `wsl --version`
- Had just updated from 2.2.something with `wsl --update`
```
C:\Windows\System32\lxss\tools>wsl --version
WSL version: 2.3.24.0
Kernel version: 5.15.153.1-2
WSLg version: 1.0.65
MSRDC version: 1.2.5620
Direct3D version: 1.611.1-81528511
DXCore version: 10.0.26100.1-240331-1435.ge-release
Windows version: 10.0.26120.751
```

## Inspecting the kernel
- Open File Explorer and enter `\\wsl$\`
- It is not in `C:\Windows\System32\lxss\tools` though googling might get that
- Apparently it is actually in your app director though

## .wslconfig and wsl.conf
- `.wslconfig` is in `c:\user\<username>` - default is no file
- Offical docs: (https://learn.microsoft.com/en-us/windows/wsl/wsl-config)


## Adding Joystick
- Need to add a windows tool to map USB and then rebuild the kernel to load the right modules
- Instructions can be found here: (https://github.com/microsoft/WSL/issues/7747)
- Turns out you can't swap the kernel under MSIT corp Intune policy
```
C:\Users\mwise>wsl
wsl: The .wslconfig setting 'wsl2.kernel' is disabled by the computer policy.
ROS 2 Distro Humble Hawksbill activated on Ubu 22.04
user@host:~$
```

## Building the kernel
- Simple clone the repo, install the tool chain, configure the kernel, and build it
- WSL2 Repo Site:(https://github.com/microsoft/WSL2-Linux-Kernel)
- Helpful Site:(https://microhobby.com.br/blog/2019/09/21/compiling-your-own-linux-kernel-for-windows-wsl2/)
- Took close to an hour to build on WSL2


- DON'T INSTALL CUDA on WSL - see this for how to do it right:
    `https://docs.nvidia.com/cuda/wsl-user-guide/index.html`
