---
title: "Flask On Azure"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Flask is a lightweight framework for web apps in Python
- How to organize - there are various thigns but this is good: <http://exploreflask.com/en/latest/organizing.html>

# Deplyiung on Azure
- Followed this: <https://code.visualstudio.com/docs/python/tutorial-deploy-app-service-on-linux>
- App Services on Linux is currently in preview (Apr 2019) so some stuff is broken/not implemented
- Boils down to following (after install Azure Extensions)
   - Create Web App using VS Code underr Azure Extesnsion - left click - Create New App
   - Set the deployment source by right clicking on newly defined Web App
   - Go to portal, finde Web App and add settings.txt under Application Settings (Classic)/Runtime/Startup File
   - Now back to VS Code, right click and deploy

