---
title: "LeRobot"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- LeRobot is a set of Hugging Face assets for doing robotics
- github repo
- LeRobot Home Page: (https://huggingface.co/lerobot)
- LeRobot Visualizer: ()

# Datasets are cached in
- Windows - c:\Users\name\.cache\huggingface
- Linux - ~/.cache/huggingface


# Installation of lerobot
- Follow script
- Make sure to test pytorch afterwards
  - python
  - import torch
  - torch.cuda.is_available()
- pytorch must be compiled with the right CUDA verson
- for example to install torch 2.6.0 with CUDA 12.5 use
    `pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cu124`

# YouTube Tutorial
- How to use LeRobot with Isaac Sim - https://www.youtube.com/watch?v=eO5wMzw9LeQ&t=246s
- Has some good utilities/data at (https://drive.google.com/drive/folders/1eyh1GzMGnrjCnwW0_CWqEyVtDDd-0Sfe)



## Setup
- Install ROS2 Humble - 0:40
- Setup Isaac Sim (includes a Python 3.10 venv) - 0:58
- He doesn't check if pytorch runs with CUDA at the end, but you should do that
- Install typeguard - 1:36
- Setup LeRobot - 1:40
- Install aloha and pushT - 2:11
- LeRobot how to train your own policy - 2:47
- Download modified files from Dropbox

## Create USD File with Isaac Sim
- Create Scene
- Import Robot
- Add articulation and adjust parameters
- Add Table
- Add Action Graph - 9:38
- Add "On Playback Tick" node
- Add "ROS2 Context" node - 9:48
- Add "ROS2 Subscribe Joint State" node - 9:52
- Add "Articulation Control" node"
- Add Top Camera (under world - overhead watching the table) 10:36
- Add Wrist Camera (under wrist 3_link - watching end effector) 12:28
- Add TF Publisher Graph - 12:44
- Add Physics material to TBar and EETool - 13:22
- Isaac Sim model finished - 14:15

## ROS2
- ROS2 start - 14:15
- data_collection.py - 14:20
- ready to collect the data - 17:01
- colcon start - 17:06
- isaac sim start - 17:14
- launch robot-arm joystick controller python script - 17:27
- launch ros2 ur5_moveit_config arm_joy_control.launch.py - 17:38
- rviz visible - 17:40

## Data collection
- run python3 data_collection.py - 17:46
- operate the tool and move the TBar - 18:12
- note index and episode_index - 18:13
- add index and episode_index to data_collection script - 18:29
- after data collection create a dir with the lerobot structure and copy data to it - 18:43
- execute create episodes jsonl python script (and stats)  - 19:22
-   python3 create episodes_jsonl.py
-   python3 create episodes_stats_jsonl.py
- move generated files to meta directory - 19:48


- already generated files location for lazy people for training - 20:07
- to run the training move these two scripts into the LeRobot examples -20:24
- to execute training execute 3_train_policy_mod.py - 20:44
- trained model storage location - 21:02
- evaluate policy script - 21:10
- to execute launch the arm diffusion control launch python script - 21:28
   - ros2 launch ur5_moveit_config arm_diffusion_control.launch.py
   - rviz comes up
- execute 2_evaluate_pretrained_policy_ROS.py - 21:36
   - python3 2_evaluate_pretrained_policy_ROS.py
finished - 21:55