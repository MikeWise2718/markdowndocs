---
title: "QNAP"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- My first QNAP was a TS-409 apparently from 2007/2008 but my first notes are from 2013
- My current (purcah2025) one is a TS-453
- You can access it over http://[ipaddress]:8080
   - Could be I configured that 8080 somewhere, not sure

# Dashbard
- Icon top left (dial-like icon)
- Can select data volume there (I only have one at the moment)
- There are about 12 TB available, I have just increased DataVol1 allocation from 5 to 8
- Put the Control Panel icon (the "settings gear") on the dashboard for easy access

# Shared Folders
- Shared folder can be viewed by going to Group/Control Panel/Priviledge/Shared Folders

# QFinder Pro
- You can also access things over QFinder Pro

# Remote Sysloging
- QuLog doesn't process BSD logs which is what both of my switches use
- I had to enable syslog from the Control Panel
- Added a `SysLog`s share and mapped it to DataVol1
- Can't view log changes in realtime over SMB though becasue of caching issues
- Syslog viewer sucks and filtering doesn't work
- Using `Lnav` log viewer from Windows and WSL instead
- `tail -f \\192.168.XXX.XXX\SysLogs\messages` doesn't update in real time, but the file size does (very confusing)

# QNAPclub
- Go to AppCenter, then you have to add a "store"
  - to do that, click on the gear, then the "App Repository" tab, then add a name and a url for the store
  - You can test the URL in your browser
  - Many URLs did not work -  this one did: `https://www.myqnap.org/repo.xml`

# SSH
- Enabled ssh login using "mike" from control panel - search for ssh
   - `ssh mike@192.168.XXX.XXX`
- Enabled color prompt in ~/.profile
- `tail -f /share/SysLogs/messages`