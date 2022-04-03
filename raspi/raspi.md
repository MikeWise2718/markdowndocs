---
title: "Raspberry Pi"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Raspberry Pi or Raspi home page: (https://www.raspberrypi.org/)
- Getting started with Canakit: (https://www.canakit.com/quick-start/pi)
- Raspberry Pi OS (previously called Raspbian) is the official supported operating system.
- NOOBS or Raspi Imager: (https://www.raspberrypi.com/software/) 
- I chose to use a Raspi image to save time over the docker which I would have prefered

# Wifi
- Configuring Wifi from the Home Assistant (https://community.home-assistant.io/t/guide-connecting-pi-with-home-assistant-os-to-wifi-or-other-networking-changes/98768)
- FOr some reason my Raspi with the Home Assistent image was not seeing 5 GHz bands on the wifi even though it should have as far as I can tell
- I couldn't find an `nmcli` command to fix this ()
- Also my PC Laptop was refusing to budge from the 5 Ghz channel for its Mobile Hotspot channel - even when I selected it- I eventually had to go to the wif device in Device Manager and specify 2.5 GHz only in the Advanced Settings - options are highly card/wifi-chip specific
- Related link:(https://www.windowsdigitals.com/how-to-change-5ghz-to-2-4ghz-in-windows-10/)
- You can see what wifi channel your card is using with an Android App (Wifi Analyzer)


# Supervisor Tab
- Never found a supervisor tab and maybe it is gone in thsi version
- Screen shots indicate it should be a seperate entry above the "Developer" entry in the left-hand menu but it never appeared even after I enabled "Advanced Usage" in my profile
- Also I installed from the OS Image so it should have been there
- Seems I have all the functionality though? Really not sure

# HACS
- Googling indicated the easist way to integrate with Govee temperature devices was with something installed with HACS
- (https://austinsnerdythings.com/2021/12/27/using-the-govee-bluetooth-thermometer-with-home-assistant-python-and-mqtt/)
- HACS Installation (https://hacs.xyz/)
- Installtion and Configuration of HACS is quite complicated and required a hard restart of the whole server before it appeared in the AddOns menu - browser refresh or ha restart from the UI were not sufficient.
