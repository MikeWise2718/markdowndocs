---
title: "Isaac Sim"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Nvidia Robotics / Simulation Suite
- Note it properly has double a, not a double s

# Issac Sim Tutorials
- https://docs.omniverse.nvidia.com/isaacsim/latest/introductory_tutorials/index.html

# Ubuntu
https://docs.omniverse.nvidia.com/launcher/latest/it-managed-launcher/install_guide_linux.html

# Code locations
- Isaac Sim Extensions (all of them): `C:\Users\mike\AppData\Local\ov\pkg\isaac_sim-2023.1.1\exts>`
- Isaac Sim Core: `cd \Users\mike\AppData\Local\ov\pkg\isaac_sim-2023.1.1\exts\omni.isaac.core\omni\isaac\core\`
- Isaac Sim Motion Generation: `cd \Users\mike\AppData\Local\ov\pkg\isaac_sim-2023.1.1\exts\omni.isaac.motion_generation\omni\isaac\motion_generation\`
- Isaac Sim Examples (from the menu): `cd \Users\mike\AppData\Local\ov\pkg\isaac_sim-2023.1.1\exts\omni.isaac.examples\omni\isaac\examples\`
- Isaac Sim franka: `cd \Users\mike\AppData\Local\ov\pkg\isaac_sim-2023.1.1\exts\omni.isaac.franka\omni\isaac\franka\`
- Isaac Sim ur10: `cd \Users\mike\AppData\Local\ov\pkg\isaac_sim-2023.1.1\exts\omni.isaac.universal_robotics\omni\isaac\universal_robotics\`
- Search all those: `findstr /a:e /i /s palletizing *.py`
- Better search: `grep -i -r "Isaac Examples" . --include=*.py --color=always`
- Palette example: `omni.isaac.examples\omni\isaac\examples\ur10_palletizing\ur10_palletizing_extension.py`
- Isaac Sim Template (for testing?): `/omni.isaac.ui_template/omni/isaac/ui_template/extension.py`

# Initializtion Complexity
- ALl the Isaac Sim example use the Isaac class world, code can be found in Isaac Sim Core


# Building a Robot from scratch
- An old video, but comprehensive ()


# Articulations
- https://docs.omniverse.nvidia.com/py/isaacsim/source/extensions/omni.isaac.core/docs/index.html


# Cortex
- Most of the cool examples use cortex.


# UR10 Palletizing
- One of the coolest demos
- Code for this is scattered:
   -====


# Surface Grippers
- Finally got things working with the Jaka Surface Gripper
- They require an a prim where the end effector is with a rigid body.
   - It is not necessarily part of the articulation.
   - An offset can be specified for the actual contact point.
   - There are a couple ways to specify the offset depending on what level you

# Physics Tutorial Notes
- How to turn on the Physics Toolbar? (Tools/Physics Autoring) or (Window/Simulation/Physics Authoring Toolbar)
- How to make automatic static mesh creation? (gear)
- How to get the Simulation Settings diaglog box? (I don't now)
- How to group objects? (Create an XForm and create them under it)
- How to make a group of objects selectable as one object? (chnge kind to "Component" or anything else)
- How to toggle that selection mode (use the All Model Kinds icon (top left ))

# Venv on windows 11 for Python 3.10
- Had Python 3.13 installed on Windows 11
- Created the directory for the home of the vevn (d:\ov\isaac_lerobot)
- `cd \ov\isaac_lerobot`
- `pip install virtualenv`
- `pip install virtualenvwrapper-win`
- `python -m virtualenv venv --python=3.10`
- `venv\activate`
- Prompt changed to `(venv) D:\ov\isaac_lerobot>`
- started python and it was indeed python 3.10.11


# Isaac Lab 2.0
- Needs Isaac Sim 4.5
- Link to installation docs: (https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html)
- Creation of virtual env is wrong instead of:
   - You need this beforehand: `sudo apt install python3.10-venv`
   - `python3.10 -m venv env_isaaclab`
   - `source env_isaaclab/bin/activate`
   - Check CUDA version: `nvcc --version` - I had version 11.5
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0
```
   - Install Cuda with correct version
   - Here CUDA 11 or 12, the minor version does not seem to matter)
       - `pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cu118`
       - `pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cu121`
       - takes like 5 min
       - You could test with
          - `python`
          - `>>> import torch`
          - `>>> torch.cuda.is_available()`
          - `True`
          - Note that I needed to do a `pip install numpy` to get this to work
          - you might want to skip this because installing isaac sim coming next will want a particular version of numpy
   - Upgrade pip
       - `pip install --upgrade pip`
   - Install isaac sim
      - `pip install isaacsim[all,extscache]==4.5.0 --extra-index-url https://pypi.nvidia.com`
      - It should run now with `isaacsim` - but takes about 10 minutes the first time as it is "pulling" additional extensions