---
title: "MikroTik CRS Switch"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Fullname - MikroTik Cloud Router Switch CRS5125-24G-1S-RM
- Details 10/100/1000 Ethernet ports	24

# Original
- Doing this retroactively - 2017 was 8 or 9 years ago (it is now17.11.2025)
- Default signin is Admin/(blank) 
- Changed it to be the same as my main router password 
- Assigned a static IP 192.168.25.3 - seemingly the gateway is 192.168.25.2 (which is wrong)
- Can be configured over `Winbox` (works with only a mac address), or `webfig` (web configuration)
- RouterOS was 6.39.1
- See screenshots for more

# Winbox
- For Mikrotik only
- Download from site and run from Downloads (seeminly no install)
- Hit connect button - should connect to router if the mac address is right

# Upgradced to RouterOS 7 16 Nov 2025
- Upgraded to RouterOS 7.20.4
- Automatic upgrade didn't work due to DNS failure (probably too old)
- Downloaded ntk and uploaded to router and rebooted
- Switch failed to route and failed to respond to http (webfig)
- ultimate reason was the swith IP was assigned to Port1 (the master port) only, and I was wired to Port10. WHen I changed it in the interface list it worked
- Not sure routing works still (seems to be not working as I couldn't just plug my windows box into it)

# Lessons learned
- Log into switch beforehand and screenshot everything
- Locate docs for initializing router from scratch including default user and password


# Netgear GS724TPP Switch
- IP Address  192.168.25.171
- Serial Number  65FA1B50A0060
- MAC Address  C8:9E:43:9A:97:88
Password tries:
- Toor.125
- toor.125
- toor.25
- Netgear1618!
- admin/password
- admin/1234
https://kb.netgear.com/1148/What-are-the-default-user-interface-passwords-for-NETGEAR-devices
Password recovery
https://kb.netgear.com/app/answers/detail/a_id/8903

