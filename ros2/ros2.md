---
title: "ROS 2"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- ROS2  - Robotics Operating System is not really an OS, it is a "System for operating robots". More like middleware
- ROS Discourse - (https://discourse.ros.org/)
- Colcon - quick start - (https://colcon.readthedocs.io/en/released/user/quick-start.html)
  - `colcon list`
  - `colcon graph --dot | dot -Tpng -o foxygraph.png`
  - `colcon build --merge-install`
 - `colcon graph --packages-up-to tinyxml2_vendor`
      - Issue (https://github.com/ros2/ros2/issues/927)

# Visual Studio Build Tools
- Location of Shortcuts: `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2019\Visual Studio Tools\VC`

# Dependency Graphs
  - `colcon graph --dot | dot -Tpng -o foxygraph.png`

## ROS2 containers

## Install ROS2 binary package on Windows 11 Native
- binary install: (https://docs.ros.org/en/foxy/Installation/Windows-Install-Binary.html)l


## Compile ROS2 Foxy on Windows 11 Native
- Tips and tricks: (https://docs.ros.org/en/galactic/The-ROS2-Project/Contributing/Windows-Tips-and-Tricks.html)
- Have to install the binary prerequisites first: (https://docs.ros.org/en/foxy/Installation/Windows-Install-Binary.html)
   - Install Chocolatey (1.1.0): (https://chocolatey.org/)\
    - See what packages are installed already with `choco list -l`
   - Install Python 3.8: (`choco install -y python --version 3.8.3`)
      - has to go into `C:\python3.8` which is odd
   - Install Visual C++ Redistributables: (`choco install -y vcredist2013 vcredist140`)
   - Install OpenSSL from (https://slproweb.com/products/Win32OpenSSL.html) - dubious location
     - `Win64 OpenSSL v1.1.1n OpenSSL` installer (I used the msi and version is q now)
     - Creates directory in `C:\Program Files\OpenSSL-Win64` with stuff in it
     - might need to do this if installer doesn't set it:
        - `setx /m OPENSSL_CONF "C:\Program Files\OpenSSL-Win64\bin\openssl.cfg"`
     - Append `C:\Program Files\OpenSSL-Win64\bin\` to path
     - Test: `dir "%OPENSSL_CONF%"`
     - Test: `openssl` should open an OpenSSL prompt that you can exit
    - Install Visual Studio 2019 (Community?)
       - Make sure `Desktop Development with C++` was selected.
       - Make sure that no C++ CMake tools are installed by unselecting them in the list of components to be installed.
          - not sure how to check this
    - Install OpenCV
       - Precompiled from: (https://github.com/ros2/ros2/releases/download/opencv-archives/opencv-3.4.6-vc16.VS2019.zip )
       - Unpack to: `C:\opt\opencv`
       - Admin privileges`setx /m OpenCV_DIR C:\opt\opencv`
       - Add `C:\opt\opencv\x64\vc16\bin` to path
       - Test with `opencv_version.exe` at `3.4.6` a the moment
    - Install random dependencies
       - Install CMake: (`choco install -y cmake`)
          - You will need to append the CMake bin folder `C:\Program Files\CMake\bin` to your PATH.
          - test with `cmake --version` at `3.22.0` at the moment
       - Download the following from ROS2 Choco packages repo: (https://github.com/ros2/choco-packages/releases/tag/2022-03-15):
            - `asio.1.12.1.nupkg`
            - `bullet.2.89.0.nupkg`
            - `cunit.2.1.3.nupkg`
            - `eigen-3.3.4.nupkg`
            - `tinyxml-usestl.2.6.2.nupkg`
            - `tinyxml2.6.0.0.nupkg`
            - `log4cxx.0.10.0.nupkg`
        - `choco install -y -s <PATH\TO\DOWNLOADS> asio cunit eigen tinyxml-usestl tinyxml2 log4cxx bullet`
    - Install some python dependencies
      - `python -m pip install -U catkin_pkg cryptography empy ifcfg lark-parser lxml netifaces numpy opencv-python pyparsing pyyaml setuptools rosdistro`
    - Install QT5
      - Download install program - select individual
      - Select only option Qt/QT5.12.12/MSVC 2017 64-bit
      - Add the following environment vars:
         - `QT_QPA_PLATFORM_PLUGIN_PATH` = `C:\Qt\Qt5.12.12\5.12.12\msvc2017_64\plugins\platforms`\
         - `Qt5_DIR` = `C:\Qt\Qt5.12.12\5.12.12\msvc2017_64`
      - Test:
         - `dir %QT_QPA_PLATFORM_PLUGIN_PATH%` should show dlls
         - `dir %Qt5_DIR%` should show directories including `bin`
    - Install RQt dependencies
      - `python -m pip install -U pydot PyQt5`
      - Install `Graphviz`
         - `choco install graphviz`
         -  Add to path: `C:\Program Files\Graphviz\bin`
         - `dot --help` should work

    - Additionally I found I had to install patch
      - `choco install patch`

    - Colcon
        - `pip install -U colcon-common-extensions`

    - At this point you would normally install the Foxy Windows binaries to
         - Go to the releases page: https://github.com/ros2/ros2/releases
         - Download the latest package for Windows, e.g., `ros2-foxy-*-windows-AMD64.zip`.
         - Unpack the zip file to `C:\dev\ros2_foxy` or something

    - Troubleshooting:
      - (https://docs.ros.org/en/foxy/How-To-Guides/Installation-Troubleshooting.html)

    - Testing
        - Environment setup: `call C:\dev\ros2_foxy\local_setup.bat`
        - Environment setup: `call C:\dev\ros2_foxy\install\local_setup.bat`
        - `ros2 run demo_nodes_cpp talker`
        - `ros2 run demo_nodes_py listener`

- Instructions: (https://docs.ros.org/en/foxy/Installation/Alternatives/Windows-Development-Setup.html)
- `d:\ros\ros2`
- Compiled most of it but simple test does not work (publishes but does not receive)
- Puzzle: have to delete or rename `yaml-cpp` in `Install/opt` for some unknown reason
- Puzzle: why did I have to rename USD-tools boost? Where was that hint coming from?


## Compile ROS2 Foxy on Windows 11 Hyper-V
- Failed as no access to bash tools like "patch"
- Could try with Cygwin I suppose, or min-gw


# Rosdep

## Compile ROS2 Foxy on Ubuntu Hyper-V
- Worked and simple test worked
- Didn't try Rviz, but it could work
- Tried to compile moveit but failed to find many components like `angles`, `geometric_shapes`, etc.
- Boost?


## Ros2 on WSL
- Seems I have humble hawkbill installed already
- can see what I have done before with `history`
- `source /opt/ros/humble/setup.bash`
- `ros2 run rviz2 rviz2`