---
title: "Catkin"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- A meta system for CMake
- Mostly a set of CMake macros that extend CMAKE to do multi-package builds
- `Ament` - and `ament_tool` is its successor, but seems to have been dropped for Colcon(http://design.ros2.org/articles/ament.html)
- Catkin Conceptual Overview: (http://wiki.ros.org/catkin/conceptual_overview)
- A universal build tool: (http://design.ros2.org/articles/build_tool.html)
- Great Catkin notes: (https://nu-msr.github.io/me495_site/lecture02_catkin.html)

# Docs
- A mistitled explanation of how it works (http://wiki.ros.org/catkin/what#How_To_Migrate_Your_Rosbuild_Package_to_Catkin)
- Real docs: (http://docs.ros.org/en/hydro/api/catkin/html/)
- Note there are two package formats: 1 (legacy) and 2 (recommended)

# Keypoints
- Catkin uses CMAKE_PREFIX_PATH to determine where to look for ROS packages - under `src` I think.
- ROS workspaces remember the state they were in when you built the workspace (e.g., ran catkin_make)
    - When you run `catkin_make` it generates the setup script (e.g. `setup.bash`). 
    - This script sets your ROS path (i.e., `CMAKE_PREFIX_PATH`) to contain all the paths already on it at the time of running `catkin_make` and a path to the current workspace.
    - Therefore, you need to make sure you have all workspaces you need sourced prior to running `catkin_make`.
- Great Catkin notes: (https://nu-msr.github.io/me495_site/lecture02_catkin.html)

# Catkin tools
- A python based set of tools allowing you to do useful Catkin-related things 
- Doesn't work in Windows - use `colcon`
  - Relevant issue: (https://github.com/catkin/catkin_tools/issues/554)
- Pretty - has lots of color coding in the output
- Not actually "Catkin" per-se
- https://catkin-tools.readthedocs.io/en/latest/installing.html
- I think this installs an executable "Catkin.exe" that does not work in Windows because it hasn't been ported
- Seemingly not necessary for Catkin


# Ament
- With the advent of `colcon` ament and its ambition partner `ament_tools` have been sidelined (http://design.ros2.org/articles/ament.html)
```
When this article was originally written ament_tools was the ROS 2 specific build tool. 
The reason was that it needed to be side-by-side installable with existing ROS 1 packages,
 which was a problem due to different targeted Python versions. 
 In the meantime the problem due to different Python versions has been addressed in shared dependencies like catkin_pkg. 
 As of ROS 2 Bouncy ament_tools has been superseded by colcon as described in the universal build tool article.
```
- Universal Build Tool article: (http://design.ros2.org/articles/build_tool.html)