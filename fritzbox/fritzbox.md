---
title: "FritzBox"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
A ubiquitous router - in Germany at least.

# Inital Setup in your Local Network
1. The initial challenge is that you can't configure the FritzBox network settings without a network connetion to it. Chicken and Egg problem. 
    * In the past I have succedded with adding a network address that can talk to the FB default (192.168.178.1 or 169.254.1.1), but this does not always work for whatever reason.
    * so it is easist to set it up by connection to its Wifi because then there is no problem figuring out the IP address.
    * the FB default Wifi config information is usually printed on the box.
2. After you can get a web setup page  connection with http://frtiz.box (if you have DNS) or directly with http://168.254.1.1 <br>
3. Next you will need to specify a password for login. Don't forget to remember it somehow (write it down?).<br>
4. The next thing is to enable the advanced menu settings by clicking on the top right menu like this:<br> ![advanced menu pic](EnableAdvancedMenu.png).<br>
5. Then you want to go to Heimnetz/SomethingOrOther and set the IP address you want it to have in your network (like 192.168.12.1).<br>
![set ip4 addr pic](SetIp4Address.png).<br>
- Which then opens to this:<br>
![set ip4 addr pic1](SetIp4Address1.png).<br>

6. Note that in the above I also setup DHCP so that other devices would be serviced by this router.

7. Now you can wire it up to your LAN with a cable and you should be able to get to the setup with http://192.168.12.1 <br>


# Backup
- Definitely worthwhile making a backup
- Instructions from this video: (Austausch einer FritzBox!) (a 7490) : (https://www.youtube.com/watch?v=cdfbdjdY6B8)
    - 1. Just login 
    - 2. then go to the poitn "System/Sichering"
    - 3. Select the "Sicherung" tab
    - 4. Add a password then it will download to a file
    - 5. Sample name: `FRITZ.Box 7490 113.07.21_13.02.21_1616.export`
- To restore
    - 3. Select the "Wiederherstellen" tab
    - 4. Select your backup and upload the file
    - 5. Select whether or not all services be restored or just selected ones
    - 6. enter password

- Can be restored to another FritzBox - not sure if the model can change, but probably

# DSL
- Here is a section from the PDF letter with my signing data from Vodafone with my user data:<br>
![vodafone user data](VodafoneUserData.png).<br>

- I simply had to add my username and password - like this:<br> ![this](ZugangsDaten.png).<br>



# Name
- Don't forget to switch to advanced mode
- Name can be set in the menu Heimnets/Fritz!Box-Name blade

# ISDN Phones
Turns out I didn't have an ISDN phone line anymore, I have only Internet telephony from Vodafone. Took me awhile to realize this.

- The sip numbers and their passwords from Vodafone looked like this:<br>
![vodafone user data](PhoneDaten.png).<br>

- I had to enter these numbers inwith the FritzBox and the FritzBox had to register them with my provider (mVodafone). For my provider (Vodafone DSL) I only had to add the numbers and the password, becasuse it knew the pattern that vodafone uses:<br>
![vodafone sip registration](SipNumberRegistration.png).<br>

- Looks like this now:<br>![vodafone sip registration](SipNumbersActive.png).<br>

- Getting the wiring right was complicated. I need to use some kind of an adapter.

# Language
* Apparently the 7490 German edition does not have a language setting
* https://en.avm.de/service/fritzbox/fritzbox-7490/knowledge-base/publication/show/428_Selecting-the-menu-language-on-your-FRITZ-Fon/
* https://www.facebook.com/fritzboxinternational/posts/662292577180496



# DNS
- Static addresses - you need to do two things
        - Tell it to always respond to a DHCP address with a fixed IP4 address under the details in the `Netwerk` entry for that device
        - Enter it as an exception in the `DNS-Rebind-Shutz` box
        - Details here: https://blog.lobraun.de/2015/05/03/static-ips-and-dns-names-for-devices-in-your-home-network/
- Doesn't seem to work like that though
    - Ping `abra` from `uxie` give me an `192.168.25.187` (the wireless interface)
    - Ping `abra.fritz.box` from `uxie` give me an `192.168.25.187` (the wireless interface)
    - What's going on?
    - Have to investigate with some tool (nslookup?)
    - https://serverfault.com/questions/41064/whats-the-command-line-utility-in-windows-to-do-a-reverse-dns-look-up/352556



# Mesh Mode
- You can set up Mesh mode under the menu point "Mesh"
- There in the tab "Mesheinstellungen" you determine (at the bottom) what gets propagated over from the mesh master
<br>![Mesheinstellungen](MeshSettings.png).<br>


# Phones in mesh mode
- (https://en.avm.de/service/knowledge-base/dok/FRITZ-Box-7490/3412_Setting-up-telephony-on-the-Mesh-Repeater/)
- You have to set up to have everything propagated in the "Mesheinstellungen" (Mesh Settings) otherwise you can't enable it number propagation
- You then have to enable it in the Mesh Phone Settings
- This is what it looks like after enablement - the menu selection at the bottom is confusing...
<br>![MeshPhoneSettings](MeshPhoneSettings.png).<br>

# Wifi
To do


# GUDE Power