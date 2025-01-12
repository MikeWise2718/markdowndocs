---
title: "Azure Ubuntu"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- This is about creating an Ubuntu on Azure
- Particularly one with a GPU running OV


# Creation
- Go to Create Resource and Create a VM
- Using Ubuntu Server 22.04 LTS -x64 Gen 2
- Been using: (Standard_N36ads_)A10_v5 - 36 vcpus, 440 GiB Memory (price unavailable)
- Price on right is 3036.80 per month, or about 5 dollars an hour
- Go through all the tabs !!!
   - think about the name - you can't change it later
   - it is case insensitive so use lower case
   - disable secure boot
   - Need bigger disk than 30 GB (using 256 at 41 per month) as this is hard to change
   - Make sure you put it in the right VNET (you can't change that either)
   - Download the key and copy it to c:/users/mwise/.ssh


   - now start wsl and copy it to ~/.ssh
      - `cp /mnt/c/Users/mwise/.ssh/vmname_key.pem ~/.ssh`
   - change the read settings because otherwise ssh will complain
      - `chmod 400 vmname_key.pem`
   - might want to add a login command to ~/bin
      - `ssh -i ~/.ssh/vmname_key.pem azureuser@10.0.0.5`
   - Have to do this to calm down mim attack warning
      - `ssh-keygen -f "/home/mike/.ssh/known_hosts" -R "10.0.0.5"`

# Start it and login from your wsl (preferably)
   - You might need to set up the Azure VPN first
   - If you can't login look at the firewall rules under `Settings` / `Networking` in left menu
   - See if there are any `deny` for `port 22`


# Install XRDP
- To get RDP working: (https://learn.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop?tabs=azure-cli)
- The Nvidia driver install script below must be run after XRDP
- If XRDP gets upgraded, you might need to reinstall the nvidia drivers
```
# Install xfce using apt (takes awhile - maybe 5-10 minutes)
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install xfce4
sudo apt install xfce4-session

# Install and configure a remote desktop server
sudo apt-get -y install xrdp
sudo systemctl enable xrdp

# Tell xrdp what desktop environment to use
echo xfce4-session >~/.xsession

# Restart the xrdp service
sudo systemctl restart xrdp

# Set a login password
# (usually configured to use only ssh certificate login at initialization, but that doesn't work with xrdp)
sudo passwd azureuser

# Now you can RDP into the machine (use the ip directly) and azureuser/passwd
# You can open a terminal with right-click
# There are app icons at the bottom
# If there is no browswer installed do the following
sudo apt install firefox
```

# Install Edge (needed for Intune)
- download deb file from: https://www.microsoft.com/en-us/edge/?cs=3457492030&form=MA13FJ
- cd ~/Downloads
- to start: `/opt/microsoft/msedge/msedge https://google.com`
- or right click and look under "Applications" and then "Internet"
- Clean it up by turning off the feed and quick links
   -  Look for the gear icon (page settin) it is on the actual web page in the upper right
   -  Click on it
   -  Change the region to English United States
   -  Change the content feed to "None"
   -  Change the "Quick Links" to "None"
- You can find it in the m

# Install Nvidia device drivers
- Can look for Nvidia Extension (see screenshot)
- Script that we got from Yuval Mazor that works:
- Should be installed after XRDP (and after XRDP gets upgraded)
```
#!/bin/bash
sudo apt update
sudo apt install -y build-essential
GRID_DRIVER_URL="https://download.microsoft.com/download/8/d/a/8da4fb8e-3a9b-4e6a-bc9a-72ff64d7a13c/NVIDIA-Linux-x86_64-535.161.08-grid-azure.run"
GRID_DRIVER_FILE="NVIDIA-Linux-x86_64-535.161.08-grid-azure.run"
wget $GRID_DRIVER_URL -O $GRID_DRIVER_FILE
sudo chmod +x $GRID_DRIVER_FILE
sudo sh $GRID_DRIVER_FILE
CUDA_TOOLKIT_URL="https://developer.download.nvidia.com/compute/cuda/12.0.0/local_installers/cuda_12.0.0_525.60.13_linux.run"
CUDA_TOOLKIT_FILE="cuda_12.0.0_525.60.13_linux.run"
wget $CUDA_TOOLKIT_URL -O $CUDA_TOOLKIT_FILE
sudo sh $CUDA_TOOLKIT_FILE --silent --toolkit --override
# Set environment variables
echo 'export PATH=$PATH:/usr/local/cuda-12.0/bin' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.0/lib64' >> ~/.bashrc
# Source the updated bashrc to apply changes
source ~/.bashrc
# Verify installations
nvidia-smi
nvcc -V
echo "Installation complete. Please reboot and verify that the GRID driver and CUDA toolkit have been installed successfully."
sudo apt-get remove --purge $(dpkg --get-selections | grep -i nvidia | cut -f1)
sudo apt-get remove --purge $(dpkg --get-selections | grep -i cuda | cut -f1)
sed -i PATH="$PATH:/usr/local/cuda-12.0/bin" >
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.0/lib64' >> ~/.bashrc
sudo reboot
```


# the following didn't work
- https://learn.microsoft.com/en-us/azure/virtual-machines/linux/n-series-driver-setup
- `sudo apt update`
- `sudo apt upgrade`
- `sudo apt update && sudo apt install -y ubuntu-drivers-common`
- `sudo ubuntu-drivers install`
- `sudo reboot`
- `ping 10.0.0.5`



# Install intune-portal
- You will need this if you need to grab a Microsoft 2FA auth repo
- https://learn.microsoft.com/en-us/mem/intune/user-help/microsoft-intune-app-linux

````
sudo apt install curl gpg

# Ubuntu 22.04 only
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/ubuntu/22.04/prod jammy main" > /etc/apt/sources.list.d/microsoft-ubuntu-jammy-prod.list'

sudo apt update
sudo apt install intune-portal
intune-portal
```
- if it gets confused try rebooting (`sudo reboot`)
- do not `sudo apt upgrade` after adding the gpg signature - this might break things
- if it works you will see the device under `https://myaccount.microsoft.com/device-list`


# Install Edge

# Something Else
