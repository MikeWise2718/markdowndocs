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