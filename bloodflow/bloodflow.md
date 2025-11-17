---
title: "Blood Flow Simulation"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Misc


# SimVascular


## Cmake
- Add Kitware's signing key
   - `wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | sudo tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null`

- Add Kitware's repository for Ubuntu 20.04 (Focal)
   - `sudo apt-add-repository 'deb https://apt.kitware.com/ubuntu/ focal main'`
   - `sudo apt update`

-  Install the latest CMake
   - `sudo apt install cmake`
-  Adjust the path (to get rid of "CMake Error: Could not find CMAKE_ROOT !!!")
   - `export PATH="$HOME/.local/bin:$PATH"`



## WSL Installation
- There are no windows binaries available, so decided to compile a WSL version on Perplexities advice
- ` sudo apt install build-essential cmake git libvtk7-dev libinsighttoolkit4-dev qtbase5-dev qttools5-dev libqt5svg5-dev`
