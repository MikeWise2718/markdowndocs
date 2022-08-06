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
- Black screen problem on Surface Book laptop solved with 
  - `export LIBGL_ALWAYS_SOFTWARE=1` 
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


# Compiling ROS2 Foxy on Windows

- Foxy Instructions (https://docs.ros.org/en/foxy/Installation/Alternatives/Windows-Development-Setup.html)
- Checklist:
 - `choco`
 - python (3.8.3)
 - `pip install -U vcstool`
 - `pip install -U colcon-common-extensions`
 - `pip install -U pytest pytest-mock coverage mock`
    - `pytest` didn't work had to back up to version 6.0
 - `choco install -y curl`
 - `python -m pip install -U setuptools pip`
 - `pip install -U flake8 flake8-blind-except flake8-builtins flake8-class-newline flake8-comprehensions flake8-deprecated flake8-docstrings flake8-import-order flake8-quotes mypy==0.761 pep8 pydocstyle`

 - `choco install -y cppcheck`
 - Next install `xmllint`:
       - Download the 64 bit binary archives of `libxml2` (and its dependencies `iconv` and `zlib`) from https://www.zlatkovic.com/projects/libxml/
       -  Unpack all archives into e.g. `C:\xmllint`
       - Add `C:\xmllint\bin` to the PATH.
       - Run some exe to see if it works
- Qt5
    - didn't do the following `setx` things as they refered to non-existent directories
       - `setx /m Qt5_DIR C:\Qt\Qt5.12.12\5.12.12\msvc2017_64`
       - `setx /m QT_QPA_PLATFORM_PLUGIN_PATH C:\Qt\Qt5.12.12\5.12.12\msvc2017_64\plugins\platforms`
- Testing
    -


## Colcon
  - output immediately on console: `colcon <verb> --event-handlers console_direct+`
  - single package build: `colcon build --packages-select <name-of-pkg> <name-of-another-pkg>`
  - package and dependencies: `colcon build --packages-up-to <name-of-pkg>`
  - packages and dependents: `colcon build --packages-above <name-of-pkg>`
  - frequent
     - `colcon build --packages-select rosbag2 --event-handlers console_direct+`
     - `colcon build  --merge-install --packages-select rosbag2_transport --event-handlers console_direct+`
     - `colcon build  --merge-install --packages-select test_rclcpp --event-handlers console_direct+`
     - `colcon build  --merge-install --packages-select rviz_common --event-handlers console_direct+`
     - `colcon build  --packages-select moveit_common --event-handlers console_direct+`


### rviz_common ROS 2 package problem 
Was compiling on my hyper-v installation but not on absol.


```
>colcon build --merge-install
...       
Summary: 247 packages finished [9min 7s]
  1 package failed: rosbag2_transport
  17 packages aborted: composition demo_nodes_cpp demo_nodes_cpp_native examples_tf2_py image_tools logging_demo robot_state_publisher ros2test rqt_gui_py test_rclcpp tf2_bullet tf2_eigen tf2_geometry_msgs tf2_kdl tf2_sensor_msgs tf2_tools tracetools_test
  50 packages had stderr output: action_tutorials_py ament_clang_format ament_clang_tidy ament_copyright ament_cppcheck ament_cpplint ament_flake8 ament_index_python ament_lint ament_lint_cmake ament_mypy ament_package ament_pclint ament_pep257 ament_pycodestyle ament_pyflakes ament_uncrustify ament_xmllint demo_nodes_py domain_coordinator examples_rclpy_executors examples_rclpy_minimal_action_client examples_rclpy_minimal_action_server examples_rclpy_minimal_client examples_rclpy_minimal_publisher examples_rclpy_minimal_service examples_rclpy_minimal_subscriber launch launch_ros launch_testing launch_testing_ros launch_xml launch_yaml osrf_pycommon quality_of_service_demo_py rmw_connext_cpp rmw_connext_shared_cpp ros2cli ros2multicast ros2trace rosidl_runtime_py rosidl_typesupport_connext_c rosidl_typesupport_connext_cpp rpyutils rqt_gui sensor_msgs_py topic_monitor tracetools_launch tracetools_read tracetools_trace
  46 packages not processed
  ```

  `colcon graph --packages-up-to rviz_common --dot >rviz_common_graph.dot`
  `dot rviz_common_graph.dot`
  `dot rviz_common_graph.dot -Tpng -o rviz_common_graph.png`

`colcon build --merge-install --packages-select rviz_common --event-handlers console_direct+`
  ```
  Starting >>> rviz_common
-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.22000.
-- Found ament_cmake: 0.9.10 (D:/ros/foxy/install/share/ament_cmake/cmake)
-- Using PYTHON_EXECUTABLE: C:/opt/ros/foxy/x64/python.exe
-- Found rviz_ogre_vendor: 8.2.6 (D:/ros/foxy/install/share/rviz_ogre_vendor/cmake)
-- Prepending to CMAKE_MODULE_PATH: 'D:/ros/foxy/install/share/rviz_ogre_vendor/cmake/../../../opt/rviz_ogre_vendor/CMake'
-- Setting OGRE_DIR to: 'D:/ros/foxy/install/share/rviz_ogre_vendor/cmake/../../../opt/rviz_ogre_vendor/CMake'
-- Found OGRE
--   static     : OFF
--   components : HLMS;MeshLodGenerator;Overlay;Paging;Property;RTShaderSystem;Terrain;Volume
--   plugins    : Plugin_BSPSceneManager;Plugin_OctreeSceneManager;Plugin_PCZSceneManager;Plugin_ParticleFX;RenderSystem_GL;RenderSystem_GL3Plus;Codec_STBI;Codec_FreeImage
--   media      : D:/ros/foxy/install/opt/rviz_ogre_vendor/Media
-- OGRE_LIBRARIES: OgreHLMS;OgreMeshLodGenerator;OgreOverlay;OgrePaging;OgreProperty;OgreRTShaderSystem;OgreTerrain;OgreVolume;OgreMain
-- OGRE_LIBRARY_DIRS: D:/ros/foxy/install/opt/rviz_ogre_vendor/lib
-- OGRE_PLUGINS: Plugin_BSPSceneManager;Plugin_OctreeSceneManager;Plugin_PCZSceneManager;Plugin_ParticleFX;RenderSystem_GL;RenderSystem_GL3Plus;Codec_STBI;Codec_FreeImage
-- OGRE_PLUGIN_DIR: D:/ros/foxy/install/opt/rviz_ogre_vendor/lib/OGRE
-- rviz_ogre_vendor::OgreOverlay for IMPORTED_LOCATION_RELEASE: D:/ros/foxy/install/opt/rviz_ogre_vendor/lib/OgreOverlay.lib
-- rviz_ogre_vendor::OgreOverlay for IMPORTED_LOCATION_DEBUG: _ogre_overlay_static_library_debug_abs-NOTFOUND
-- rviz_ogre_vendor::OgreMain for IMPORTED_LOCATION_RELEASE: D:/ros/foxy/install/opt/rviz_ogre_vendor/lib/OgreMain.lib
-- rviz_ogre_vendor::OgreMain for IMPORTED_LOCATION_DEBUG: _ogre_main_static_library_debug_abs-NOTFOUND
-- rviz_ogre_vendor::RenderSystem_GL for IMPORTED_LOCATION_RELEASE: D:/ros/foxy/install/opt/rviz_ogre_vendor/lib/OGRE/RenderSystem_GL.lib
-- rviz_ogre_vendor::RenderSystem_GL for IMPORTED_LOCATION_DEBUG: _render_system_gl_static_library_debug_abs-NOTFOUND
-- Found geometry_msgs: 2.0.5 (D:/ros/foxy/install/share/geometry_msgs/cmake)
-- Using all available rosidl_typesupport_c: rosidl_typesupport_fastrtps_c;rosidl_typesupport_introspection_c
-- Found rosidl_adapter: 1.2.1 (D:/ros/foxy/install/share/rosidl_adapter/cmake)
-- Using all available rosidl_typesupport_cpp: rosidl_typesupport_fastrtps_cpp;rosidl_typesupport_introspection_cpp
-- Found pluginlib: 2.5.4 (D:/ros/foxy/install/share/pluginlib/cmake)
-- Found rclcpp: 2.4.2 (D:/ros/foxy/install/share/rclcpp/cmake)
-- Found rmw_implementation_cmake: 1.0.3 (D:/ros/foxy/install/share/rmw_implementation_cmake/cmake)
-- Using RMW implementation 'rmw_fastrtps_cpp' as default
-- Found resource_retriever: 2.3.4 (D:/ros/foxy/install/share/resource_retriever/cmake)
-- Found rviz_assimp_vendor: 8.2.6 (D:/ros/foxy/install/share/rviz_assimp_vendor/cmake)
-- library: assimp-vc142-mt.lib
-- Found rviz_rendering: 8.2.6 (D:/ros/foxy/install/share/rviz_rendering/cmake)
-- Found sensor_msgs: 2.0.5 (D:/ros/foxy/install/share/sensor_msgs/cmake)
-- Found tinyxml_vendor: 0.8.2 (D:/ros/foxy/install/share/tinyxml_vendor/cmake)
-- Found tf2: 0.13.13 (D:/ros/foxy/install/share/tf2/cmake)
-- Found tf2_geometry_msgs: 0.13.13 (D:/ros/foxy/install/share/tf2_geometry_msgs/cmake)
-- Found urdf: 2.4.0 (D:/ros/foxy/install/share/urdf/cmake)
-- Found yaml_cpp_vendor: 7.0.2 (D:/ros/foxy/install/share/yaml_cpp_vendor/cmake)
-- Setting yaml-cpp_DIR to: 'D:/ros/foxy/install/share/yaml_cpp_vendor/cmake/../../../opt/yaml_cpp_vendor/CMake'
-- Found ament_cmake_cppcheck: 0.9.7 (D:/ros/foxy/install/share/ament_cmake_cppcheck/cmake)
-- Found ament_cmake_cpplint: 0.9.7 (D:/ros/foxy/install/share/ament_cmake_cpplint/cmake)
-- Found ament_cmake_lint_cmake: 0.9.7 (D:/ros/foxy/install/share/ament_cmake_lint_cmake/cmake)
-- Found ament_cmake_uncrustify: 0.9.7 (D:/ros/foxy/install/share/ament_cmake_uncrustify/cmake)
-- Found ament_cmake_gmock: 0.9.10 (D:/ros/foxy/install/share/ament_cmake_gmock/cmake)
-- Found ament_cmake_gtest: 0.9.10 (D:/ros/foxy/install/share/ament_cmake_gtest/cmake)
-- Found gmock sources under 'D:/ros/foxy/install/src/gmock_vendor': C++ tests using 'Google Mock' will be built
-- Found gtest sources under 'D:/ros/foxy/install/src/gtest_vendor': C++ tests using 'Google Test' will be built
-- Configuring done
-- Generating done
-- Build files have been written to: D:/ros/foxy/build/rviz_common
Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

  gmock.vcxproj -> D:\ros\foxy\build\rviz_common\gmock\Release\gmock.lib
  gmock_main.vcxproj -> D:\ros\foxy\build\rviz_common\gmock\Release\gmock_main.lib
     Creating library D:/ros/foxy/build/rviz_common/Release/rviz_common.lib and object D:/ros/foxy/build/rviz_common/Release/rviz_common.exp
yaml_config_reader.obj : error LNK2019: unresolved external symbol "__declspec(dllimport) public: __cdecl YAML::InvalidNode::InvalidNode(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)" (__imp_??0InvalidNode@YAML@@QEAA@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z) referenced in function "public: class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > __cdecl YAML::Node::as<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >(void)const " (??$as@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Node@YAML@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@XZ) [D:\ros\foxy\build\rviz_common\rviz_common.vcxproj]
    Hint on symbols that are defined and could potentially match:
      "__declspec(dllimport) public: __cdecl YAML::InvalidNode::InvalidNode(class YAML::InvalidNode const &)" (__imp_??0InvalidNode@YAML@@QEAA@AEBV01@@Z)
D:\ros\foxy\build\rviz_common\Release\rviz_common.dll : fatal error LNK1120: 1 unresolved externals [D:\ros\foxy\build\rviz_common\rviz_common.vcxproj]
  gtest.vcxproj -> D:\ros\foxy\build\rviz_common\gtest\Release\gtest.lib
  gtest_main.vcxproj -> D:\ros\foxy\build\rviz_common\gtest\Release\gtest_main.lib
Failed   <<< rviz_common [17.2s, exited with code 1]

Summary: 0 packages finished [18.3s]
  1 package failed: rviz_common
```


# Current Status


## fails with missing  stuff "InvalidNode in yaml thing
- Loglevels: DEBUG INFO WARNING ERROR CRITICAL
- `colcon --log-level DEBUG build --merge-install --packages-select rviz_common --event-handlers console_direct+`
- first cmake: 
```
Invoked command in 'D:\ros\foxy\build\rviz_common' returned '0': AMENT_PREFIX_PATH=D:\ros\foxy\install;%AMENT_PREFIX_PATH% CMAKE_PREFIX_PATH=D:\ros\foxy\install;%CMAKE_PREFIX_PATH% PKG_CONFIG_PATH=D:\ros\foxy\install\lib\pkgconfig;%PKG_CONFIG_PATH% PYTHONPATH=D:\ros\foxy\install\Lib\site-packages;%PYTHONPATH% Path=D:\ros\foxy\install\Scripts;D:\ros\foxy\install\bin;D:\ros\foxy\install\opt\yaml_cpp_vendor\bin;D:\ros\foxy\install\opt\rviz_ogre_vendor\bin;%Path% c:\opt\ros\foxy\x64\Scripts\cmake.EXE D:\ros\foxy\src\ros2\rviz\rviz_common -DCMAKE_INSTALL_PREFIX=D:\ros\foxy\install
```
- second cmake:
```
D:\ros\foxy\src\ros2\rviz\rviz_common\src\rviz_common\yaml_config_writer.cpp : message : see previous definition of 'YAML_CPP_DLL' [D:\ros\foxy\build\rviz_common\rviz_common.vcxproj]
     Creating library D:/ros/foxy/build/rviz_common/Release/rviz_common.lib and object D:/ros/foxy/build/rviz_common/Release/rviz_common.exp
yaml_config_reader.obj : error LNK2019: unresolved external symbol "__declspec(dllimport) public: __cdecl YAML::InvalidNode::InvalidNode(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)" (__imp_??0InvalidNode@YAML@@QEAA@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z) referenced in function "public: class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > __cdecl YAML::Node::as<class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > >(void)const " (??$as@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Node@YAML@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@XZ) [D:\ros\foxy\build\rviz_common\rviz_common.vcxproj]
    Hint on symbols that are defined and could potentially match:
      "__declspec(dllimport) public: __cdecl YAML::InvalidNode::InvalidNode(class YAML::InvalidNode const &)" (__imp_??0InvalidNode@YAML@@QEAA@AEBV01@@Z)
D:\ros\foxy\build\rviz_common\Release\rviz_common.dll : fatal error LNK1120: 1 unresolved externals [D:\ros\foxy\build\rviz_common\rviz_common.vcxproj]
  Building Custom Rule D:/ros/foxy/install/src/gtest_vendor/CMakeLists.txt
  gtest-all.cc
[Processing: rviz_common]
  gtest.vcxproj -> D:\ros\foxy\build\rviz_common\gtest\Release\gtest.lib
  Building Custom Rule D:/ros/foxy/install/src/gtest_vendor/CMakeLists.txt
  gtest_main.cc
  gtest_main.vcxproj -> D:\ros\foxy\build\rviz_common\gtest\Release\gtest_main.lib
[34.290s] colcon.colcon_core.event_handler.log_command DEBUG Invoked command in 'D:\ros\foxy\build\rviz_common' returned '1': AMENT_PREFIX_PATH=D:\ros\foxy\install;%AMENT_PREFIX_PATH% CL=/MP CMAKE_PREFIX_PATH=D:\ros\foxy\install;%CMAKE_PREFIX_PATH% PKG_CONFIG_PATH=D:\ros\foxy\install\lib\pkgconfig;%PKG_CONFIG_PATH% PYTHONPATH=D:\ros\foxy\install\Lib\site-packages;%PYTHONPATH% Path=D:\ros\foxy\install\Scripts;D:\ros\foxy\install\bin;D:\ros\foxy\install\opt\yaml_cpp_vendor\bin;D:\ros\foxy\install\opt\rviz_ogre_vendor\bin;%Path% c:\opt\ros\foxy\x64\Scripts\cmake.EXE --build D:\ros\foxy\build\rviz_common --config Release
```
## works
- On ABSOL Start a command shell and initialize it with "foxy" which does a `c:\opt\...local_setup.bash` initialization
- ros2 will then run
- Then go to `d:\ros\foxy\src\ros2\rviz\rviz_common`
- `rm -r build; md build; cd biuld`
- `cmake ..`
- `cmake --build .` fails with a missing ogre obj
- `cmake --build . --config Release` builds a dll


