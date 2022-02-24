---
title: "Gazebo"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Don't try and compile it under windows like the docs indicate you should do. It is a catasrophy
- Works well with WSLg, but you need Windows 11

# Installation
- ROS1 installations correspond to versions of Ubuntu
    - Noetic is Focal (WSLg)
    - Melodic is Bionic (WSLg)

# Get a turtlebot3 up and running in gazebo
- Installed Noetic and Catkin via the ROS setup instructions on the ROS site
- Setup script to initialize ROS
    - `. ~/bin/ros`ws
    - DON'T FORGET THE PERIOD IN THE ABOVE COMMAND!!!!
- Check if loaded: `env | grep ROS`
- list all the turtlebot packages for noetic `apt-cache search ros-noetic | grep turtle`
- Installed a bunch of them:
    - turtlebot3_bringup
    - turtlebot3_description
    - turtlebot3_example
    - turtlebot3_fake
    - turtlebot3_gazebo
    - turtlebot3_msgs
    - turtlebot3_navigation 
    - turtlebot3_slam
    - turtlebot3_teleop
- `export TURTLEBOT3_MODEL=burger`
- `roslaunch turtlebot3_gazebo turtlebot3_world.launch`
    - Gazebo opens up with Turtlebot3 world
- To control it - make a new WSL window, activates scipt with export variable
    - `roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`


# KHI
- Installed Noetic
-  `cd /opt/ros/noetic/share`
-  `git clone https://github.com/Kawasaki-Robotics/khi_robot.git`
-  (doesn't work?) `roslaunch khi_rs_gazebo/launch/rs007n_world.launch simulation:=true`
-  `roslaunch khi_rs_gazebo rs007n_world.launch simulation:=true`

- Packages 
   - https://gist.github.com/rebeccali/a1d93128c892e677f3a2f40c8e6f38d9  
   - catkin_make
   - https://github.com/ros-planning/moveit
   - https://github.com/ros/eigen_stl_containers.git
   - https://github.com/ros-planning/geometric_shapes.git
   - https://github.com/ros-planning/moveit_msgs
   - https://github.com/wg-perception/object_recognition_msgs
   - https://github.com/OctoMap/octomap_msgs
   - https://github.com/ros-planning/srdfdom.git
   - https://github.com/ipab-slmc/pybind11_catkin.git
   - https://stackoverflow.com/questions/46961942/pybind11-linux-building-tests-failure-could-not-find-package-configuration-fi
   - https://github.com/ros-planning/panda_moveit_config.git
   - https://github.com/ros-planning/moveit_resources.git
   - https://github.com/ethz-asl/ompl_catkin
   - https://github.com/catkin/catkin_simple.git
   - sudo apt-get install ros-noetic-ompl
   - sudo apt-get install python3.8 python3.8-dev python3.8-distutils python3.8-venv
   - sudo apt-get install ros-noetic-eigenpy
   - sudo apt-get install ros-noetic-rosparam

# Write some services

- `catkin_ws` was there, but the catkin command was not found
    - To get catkin working: `sudo apt install python3-catkin-tools python3-osrf-pycommon`

# Commands
- `roslaunch khi_robot_bringup rs007n_bringup.launch simulation:=true`
- `roslaunch khi_rs007n_moveit_config moveit_planning_execution.launch`

# Compiling
- ign-cmake
    - had to use `.\configure Release`
-  ign-common
    - Had to comment out the two `%win_lib%` calls in `configure.bat` at the begining
    - Had to add `set ignition-math4_DIR=d:\gz-ws\ign-math\build\` to get it to find the math4 cmake
    - Had to add `set dlfcn-win32_DIR=D:\gz-ws\dlfcn-win32-vc15-x64-dll-MD\share\dlfcn-win32' to get it to find the dlfcn-win32 cmake
- After about 3 hours of getting nowhere I gave up
