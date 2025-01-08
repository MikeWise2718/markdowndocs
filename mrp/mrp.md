---
title: "Microsoft Mission Robotics Platform"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Github repo: (https://github.com/strategic-missions-and-technologies/MRP)
- Core teams stuff is in TFMR subdirectory

# Teams Toolkit
Much of the app is built around a Teams plug_in. These are normally built using the Teams Toolkit, which has a VS Code extension.
- Test app in `C:\users\mwise\TeamsApps\TestTab`


# Configuing Azure VMs
- You can go with the standard Ubu 22.04 VM
- Probably want a D4 with 16 GB Mem - bigger than what dan recommends
- Probably want like 256 GB Disk
- Definitely turn off secure boot - otherwise you will get into trouble installing v4l2loopback and it will blabber about keys
- You will need XRDP, but in general installation is easier on an SSH terminal because copy and paste doesn't keep breaking and it keeps timing out the screen (royal pain in the ass)
- SSH works best from WSL - so use that
  - need to generate a dfpem key and drop it into your .ssh both in windows and in wsl home directory
- ROS install:
  - default desktop
  - dev tools
  - image-* (this is where image publisher gets added)
- You will need to configure a password for XRDP - 12 length, capitals, lower, numbers and special chars
   - if you don't you will have problems with intune
- You need to install V4l2loopback-dkms-013.2_1, then V4l2loopback-utils-013.2_1 then linux_extra_modules
- Changing a user password invalidates your browser keyring - need to delete files in ~/.local/share/keyrings
- `lsof -i -P -n` is your friend (list open files)

# Build plug-in

## Steps to build plug-in
- Following readme in TFMR/teams_plugin
- Installed Node 18.4.0 (LTS) -
  - https://nodejs.org/en/download/package-manager
  - used the "Prebuilt Installer" Option which installed
- Need to be signed in to the proper tenant (i.e. an email with a domain)
- Also need an M365 account in that tenant (They gave me a full Office 365 E5 license)
- F5 then builds the app and puts it .... where?

## Using that app that app
- Seems to only be usable as shared in a meeting
- Sign into teams with that tenant.
- Schedule a meeting
- Join that meeting
- Click on "+ Apps" in the top menu bar
- Dialog opens, click on "Manage Apps" button at the bottom
- Click on "Apps" on the far left vertical bar
- Stuff opens  - Click on "Manage your Apps" button at the bottom left
- Another window should open - click on "MRP local" if you can find it (Should be near "MRP copilot")
- Click on "Personal App" at the bottom
- The app should open with a black horizontal stripe
- Click on "Present Now" in the upper right
- Will ask you to "Share MRP Local"
- A new dialog will open with "Cancel" and "Start Sharing", select "Start Sharing"
- Apparently the app is now being shared

# linux-robot-side

## linux-robot-side directory
- No readme so had to guess - guess based on contents of `package.json`
- Installed NPM
- Installed Node version 18 (may not have been necessary, may be a mistake, had to deinstall version 12 first)
- `sudo npm install -g browserify`
- `sudo npm install @azure/communication-common`
- `sudo npm install @azure/communication-calling`
- ` npm run bundle` (not sure I need to do this actually)
- Finished without errors
- Couldn't see anything else to do

## linux-robot-side/docker directory
- There is a readme
- `build.sh` and `run_image.sh` files had lots of ^M in them - DOS linefeeds
   - removed using vim commands `:set ff=unix` then `:w`
- had to change distro from "desktop" to "desktop-full"
- `sudo ./build.sh humble` built an image
- `docker image list` showed that it built the image but it had no tag?
- THere was an error message `usermod: user 'ubuntu' does not exist` - could mount the image and see what is in There
- `run_image.sh humble 5 3` failed with
   - `modprobe: FATAL: Module v4l2loopback not found in directory /lib/modules/5.15.153.1-microsoft-standard-WSL2`
   - `chown: cannot access '/dev/video3': No such file or directory`
   - `chown: cannot access '/dev/video4': No such file or directory`
   - `chown: cannot access '/dev/video5': No such file or directory`
   - `chown: cannot access '/dev/video6': No such file or directory`
   - `chown: cannot access '/dev/video76': No such file or directory`
- Led me to conclude we need to get the 412loopback working

# Video v4l2Loopback

## gz_sim
- start_sim.sh
   - `start_sim.sh -h` lists several options that simply don't work
      - like `./start-sim.sh ./world_model/my_world.sdf`, find complains about `name` vs `wholename`
      - very unhelpful - lost a couple of hours looking into this
- start_sim_add... stuff
   - had to install `ros_gz_bridge`
      - complained it couldn't find the package
      - pkg list
     - `sudo apt install ros-humble-ros-gz-bridge`
   - had to install `xacro`
      - couldn't generate the robot model after unhelpfully deleting the robot file
      - then complained the file that was there no longer existed - a bit confusing
      - `sudo apt install ros-humble-xacro`

## Fail
- Standard 12.1 failed to compile because of change in kernel code (using a different `strXcpy`)

## Installing 0.13.2
- Helpful video: (https://www.youtube.com/watch?v=pKLVNcP0wsk)
- Follow instructions in (https://forums.debian.net/viewtopic.php?t=159976) in post #5
   - `sudo apt install linux-headers-$(uname -r)`
   - `wget http://ftp.us.debian.org/debian/pool/main/v/v4l2loopback/v4l2loopback-dkms_0.13.2-1_all.deb`
   - `sudo dpkg -i v4l2loopback-dkms_0.13.2-1_all.deb`
   - Secure boot pass: "Pikachu22.04!"
- On an Azure (or AWS) VM you need to do this too
   -  `sudo apt -y install v4l2loopback-dkms v4l2loopback-utils linux-modules-extra-$(uname -r)`
   - probably need to rebuild v4l2loopback after this
- To get the utils:
   - `wget http://ftp.us.debian.org/debian/pool/main/v/v4l2loopback/v4l2loopback-utils_0.13.2-1_amd64.deb`
   - `sudo dpkg -i v4l2loopback-utils_0.13.2-1_amd64.deb`

## Testing
   - Check the `/dev` first
     - `ls /dev/v*1`
     - should be no `/dev/video0`, etc
     - `sudo modprobe v4l2loopback`
     - `ls /dev/v*1`
     - should have `/dev/video0`, and `/dev/v4l2loopback`
     - `sudo v4l2loopback-ctl add -n "loopy doopy" /dev/video7`
     - should have added `/dev/video7`

## Other commands
     - There is also, confusingly `v42l-ctl` which is a different program
        - `v4l2-ctl --list-devices`
    `- `sudo modprobe v4l2loopback video_nr=5 card_label="Virtual Camera" exclusive_caps=1`
     - Remove with `sudo modprobe v4l2loopback -r`
     - Driver info:
       `v4l2-ctl --device=/dev/video5 --all`

## Testing with actual video
    - From (https://superuser.com/a/1331422/524399)
    - Play video: `ffmpeg -re -stream_loop -1 -i input.mp4 -f v4l2 /dev/video0`
    - Play image: `ffmpeg -loop 1 -i lena512.jpg -f v4l2 /dev/video0`
    - Play desktop: `ffmpeg -f x11grab -framerate 25 -video_size 1280x720 -i :1 -f v4l2 /dev/video0`
        - note the value of the -i parameter `:1` is the value that `echo $DISPLAY` outputs
    - Watch video 1: `ffplay -f v4l2 /dev/video0`
    - Watch video 2: `mpv --demuxer-lavf-format=v4l2 /dev/video0` (didn't work for me)
    - Watch video 3: Open `vlc` and "Open Capture Device" and select `dev/video0` from dropdown
    - Watch video 4: `timg --center /dev/video0` (worked but was mosaic blurred since a terminal is not "pixel addressable")

## ros_virtual_camera
 - followed brief instructions in readme
 - installed `libv4l` without issue
 - v4l2loopback gave some compile problems but eventually got it to work
 - Initialized `rosdep` (It had not been used yet and complained)
 - All dependencies installed okay
 - Colcon ran without complaints
 - `source ./install/setup.bash` ran without complaints
 - No notes on how to test this

### Getting ros_virtual_cam to work
 - It is old ROS1 code running in a container!
 - lives in `linux-robot-side/ros_virtual_cam-main/`
 - `$ACS_PROJECT_DIR` = `/home/mike/MRP/TFMR`
 -  needs to be initialized with:
 ```
 source $ACS_PROJECT_DIR/linux-robot-side/ros_virtual_cam-main/install/setup.bash
sudo modprobe -r v4l2loopback
sudo modprobe v4l2loopback video_nr=3 card_label="RobotBlue"

 ```
 - `ROS_DOMAIN_ID=50 ros2 launch ros_virtual_cam ros_virtual_cam.launch.py device:=/dev/video3 topic:=/rgb_jackal &`
 - note that the `ros_virtual_cam.launch.py` is responsible for transferring parameters from the environment to the ROS1 code -  this took me a long time to find
 - can look at `ROS_DOMAIN_ID=50 ros2 topic echo /rgb_jackal` to see if there is any output (a bunch of bytes changing by a little bit a few times a second)
 - can view `/dev/video3` in either `VLC` or `ffplay` above

## Joystick
- (https://www.youtube.com/watch?v=UP4h7EZaqSs)
   - `sudo apt-get install xboxdrv joystick`
   - `sudo apt-get install jstest-gtk`
   - To test now start the `jstest-gtk` app and see if it works
   - can also test with `jstest /dev/input/js0`

   - `ros2 launch single-robot-launch.yaml &`
      - let to the creation of the missing topics
      -
```
mike@luxray:~/MRP/TFMR/linux-robot-side/launch/omniverse$ ros2 topic list
/RobotBlue/cmd_vel
/blue/joy
/parameter_events
/rosout
```

# Omniverse start-sim.sh
  - Seems to be accessing TFMR/simulation/omniverse/B25_Spot_MRPintegration.usda
  - Not actually using Spot, using a Jackel robot
  - Start simulation that references with
       `./start-sim.sh -r RobotBlue -c 3 -d 44 -v 3001 -j 1030 -b '/robot/joy' -f 'robot/image`
       - d parameter is for robot domain
       - Thus `ROS_DOMAIN_ID=44 ros2 topic list -t`
`fd``
mike@luxray:~$ ROS_DOMAIN_ID=44 ros2 topic list -t
/RobotBlue/cmd_vel [geometry_msgs/msg/Twist]
/blue/joy [sensor_msgs/msg/Joy]
/clock [rosgraph_msgs/msg/Clock]
/front_stereo_camera/left/image_rect_color [sensor_msgs/msg/Image]
/gps [sensor_msgs/msg/NavSatFix]
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/robot/image [sensor_msgs/msg/Image]
/robot/joy [sensor_msgs/msg/Joy]
/rosout [rcl_interfaces/msg/Log]

```


# ACSNode.js
- Added a line recognizing `humble` in addition to `jazzy`
- Then Errored out by not being able to `/home/mike/.mozilla/firefox/RobotBlue`
- Created the directory by hand and it went further, eventually complaining about a missing "ClientID"

# Teamsfx 5.0
- Video explaining changes:(https://www.youtube.com/watch?v=j_ixFGdNrRE&t=719s)
- Docs: https://github.com/OfficeDev/teams-toolkit
- To install:
    - from: (https://www.npmjs.com/package/@microsoft/teamsfx-cli)
    - `npm install -g @microsoft/teamsfx-cli`
    - `teamsfx -h`
- `teamsfx` is now depreciated
- `teamsapp` seems to be essentially the same app but newer with a different name
- New install:
    - From docs below
    - ` npm install -g @microsoft/teamsapp-cli`
    - `teamsapp -h`
    - Installed version on 10 Nov 2024:
       - `teamsapp -v`
       - 13.0.41
- New Docs:(https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/teams-toolkit-cli?pivots=version-three)

# Doc notes
Each section addresses a markdown document

## README.md
- /README.md
- Top-level Readme should say what the high-level use cases (HLUC) could be for someone using it.
  - Using it for a canned demo for a prospective user
  - Adding a new robot
  - Adding a new copilot (set)
  - What else?
- Probably a video of using it for a canned demo could be provided.
- A high level architecture diagram would be extremely helpful as well - maybe by use case.
- Should have separate setup steps for all of these different use cases.
- Nitpicks
   - the `git clone` command is ludicrous and confusing
   - "setup the development container"  (wth?)
      - There are 6 different containers in MRP
      - However after looking around this is probably the container in the directory `.devcontainer`
      - Unfortunately `.devcontainer` it has no `readme.md` so I can only guess.
      - `.devcontainer` brings up two services containers - the container defined and built in it's own directory, and the CosmosDB emulator directory.
      - It seems to use Docker-compose to manage a few other containers
   - "Follow the prompts..." I didn't get any prompts like this
   - 1. "FOllow the guildelines" (come on)
   - There is no 2. or higher

- "Development Philosophy" should be moved to the end
- "Contribution Guidelines" should be part of the HLUC workflows

## CONTRIBUTING.md
- /CONTRIBUTING.md
- Should mention the presumed OS as not everything works on both Windows 11 and Ubuntu
- `Tooling Requirements` needs notes for installing each tool
 - Like where the tools are mainly used.
 - Also example does the CosmosDB emulator want NOSQL or MongoDB or something else even.
- `Configure CosmosDB Emulator` is really about configuring the `cpmr` container to use the correct Cosmos DB. This is confusing.
- `Running Tests` - what to the tests test? Surely not everything.
