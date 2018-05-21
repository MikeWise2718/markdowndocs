---
title: "Zero MQ"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
* Smaba on Ubuntu - https://help.ubuntu.com/community/How%20to%20Create%20a%20Network%20Share%20Via%20Samba%20Via%20CLI%20%28Command-line%20interface/Linux%20Terminal%29%20-%20Uncomplicated,%20Simple%20and%20Brief%20Way!

# Smb debugging
* Get the versions of everthing - `dpkg-query -W -f='${Package} ${Version} ${Source} ${Status}\n' | grep samb`
* Test a share - `smbclient //192.168.25.12/object_detection` (doesn't work SMB2 minversion?)
    - 
    - https://forums.freenas.org/index.php?threads/whats-recommended-to-avoid-issues-with-minimum-smb-version-in-services-config.54033/https://blogs.technet.microsoft.com/josebda/2013/10/02/windows-server-2012-r2-which-version-of-the-smb-protocol-smb-1-0-smb-2-0-smb-2-1-smb-3-0-or-smb-3-02-are-you-using/
* config is in - 
* Ubuntu config is in - `/etc/samba/smb.conf` 
* Ubuntu logs are in - `/var/logs/samba` 

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

