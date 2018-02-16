---
title: "Ubuntu"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Ubuntu seems to be the data science standard now.

# Terminal windows
- You pretty much do all system stuff via the terminal with good old Linux commands
- Ctrl-Shift-V to paste

# Installing Chrome
- The automatic installd did not work
- Downloaded the deb package (google-chrome-stable_current_amd64.deb) from google into ~/Downloads
- Installed gdebi with sudo apt-get install gdebi
- Installed chrome with sudo gdebi -i google-chrome-stable_current_amd64.deb
- Found "Google Chrome" in /usr/share/applications

# RDP (Remote Deskttop from Windows)
- For a long time this did not work at all as Ubuntu uses a Desktop Environment as opposed to a window manager.
- There are two ways to do remote desktop, VNC or RDP (the latter is kind of Windows specific and has better graphics than Generic VNC which is JPEG vased).
- TigerVNC (derived from the older TightVNC) apparently supports RDP too.
- Install [xrdp](https://help.ubuntu.com/community/xrdp)
- Install TigerVNC on Ubuntu (https://github.com/TigerVNC/tigervnc/releases)
- TigerVNC Ubuntu Install [instructions](http://linuxpitstop.com/install-tigervnc-1-5-on-linux/)
- Note that in bintray there are binaries just fur [Ubuntu](https://bintray.com/tigervnc/stable/tigervnc/1.8.0#files)
- Had to install with gdebi to get the dependencies installed.
- Useful post setting screen size is [here](https://askubuntu.com/questions/948774/configure-tigervnc-server-to-start-with-system-in-ubuntu-gnome-16-04)

# VNC
Finally got something working, but it is not great.
Ubuntu:
- installed mir on Ubuntu with sudo apt-get install unity8-desktop-session-mir
- this was a heavy install that apparently installs the unity8 desktop (although I did not see it)
- Changed the configuration to enable remote desktop with "dconf-editor"
- under org.gnome.desktop.remote-access set the "enabled" checkbox
- You then get a connection, but the tiger vncclient complains there is no matching encription
- you can get a connection by settting "require-encryption" above to false
- Left it disabled for now
- Next steps: substitute tigervnc for vino-server
Windows:
- Installed tigervnc on windows
- used the tigervnc "vncviewer" to connect to the server addess and port 5900

# NoMachine
- I gave up on all that VNC stuff when I found NoMachine.
- It has a client, start in Windows with Windows Key and then type "NoMachine"
- It is commercial, but free for home use

# Misc Unix commands
- grep stuff files - grep -r tqdm *.py .
- find files with a mask find . -path "*/src/*.h"
- find filew with masks - find . -path '*/src/*.h' -o -path '*/src/*.cpp'
- find files and pipe to greap - find . -path '*/src/*.h' -exec grep PATTERN {}
- change field 3 to AD - awk '{$3 = "AD"; print}' infile > outfile

# Terminal Window
- Note that the "super" key is the "windows" key in the docs. 
- Open Terminal Window - Ctrl-Alt-T
- Paste into Terminal Window - Ctrl-Shift-V
- Other shortcuts can be found [here](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)


# Applications
- Application launch icons can be found in /usr/share/applications

# Perf monitoring
- Useful [link](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)

# Installation
- Followed instructions on Ubuntu site to burn USB stick to boot from
- Downloaded an ISO and put it on there
- Needs a live Internet connection apparently (uses DHCP)
- Couldn't boot from the stick in Hyper-V because the USB drive has no pass-thru functionality (oddly)
- Installation straightforward
- Installed Chrome next (via Firefox)
