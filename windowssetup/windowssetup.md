---
title: "Windows Setup"
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

# Windows sleep troubleshooting
- Found this here: (https://www.faqforge.com/windows/how-to-see-which-application-prevents-your-pc-in-windows-10-from-entering-sleep-mode/)
- Sleep debugging: From an admin command prompt: `powercfg /requests`


# Windows keys
- `aka.ms\mykeys`

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

# Installing using a local account
- Otherwise it will give your home account a screwed up name based on your email
- (https://www.tomshardware.com/how-to/install-windows-11-without-microsoft-account)
1. Follow the Windows 11 install process until you get to the "choose a country" screen.
2. Now we want to issue a command from forcing you to have an internet connections
2a. Hit Shift + F10. A command prompt appears
3. Type OOBE\BYPASSNRO (i.e. go to the OOBE subfolder and invoke the bypassnro batch file)
3a. Computer will reboot
4. Hit Shift + F10 again. type "ipconfig /release" go disable Internet
5. Continue with installation
6. When you get to the "Let's connect you to a network" page with the big wifi symbol,
   there will be a new option"I don't have Intenet" at the bottom next to the "Next" button,
   choose that.
7. This will casuse a new option to appear on that page "Continue with limited setup"
8. A new login screen will appear with "Whos going to use this device". You can enter a username there.
9. Enter a password, but you will have to disable the "Change password on next login" option somewhere

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

## Breaking and repairing the boot loader
- Good video (https://www.youtube.com/watch?v=CZ17JrgFFhw) from CyberCPU Tech
- Need Media Creation Tool to create bootable USB stick

### Look at bcd
Spearow - 26 Dec 2023
```
C:\Users\mike>hostname
Spearow

C:\>bcdedit

Windows Boot Manager
--------------------
identifier              {bootmgr}
device                  partition=\Device\HarddiskVolume1
path                    \EFI\Microsoft\Boot\bootmgfw.efi
description             Windows Boot Manager
locale                  en-US
inherit                 {globalsettings}
flightsigning           Yes
default                 {current}
resumeobject            {190d...e4}
displayorder            {current}
toolsdisplayorder       {memdiag}
timeout                 30

Windows Boot Loader
-------------------
identifier              {current}
device                  partition=C:
path                    \WINDOWS\system32\winload.efi
description             Windows 11
locale                  en-US
inherit                 {bootloadersettings}
recoverysequence        {190d...e4-2}
displaymessageoverride  Recovery
recoveryenabled         Yes
isolatedcontext         Yes
flightsigning           Yes
allowedinmemorysettings 0x15000075
osdevice                partition=C:
systemroot              \WINDOWS
resumeobject            {190d...e4}
nx                      OptIn
bootmenupolicy          Standard
hypervisorlaunchtype    Auto
claimedtpmcounter       0x10002
```

### Backing up bcd
- Good video (https://www.youtube.com/watch?v=CZ17JrgFFhw&t=271s)
- Enter `bcdedit export c:\bcd.bak` from Admin Command Shell to backup
- Enter `bcdedit /import c:\bcd.bak` from Admin Command Shell to restore

## Breaking it
- `bcdedit /set path \win`
- `bcdedit /set recoveryenabled no`


## Fixing it
- boot to Blue "Windows, Language to Install, Time and Currency format, Keyboard or input" screen
- Just hit next to get the next screen
- "Repair your computer" instead of "Install Now"
- Then select "Troubleshoot"
- From "X:\sources" can select bcdedit and diskpart

CyberCPU sequence
```
diskpart
list disk
sel disk 0 (which ever one Windows is on)
list vol
(look for FAT32 100 MB partiation)
sel vol 1
assign letter=v
list vol (and look and see if it was assigned)
exit
v:
cd EFI
dir
cd Microsoft
dir
cd boot
dir
(look for BCD)
c:
format v: /fs:fat32
proceed (y)
No volume label
dir v: (now empty)
dir c: (should be the normal windows drive)
bcdboot c:\windows /s v: /f UEFI
"Boot file sucessfully created"
v:
(should see EFI like before, can look at boot and etc again)
close command prompt
select "Close your PC"
You will have lost recovery
``````

# Install Office
https://microsoft.sharepoint.com/sites/mywork/SitePages/Microsoft365Apps/Get-Microsoft-365-Apps.aspx