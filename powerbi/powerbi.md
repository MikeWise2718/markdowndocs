---
title: "PowerBI"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Power BI - it could be better...
- My site: https://msit.powerbi.com/groups/me/contentlist

# Overview 
- It is all about licnsening: https://www.encorebusiness.com/blog/power-bi-free-vs-pro-vs-premium/
- REST API Limitations: https://msdn.microsoft.com/en-us/library/dn950053.aspx
- Embedded complications: https://www.encorebusiness.com/blog/power-bi-free-vs-pro-vs-premium/


# Settings
- They are under Gear/Settings:<br>
![gears](gearsettings.png)

# License type
- What kind of License do I have? http://community.powerbi.com/t5/Service/Power-BI-Pro-how-to-tell/td-p/186195
- It is under Gear/Manage Personal Settings<br>
- According to this Picture I am a "Pro User" - so I can use the REST API:<br>
![gears](ManagePersonalSettings.png)

# Streaming Real-time data
- Go to the PBI web thing (https://msit.powerbi.com/groups/me/contentlist/ )
- Create a new dashboard (+Create in the upper right corner)
- Add a tile (+ Add tile in menu)
- Click on "Custom Streaming Data" then next
- Add streaming data set

# Authentication
- PowerBI and Swagger - Doesn't really work - https://community.powerbi.com/t5/Report-Server/Swagger-URL-for-PBI-Report-Server/td-p/295076
- PushData to 


# Issues
- 403 (Not Autorized) - This can mean a bad token, or you haven't given your app the right permissiosn
- 404 (URL not found) - you used the wrong URL somehow
- 400 (Bad Request) - I got this trying to use a Guid (which is not a valid datatype I suppose, but I also got it when I didn't have matching brackets, etc)