---
title: "Omniverse Cloud (OVC)"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Nvidia's Omniverse

# Docs
- OVC - https://www.nvidia.com/en-us/omniverse/cloud/
- NGC - https://www.nvidia.com/en-us/gpu-cloud/
- KitApp Template - https://github.com/NVIDIA-Omniverse/kit-app-template
- Tutorial - https://docs.omniverse.nvidia.com/kit/docs/kit-app-template/latest/docs/intro.html

- KAT 105.1 howto - https://docs.omniverse.nvidia.com/kit/docs/kit-app-template/105.1/app_from_scratch.html
- OVC packaging it: `https://docs.omniverse.nvidia.com/kit/docs/kit-app-template/105.1/packaging_app.html`
- OVC containerizing - `https://docs.omniverse.nvidia.com/ovc/latest/developing_for_ovc/containerizing_val.html`cd sf
- OVC uploading - `https://docs.omniverse.nvidia.com/ovc/latest/developing_for_ovc/uploading_pub.html`


# NGC Login
- Link: (https://org.ngc.nvidia.com/)
- Service is confusing opening screen is "getting started stuff"

## Dashboard
- To get to dashboard
   - Scroll down and find "CLI" tile
   - CLick on "Download" link in that tile
   - Or something similar until the dashboard comes up

NGC Dashboard - not always easy to find

<img alt="Red Fish" src=images/NgcDashboard.png width=400 title="NGC Dashboard" />

- Service keys can be found from dashboard - but they are not identity keys

## Personal Keys
- To generate a personal identity key
   - Click on user name in the upper right
   - In the dropdown click "Setup"
   - Click on "Generate Personal Key"

- To see everyone else's personal identity keys
   - Click on Users
   - Click on your name
   - Click on "Personal Keys" tab

Personal Key Setup

<img alt="Red Fish" src=images/NgcPersonalKeysSetup.png width=400 title="NGC Personal Keys" />

<br>

Generating a Key

<img alt="Red Fish" src=images/NgcGeneratePersonalKey.png width=400 title="NGC Generate Personal Key" />


- To get to uploaded containers
   - There should be a dropdown in the upper-left next to NVIDIA
   - In dropdown click on "Private Registry"
   - Select "Containers" in menu on left
   - Should get tiles showing uploaded containers

Container Tiles

<img alt="Red Fish" src=images/NgcContainerTiles.png width=400 title="NGC Container Tiles" />

<br>
Container info

<img alt="Red Fish" src=images/NgcContainerInfo.png width=400 title="NGC Container Tiles" />


# Nvidia Enterprise Support Portal
- Link: https://enterprise-support.nvidia.com
- Login with email
- Click on Enterprise Support

<img alt="Red Fish" src=images/NvidiaEnterpriseSupportPortalHome.png width=400 title="NGC Personal Keys" />



## View Cases
- Click on "View All" to the right of "Your recent cases"
- Click on filter
   - On left activate Filter
   - Filter on "Case Owner"
   - Select radio button "My Cases"

<img alt="Red Fish" src=images/EspYourRecentCases.png width=400 title="NGC Personal Keys" />


## Making a New case
   - Upload container
   - Create New Case
      - Title "Deploy Container App"
      - Description:
         - "NGC Private Registry"
         - (link to container)
         - Application Name: Sf4ovc-106-5
         - Version: 1.0
         - Don't bother with icon - it isn't supported yet
         - After submit select Omniverse Cloud CSP entitlement
   - Entitlement: Search for Omniverse and choose "MDF-NVIDIA Omniverse Cloud CSP Marketplace Annual Subscription, Upfront"

My Cases

<img alt="Red Fish" src=images/Cases.png width=600 title="Cases" />

 Existing case:

<img alt="Existing Case" src=images/PortalExistingCase.png width=600 title="Cases" />

 New case for submission:

<img alt="New Case for submission" src=images/PortalCoontainerDeploymentCaseSubmission.png width=600 title="Cases" />



##  OVC Overview
Procedure:
- Install Kit 105.1
- make an extension template `./repo.sh template new` (to make a new extension)
- build `./repo.sh build`
- see what it builds - these are defined in `premake5.lua`
    - `ls ./_build/linux-x86_64/release/*.sh`
- run it `./_build/linux-x86_64/release/my_name.my_app.sh`
- trim excess builds from `premake5.lua`
- fat package it `./repo.sh package`

## Making a Kit App (106.3)
   - Following docs at: (https://docs.omniverse.nvidia.com/kit/docs/kit-app-template/latest/docs/kit_sdk_overview.html#hands-on-exploration)
   - And email at:
 ### Making the Kit App
   - `git clone https://github.com/NVIDIA-Omniverse/kit-app-template.git sf4ovc-106-3`
   - `./repo.sh template new`
       + name is `msft.sphereflake22`
       + display name is `Sphereflake22`
       + version is `1.0.1`
   - `./repo.sh build`
       + Downloaded a bunch of stuff and took 87 seconds to build
   - `./repo.sh launch -d`
       + Launched in developer mode
       + Enabled extension `omni.kit.collaboration.channel_manager`
       + Exited app
   - Added `sphereflake22` to the newly created `_build/linux_x.../release/exts`folder
       + `cd release/exts`
       - `git clone https://github.com/mikewise2718/sphereflake22`

   - Copy over missing extensions
      - Find your extension (uiapp in this example)
         - Ubunutu:
            - Split a new command window
            - `cd /home/mike/.local/share/ov`
            - `grep -Rl . --include=extension.toml | grep channel_manager`
            - `cp -r /home/mike/.local/share/ov/data/exts/v2/omni.kit.collaboration.channel_manager-94f61211f9293654 .`
            - `grep -Rl . --include=extension.toml | grep uiapp`
            - `cp -r /home/mike/.local/share/ov/data/exts/v2/omni.kit.uiapp-ea4f8b19a20e8f6a .`
         - Windows:
            - Open a new command window
            - `cd C:\Users\mwise\AppData\Local\ov`
            - `grep -rl . --include=extension.toml | grep uiapp`
         - big R follows softlinks and takes a lot longer in Windows for some reason
      `cp -r /home/mike/.local/share/ov/data/Kit/msft.sphereflake22/1.0/exts/3/omni.kit.collaboration.channel_manager-1.0.12+0d669cdf .`
      `cp -r /home/mike/.local/share/ov/data/Kit/msft.sphereflake22/1.0/exts/3/omni.kit.uiapp-0.0.0+0d669cdf .`


   - kit files are in ./source/apps
   - Modified the `[dependencies]` in the kit streaming app (actually did it to both kit apps)
       +   `"sphereflake22" = {}`
       +   `"omni.kit.collaboration.channel_manager" = {}`
   - Tested
       + `./repo.sh launch`

### Packaging the Kit App
-`./repo.sh package --container --name sf4ovc-106-3:0.1`
- `./repo.sh launch --container --name sf4ovc-106-3:0.1`
- if the repo package tpp; is still broken
   - copy over repo_tools.toml from a working version
   - replace the repoman subdir where all the tools are
   - note that package changed (a new file had been added) so I had to copy the package.py over localpack.py
- then use localpack

- select the kit option that has the streaming enabled

- start it and test

- to test need to use the webviewer
   - github repo at `https://github.com/NVIDIA-Omniverse/web-viewer-sample`
   - `cd apps/web_viewer_sample`
   - `npm run dev`

- Then run it
   - `./repo.sh launch --container`
   - it will ask you which container to run, make sure it is the one built with the streaming option

### Uploading the container to OVC
   - Login to the IAI Dev sub and start vm_nucleus
   - connect the to the `vnet-ovc` VPN with the Azure VPN Client
   - should get a list of uploaded containers you can start
   - now go to the box you built it on
   - `docker login nvcr.io`
   - "Username: $oauthtoken"
   - "Password: < Insert private key here >"
   - Identity Private key comes from somewhere in the NGC site
   - in the following 05...72 is my org id,retrieved from my NGC profile
   - `docker tag sf4ovc-106-3r:latest nvcr.io/0509407381744272/sf4ovc-106-3r:1.0`
   - `docker push nvcr.io/0509407381744272/sf4ovc-106-3r:1.0`

### Streaming
- This changes a lot
- Apparently obsolete - works up to Kit version 105 - does not work with 106 and above
   - https://docs.omniverse.nvidia.com/extensions/latest/ext_livestream/webrtc.html
- Designed for kit template and version 106:
   - https://github.com/NVIDIA-Omniverse/web-viewer-sample
   - requires Node.js installation (https://nodejs.org/en/download)
   - Windows
   ```
   # installs fnm (Fast Node Manager)
   `winget install Schniz.fnm`
   # configure fnm environment

   fnm env --use-on-cd | Out-String | Invoke-Expression
   # download and install Node.js
   `fnm use --install-if-missing 20`

   # verifies the right Node.js version is in the environment
   `node -v` # should print v20.18.0

   # verifies the right npm version is in the environment
   `npm -v` # should print 10.8.2
   ```
   - Linux
   ```
   # installs fnm (Fast Node Manager)
   curl -fsSL https://fnm.vercel.app/install | bash

   # activate fnm
   source ~/.bashrc

   # download and install Node.js
   fnm use --install-if-missing 20

   # verifies the right Node.js version is in the environment
   node -v # should print `v20.18.0`

   # verifies the right npm version is in the environment
   npm -v # should print `10.8.2`
   ```
   - Activate with `source ~.bashrc` this should have the `eval "``fnm env``"` command in it
   - Compile with `npm install`
   - Run with `npm run dev`

# Versions

- Isaac Sim 2023.1.0-hotfix.1 (2023.1.0-rc.42) uses Kit 105.1 and Client Library 2.38.7
- Isaac Sim 2023.1.1-rc.8 uses Kit 105.1.2 and Client Library 2.38.12
- Isaac Sim 4.0.0-rc.21 uses Kit 106.0.0 and Client Library 2.47.1
- Isaac Sim 4.1.0-rc.7 uses Kit 106.0.1 and Client Library 2.49.0
- Isaac Sim 4.2.0-rc.17 uses Kit 106.1.0 and Client Library 2.49.2
