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
