---
title: "Zero MQ"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
* Smaba on Ubuntu - https://help.ubuntu.com/community/How%20to%20Create%20a%20Network%20Share%20Via%20Samba%20Via%20CLI%20%28Command-line%20interface/Linux%20Terminal%29%20-%20Uncomplicated,%20Simple%20and%20Brief%20Way!

# Basic share
* see my ubuntu question for cd /a sample write up
* create a share directory (`/media/transfer`) with mask 755 and owner being the user (`mike` in this example)
* config is in `/etc/samba/smb.conf`
* don't forget to set an extra SMB password with `sudo smbpasswd -a mike`
* restart with `sudo service smbd restart`
* map a drive from the Windows command line with `net use u: \\192.168.25.12\transfer /user:mike pass`
* delete that map with `net use u: /delete`
* sample smb entry:
```
[transfer]
   comment = file transfer share
   path = /media/transfer
   writable = yes
   browsable = yes
   valid users = mike
   read only = no
```

# Issues
* My Ubunut question - https://askubuntu.com/questions/1014558/samba-share-cant-serve-win-10-since-fall-creator-update-system-error-1272

