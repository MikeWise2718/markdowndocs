---
title: "Windwos SetupTemplate Titles."
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Stuff I do every time I reinstall windows.

# Restrict Files Showing up in quick access
- In Windows explorer go to the `View` Ribbon Tab, and select `Options`
- Then click on: `Change folder and search options`
- A dialog opens, there disable the `Show Recently Used Files...` checkbox in the `Privacy` tab.

# Getting a windows dump
- Open Event viewer and look for "bugcheck"

# Windows Update Tips
 - https://serverfault.com/questions/625332/windows-update-not-working-on-windows-2012-r2-standard


# Windows Evaluation Version Expiring workarounds
- An evaluation version of Windows Enterprise restarts after 90 days
- Puts off Windows sActivation Checks
- Check licensing with `slmgr.vbs /dli`\
- Detailed: `slmgr.vbs /dlv` 
- You can "rearm" it up to 3 times with `slmgr -rearm` (from an admin window)
- Expiration date `slmgr.vbs /xpr`\
- "Windows Notification Mode" means the activation deadline has passed and certain things will be turned off (customizations, auto reboot, etc.)
- 3 times 90 is 260 days, after expiration of the eval version it will start to autoboot after one hour of running
- Skip autoboot after expiry: (https://medium.com/tech-learn-share/how-to-stop-expired-windows-server-auto-shutdown-every-hour-c0cd74e0974e) 
   - Initially download PsTools
   - Create folder called — PSTOOLS on C: drive
   - Extract all the contents of the zip file in C:\ drive into the folder PSTOOLS (which we just created)
   - After that you need to start command prompt with Administrator privileges and go to PSTOOLS
   - Enter `psexec -i -d -s cmd` and click-agree on the license agreement dialog box
   - Then you will get another command prompt running under `nt authoriy\system`
   - To check this enter `whoami` and check that it is the case
   - Enter `sc delete WLMS`
   - `regedit` go to `HKLM\System\CurrentControlSet\Service\WLMS` key and delete it
   - Now reboot
   - You can control uptime by looking in task manager under CPU, it should display up time 
   - The simple way of doing it would be to open command prompt with administrator privileges and run the command `sc delete WLMS` and then delete the WLMS key from the registry. However, if this doesn’t work, you can try the above method which will work for sure..



# Things I like to install

###	General Utils
   - Chrome
   - Firefox
   - Git

###	Office
   -	Outlook, Word, Ppt, Excel, Visio
   - Greenshot
   
###	Compilers
   - VS Code
   -	Newest Visual Studio
   -	R-Studio
   - Anaconda
   -	Scala (?) - VM
   -	Octave (?) - VM
   -	Matlab (?) – VM
   -	MikTek (?)
   -	Pandoc (?)
###	Editors
   -	Notepad 2
   -	Notepad++
   -	VS Code
   -	HxD – hex editor -  https://mh-nexus.de/en/hxd/ 
###	Explorer
   -	Configure file extensions
  - Preview Config at https://chocolatey.org/packages/previewconfig 
   - See this post: https://superuser.com/questions/970951/how-can-i-get-a-file-preview-in-file-explorer-in-windows-10 
  -	Configure previews for 
     - 	Text
         - 	r,cs,csv,js,json,py
     - 	Bitmaps?
     - 	What else?

### Tray Management
 - https://www.howtogeek.com/75510/beginner-how-to-customize-and-tweak-your-system-tray-icons-in-windows-7/

## Seconds Display in Tray
- https://winaero.com/blog/taskbar-clock-show-seconds-windows-10/
- `Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced`
- Create a DWORD32 key `ShowSecondsInSystemCLock` and set it equal to 1
- Log in and log out
