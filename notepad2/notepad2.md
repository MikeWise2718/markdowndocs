---Had
title: "Notepad2"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Link: (https://www.flos-freeware.ch/notepad2.html)

# Replacing Notepad
There are a couple of ways to do this
- Just copy over the notepad.exe (but it is protected and probably will freak out virus protection like Defender and get overwritten in big Windows updates)
- Some wierd registry trick - but requires a patched version: https://www.flos-freeware.ch/doc/notepad2-Replacement.html
- Just make sure its path is in front of `/windows/system32`. 
    - check the path by entering path on the cmd line
    - change it by editing the path in the System Environment Variables (windows-key Enviornment)
    - I currently have it in `d:/ut`


# In Context Menu
- https://www.howtogeek.com/howto/windows-vista/add-open-with-notepad-to-the-context-menu-for-all-files/
   - Added a key "Open with Notepad2" under HKEY_CLASSES_ROOT
   - Added a key under that "command" with "d:/ut/notepad2.exe %1"
   - Used back-slashes in the path above, not fore-slashes

