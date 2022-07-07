---
title: "ROS"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- ROS - Robotics Operating System is not really an OS, it is a "System for operating robots". More like middleware
- Wikipedia: (https://en.wikipedia.org/wiki/Robot_Operating_System)
- ROS home page: (https://www.ros.org/)

# Unity-Robotics-Hub
- Home page: (https://github.com/Unity-Technologies/Unity-Robotics-Hub)
- Pick and Place Tutorial: (https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/pick_and_place/README.md)
- Building image
    - `cd d:\unity\Unity-Robotics-Hub\tutorials\pick_and_place`
    - `git submodule update --init --recursive`
    - `docker build -t unity-robotics:pick-and-place -f docker/Dockerfile .`
- Starting tutorial ROS docker: `docker run -it --rm -p 10000:10000 unity-robotics:pick-and-place /bin/bash`
- Should open a bash in the ROS workspace root
- With volume: `docker run -v /mnt/d:/var/ddrive -it --rm -p 10005:10005 unity-robotics:pick-and-place /bin/bash`
- Didn't work
    - `roslaunch niryo_moveit part_2.launch tcp_ip:=127.0.0.1 tcp_port:=10005`
    - `roslaunch niryo_moveit part_2.launch tcp_ip:=172.17.0.2 tcp_port:=10005`
- Worked
    - `docker run -v /mnt/d:/var/ddrive -it --rm -p 10005:10005 unity-robotics:pick-and-place /bin/bash`
    - `roslaunch niryo_moveit part_2.launch tcp_port:=10005` this worked
    - `roslaunch niryo_moveit part_3.launch tcp_port:=10005` this worked
    - `c` this worked

- Verification
    - `docker ps`
    - `docker exec -it optimistic_joliot /bin/bash`
    - `source devel/setup.bash`
    - `netstat -a`
- Creating KHI URDF
    - copied robot geometry data (in github repo `khi_Robot/rs_description` ) to Unity Assets folder `Assets/khi_urdf/khi_description`
    - copied the `..Assets/khi_urdf/khi_description/urdf` directory to `~/khi_urdf` in wsl
        - `cp -r khi_urdf ~`
    - Then created the `rs0008n.urdf` and copied back to unity
```    
1542 cd khi_urdf/
1543 ls
...
1551 rosrun xacro xacro --inorder -o rs007n.urdf rs007n.urdf.xacro
1552 ls
1553 ls  -ali
1554 cp rs007n.urdf /mnt/d/unity/Unity-Robotics-Hub/tutorials/pick_and_place/PickAndPlaceProject/Assets/khi_urdf
```
# Import into unity
- Copy the urdf file into assets directory somewhere
- Left-click Select the urdf file in assets folder (it won't have an extension)
- Towards the bottom Under "Open C# Project" you should see "Import Robot from Selected URDF file" - select that
- Robot will be imported (a progress bar will advance with each link)
- For the table demo you need to adjust the "transform position y value" to 0.624
    
```
root@daab8248f515:/catkin_ws# netstat -a
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:35253           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:10005           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:37205           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:37601           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:42787           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:37481           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:35019           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:44493           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:11311           0.0.0.0:*               LISTEN
tcp        0      0 daab8248f515:42274      daab8248f515:35019      ESTABLISHED
tcp        0      0 daab8248f515:35019      daab8248f515:42274      ESTABLISHED
tcp        0      0 daab8248f515:35019      daab8248f515:42282      ESTABLISHED
tcp        0      0 localhost:11311         localhost:45846         ESTABLISHED
tcp        0      0 localhost:11311         localhost:45836         ESTABLISHED
tcp        0      0 localhost:45846         localhost:11311         ESTABLISHED
tcp        0      0 daab8248f515:44493      daab8248f515:60160      ESTABLISHED
tcp        0      0 daab8248f515:34150      daab8248f515:37481      ESTABLISHED
tcp        0      0 localhost:45838         localhost:11311         ESTABLISHED
tcp        0      0 localhost:45836         localhost:11311         ESTABLISHED
tcp        0      0 daab8248f515:60160      daab8248f515:44493      ESTABLISHED
tcp        0      0 daab8248f515:42282      daab8248f515:35019      ESTABLISHED
tcp        0      0 localhost:11311         localhost:45838         ESTABLISHED
tcp        0      0 daab8248f515:37481      daab8248f515:34150      ESTABLISHED
udp        0      0 0.0.0.0:49446           0.0.0.0:*
Active UNIX domain sockets (servers and established)
Proto RefCnt Flags       Type       State         I-Node   Path
```
From Windows command line:
```
C:\Users\mike>netstat -a | grep 1000
  TCP    0.0.0.0:10005          Absol:0                LISTENING
  TCP    127.0.0.1:10000        Absol:0                LISTENING
  TCP    127.0.0.1:10000        kubernetes:50915       ESTABLISHED
  TCP    127.0.0.1:50915        kubernetes:10000       ESTABLISHED
```

- https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/pick_and_place/2_ros_tcp.md

 - ros settings: localhost and 10005


# KHI Robotics Repo
- Oriented on Noetic Moveit Tutorial Page (https://ros-planning.github.io/moveit_tutorials/)
- Build in a catkin_ws according to instructions here: (https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html)
    - Updated packages
    - Installed catkin
    - installed `wstool`
    - Created a catkin workspace and downloaded Moveit source
    - Installed panda robot somewhere...
- Got RViz to work 
    - `roslaunch panda_moveit_config demo.launch rviz_tutorial:=true`
- Went to Tutorial on "Move Group Python Interface"
    - (https://ros-planning.github.io/moveit_tutorials/doc/move_group_python_interface/move_group_python_interface_tutorial.html)
    - Needed two windows
        - `roslaunch panda_moveit_config demo.launch`
        - `rosrun moveit_tutorials move_group_python_interface_tutorial.py`
- Black screen problem on Surface Book laptop solved with `export LIBGL_ALWAYS_SOFTWARE=1` 
- See also (https://github.com/microsoft/wslg/issues/455)

## Working with KHI_ROBOT
- Open wsl window
- ros bash script
        - `cd ~/ros/catkin_ws`
        - `source devel/setup.bash`
        - `conda activate ros_khi` (on Absol)
        - `roslaunch khi_rs007n_moveit_config demo.launch`
        - This should bring up a ros window with the RS007n robot (without an end effector however)

- ros bash script
        - `cd ~/ros/catkin_ws/src/khi_robot/khi_rs007n_moveit_config/script`
        - `python rs007n_demo.py`
        - This should cause the robot arm to move around randomly forever


