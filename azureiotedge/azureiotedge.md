---
title: "Azure IoT Edge Stuff"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Living close to the edge.

# Documentation

  ### Code
  - API Docs: https://docs.microsoft.com/en-us/dotnet/api/microsoft.azure.devices.client?view=azure-dotnet 
  - GitHub C# API Code and Docs: https://github.com/Azure/azure-iot-sdk-csharp 
  ### Tutorials
  - Simulate Linux Device Tutorial - https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-simulate-device-linux
  - C# Module Tutorial - https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-csharp-module
  ### Guidance
  - Deploying via Azure CLI 2.0 - https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-create-deployment-with-cli-iot-extension
  - Deployment Manifests - https://docs.microsoft.com/en-us/azure/iot-edge/module-composition
  - Temp Sensor Code - https://github.com/Azure/iot-edge/tree/master/v2/samples/azureiotedge-simulated-temperature-sensor 
  - Troubleshooting: - https://docs.microsoft.com/en-us/azure/iot-edge/troubleshoot 
  - A device is controled with the python `iotedgectl` utility
      - some docs are here - https://pypi.python.org/pypi/azure-iot-edge-runtime-ctl
  - Important things you do with `iotedgectl`
     - Enroll your device with your Azure IoT Edge instance so you can start `edgeAgent`
     - Start and stop the `edgeAgent`
     - Register the docker registry credentials that `edgeAgent` needs to pull docker images
     - `iotedgectl` parameters are stored in `/etc/azure-iot-edge/config.json`

# How tos from a remote build machine
  - List devices - this works better than the device-identity command which fails whey you are out of messages
```  
C:\Users\mike>az iot device list --hub-name MikesIoThub1618 --output table
This command is deprecating and will be removed in future releases. Use 'az iot hub device-identity list (via IoT Extension)' instead.
ConnectionState    ConnectionStateUpdatedTime    DeviceId                  GenerationId  LastActivityTime     Status    StatusUpdatedTime
-----------------  ----------------------------  ------------------  ------------------  -------------------  --------  -------------------
Disconnected       0001-01-01T00:00:00           joltik-l4t-aarch64  636573115187857662  0001-01-01T00:00:00  enabled   0001-01-01T00:00:00
Disconnected       0001-01-01T00:00:00           abra-ubu-x86        636573076267454124  0001-01-01T00:00:00  enabled   0001-01-01T00:00:00
```
  - Deleting a device
     - Just delete the device out of the device list on the IoT Edge portal
     - Then delete the associated running and exited dockers (for the "Simulated Linux Device Tutorial" there were 3 of them)
     - `az delete device` (apparently depreciated)
  - Create a module from source code
     - Notes
        - This is documented in the C# Module tutorial above in a rather verbose fashion
        - it is easiest to use VS Code with its built in commands
        - but you can figure out what is happening by looking at the powershell output
     - Install Azure IoT Edge Extentsion in VS Code
     - Update the AzureIoTEdgeModule template 
        - `dotnet new -i Microsoft.Azure.IoT.Edge.Module` 
     - Now generate a new module project with:         
        - `dotnet new aziotedgemodule -n FilterModule`
     - Use VS Code to make your code edits adding your real biz logic (see above tutorial link)
        - it will ask to add missing assets to your project (not sure what these were)
        
     - compile by right clicking on the `.csproj` file
     - build the docker by right-clicking on the docker file in the right sub-directory
        - you will be asked to brows to the `publish` subdirectory (how stupid is this?)
        - you will be asked to name the image - you will need to put the name of the targe repository in the first part of the name (I think this is required)
     - Now login to your repository and push the docker image
        - `az acr login --name mikescontainers`
        - `docker push mikescontainers.azurecr.io/faketempsensor:latest`
     - Enroll a device named `abratemp` from the device
        - `iotedgectl setup --connection-string "HostName=MikesIoThub1618.azure-devices.net;DeviceId=abratemp;SharedAccessKey=XX...XXX==" --auto-cert-gen-force-no-passwords`
     - Register credentials so the edgeAgent can pull docker images from your repository
        - `iotedgectl login --address mikescontainers.azurecr.io --username MikesContainers --password xxxxxx`        
  - Pushing a container from VS Code
    - When you create the container, you should name (tag) it with the full name it will have when you push it to the container regsistry
      - in the example below the container registry is `mikescontainers` and the docker tag is `mikescontainers.azurecr.io/filtermodule:latest`
      - You can change a local image name with the tag command `docker tag localname mikescontainers.azurecr.io/filtermodule:latest`
    - Then from the command line windows you need to do
      - `az acr login --name mikescontainers`
      - `docker push mikescontainers.azurecr.io/filtermodule:latest`

# How tos on an Edge device you are deploying to
 - Install the IoT edge runtime - basically, install pip (for python) and then use pip to install the runtime
    - `sudo apt-get install python-pip`
    - `sudo pip install update`
    - `sudo pip install azure-iot-edge-runtime-ctl`

    - Latest docker edgeAgent: https://hub.docker.com/r/microsoft/azureiotedge-hub/tags/
    - Latest docker edgeHub: https://hub.docker.com/r/microsoft/azureiotedge-hub/tags/
    - To update (assuming you are ok with gat `1.0-preview`- otherwise change it here and in the config below):
        - `iotedgectl stop`
        - `sudo pip install azure-iot-edge-runtime-ctl -update`
        - `docker pull microsoft/azureiotedge-agent:1.0-preview`
        - `docker pull microsoft/azureiotedge-hub:1.0-prevew`
        - `iotedgectl start`
    - Config in: `/etc/azure-iot-ege/config.json`

 ### Troubleshooting docs
 - Here: https://docs.microsoft.com/en-us/azure/iot-edge/troubleshoot 

 ### Enroll device with the hub

 - First create the device on the hub
   - Can use the Azure Web Interface
   - From Azure CLI - but note you don't actually need to install this on the device, `iotedgectl` does everything you really need except create the device on Azure, which you can do elsewhere.
     - Login to Azure
     - `az login`
         - Make sure you have the right account with  `az account show` 
         - if not use `az account list --output table` to find the right one
         - and set it with `az account set xxxx`
     - Now use the following command to create the device on the hub
        - `az iot hub device-identity create --device-id edge001 -hub-name MikesIoThub1618 --edge-enabled`
   - This actually enrolls it - provided the device exists in azure      
       - `sudo iotedgectl setup --connection-string "HostName=MikesIoThub1618.azure-devices.net;DeviceId=edge001;SharedAccessKey=xxxxSharedAccessKeyxxxx" --auto-cert-gen-force-no-passwords`
       - Use the `device connection string` obtained by clicking on the device in the Azure IotEdge UI - not the primary key found under `Shared Access Keys` (SAK<br>
       ![devconstr](DeviceConnectionString.png)<br>

### Edge Device client debugging and maintenance
  - You may need to change the `edgeAgent` docker image that is downloaded depending on your architecture
    - configuration is in `/etc/azure-iot-ege/config.json`
    - For example to specify ARM use `"edgeRuntimeImage": "microsoft/azureiotedge-agent:1.0.0-preview021-linux-arm32v7",`
  - Let the device know the credentials it needs to pull docker images
      - `sudo iotedgectl login --address mikescontainers.azurecr.io --username MikesContainers --password xxx-PrimaryKey-xxxx`
      - You need to enable Azure Container Repository UI to allows you to use the repository name as the user - it is not enabled by default.<br>
          ![azconregpass](AzureContainerRegistryPassword.png)<br>
      - If the `edgeAgent` is running it will then stop and restart - probably the `edgeHub` too
  - Start the `edgeAgent` on the edge client
      - `sudo iotedgectl start`
  - Stop the `edgeAgent` on the edge client
      - `sudo iotedgectl stop`
  - Kill a running instance of the `edgeAgent` on the edge client
    - `docker rm -f edgeAgent`
    - You will have to restart it manually
  - Kill a running instance of the `edgeHub`  on the edge client
    - `docker rm -f edgeHub`
    - if the `edgeAgent` is up it will restart the `edgeHub` now immediately (if the current deployment indicates that it should)
  - Kill one of your modules`
    - `docker rm -f mymodule`
    - if the `edgeAgent` is up it will restart the `mymodule` now immediately (if the current deployment indicates that it should)
  - Troubleshoot
    - Figure out what is running
      - `docker ps -a`
    - Look at the docker logs
      - `docker logs edgeAgent`
      - `docker logs edgeHub`
      - `docker logs mycontainer`


# Base images
- Audi hack
    - most things based off `FROM microsoft/dotnet:2.0.0-runtime-stretch`
    - ml based off `FROM  audimunichacr.azurecr.io/audi_tf_models`
 - New style
    - FROM microsoft/dotnet:2.0-sdk AS build-env
    - FROM microsoft/dotnet:2.0-runtime

# Issues
 - Issue: Image was building but was not writing tag (ended up taged with <none> <none>>)
   - Date 2018-04-15 11:20
   - Resolution: Deleted a 3 day old image with the same tag and rebuilt - then it worked

 - Issue: Docker run Image gets error msg:`Did you mean to run dotnet SDK commands? Please install dotnet SDK from:`
   - Date 2018-04-15 11:30
   - Resolution: dll name `h-camcap.dll` was incorrectly specified in Docker build file as `ENTRYPOINT ["dotnet", "h_camcap.dll"]`
   - Resolution2: Files were not in the build exe copy directory, so they were not being copied - so the ENTRYPOINT could not find them

 - Issue: On Windows Docker run Image gets `Unhandled Exception: System.InvalidOperationException: Missing path to certificate file.`
   - Date 2018-04-15 11:40
   - Resolution: None yet - running on Ubuntu box instead

 
 - Issue: iotedgectl somehow could not pull the images, although I could locally
   - Date 2018-04-15 12:07 
   - Resolution:  `sudo iotedgectl login --address vafsb.azurecr.io --username vafsb --password IBcNH....3lvVz68`
   - Notes: `az acr login --name vafsb` and `docker login vafsb.azurecr.io -u vafsb -p IBcNH...v68` were not enough
     - Even the the `sudo iotedgect` variant did not work at first - probably because I had `iotedgectl` stopped. 
     - When I did it while it was running, it worked
     - Afterwards this registry data should be in the `/etc/azure.../config.json` file so you will only need to do it onces
   - Complete Error Message:
 ```
2018-04-15 10:07:47.841 +00:00 [ERR] - Step failed in deployment 10, continuing execution. Failure when running command Command Group: (
  [docker pull vafsb.azurecr.io/h-camcap:latest-amd64]
  [docker create --name h-camcap vafsb.azurecr.io/h-camcap:latest-amd64]
  [docker start h-camcap]
)
2018-04-15 10:07:47.841 +00:00 [INF] - Plan execution ended for deployment 10
2018-04-15 10:07:47.841 +00:00 [ERR] - Edge agent plan execution failed.
System.AggregateException: One or more errors occurred. (Docker API responded with status code=InternalServerError, image=vafsb.azurecr.io/h-camcap, tag=latest-amd64. Check container registry (possible authorization failure or container registry down).) ---> Microsoft.Azure.Devices.Edge.Agent.Docker.InternalServerErrorException: Docker API responded with status code=InternalServerError, image=vafsb.azurecr.io/h-camcap, tag=latest-amd64. Check container registry (possible authorization failure or container registry down). ---> Docker.DotNet.DockerApiException: Docker API responded with status code=InternalServerError, response=
   at Docker.DotNet.DockerClient.HandleIfErrorResponse(HttpStatusCode statusCode, String responseBody, IEnumerable`1 handlers)
 ```


- Issue: Docker was not pulling the latest images
   - Date 2018-04-17 12:30
   - Resolution: I was entering the wrong name on the docker pull command  (h-objdet instead of h-camcap ... I think...)

- Issue: After getting h-camcap and h-objdet working, I tried to setup a shared library so they could share definitions of the communication objects. That did not work
   - Date 2018-04-18 17:00
   - Resolution: Still working on it, but I think I have to make sure I have no conficts and rebuild the shared library project from the correct .Net Core template.
```
Time Elapsed 00:00:02.17
PS D:\transfer\vafsb\h-mod\h-objdet> dotnet publish
Microsoft (R) Build Engine version 15.5.179.9764 for .NET Core
Copyright (C) Microsoft Corporation. All rights reserved.

  Restore completed in 15.3 ms for D:\transfer\vafsb\h-mod\h-common\h-common.csproj.
  Restore completed in 63.73 ms for D:\transfer\vafsb\h-mod\h-objdet\h-objdet.csproj.
  h-common -> D:\transfer\vafsb\h-mod\h-common\bin\Debug\netstandard2.0\h-common.dll
  h-objdet -> D:\transfer\vafsb\h-mod\h-objdet\bin\Debug\netcoreapp2.0\h-objdet.dll
  h-objdet -> D:\transfer\vafsb\h-mod\h-objdet\bin\Debug\netcoreapp2.0\publish\
PS D:\transfer\vafsb\h-mod\h-objdet> docker build --rm -f "d:\transfer\vafsb\h-mod\h-objdet\Dockerfile.amd64" -t vafsb.azurecr.io/h-objdet:latest-amd64 "d:\transfer\vafsb\h-mod\h-objdet"
Sending build context to Docker daemon  10.85MB
Step 1/10 : FROM microsoft/dotnet:2.0-sdk AS build-env
 ---> 2e537f28e47b
Step 2/10 : WORKDIR /app
 ---> Using cache
 ---> 31122610aea5
Step 3/10 : COPY *.csproj ./
 ---> Using cache
 ---> 1a0ab7f05c5b
Step 4/10 : RUN dotnet restore
 ---> Using cache
 ---> c730cdeb6000
Step 5/10 : COPY . ./
 ---> Using cache
 ---> 153f8a62546c
Step 6/10 : RUN dotnet publish -c Release -o out
 ---> Running in 66cd7047773e
Microsoft (R) Build Engine version 15.6.84.34536 for .NET Core
Copyright (C) Microsoft Corporation. All rights reserved.

/usr/share/dotnet/sdk/2.1.104/NuGet.targets(895,5): warning MSB3202: The project file "/h-common/h-common.csproj" was not found. [/app/h-objdet.csproj]
/usr/share/dotnet/sdk/2.1.104/NuGet.targets(986,5): warning MSB3202: The project file "/h-common/h-common.csproj" was not found. [/app/h-objdet.csproj]
  Restoring packages for /app/h-objdet.csproj...
  Generating MSBuild file /app/obj/h-objdet.csproj.nuget.g.props.
  Generating MSBuild file /app/obj/h-objdet.csproj.nuget.g.targets.
  Restore completed in 655.05 ms for /app/h-objdet.csproj.
/usr/share/dotnet/sdk/2.1.104/Microsoft.Common.CurrentVersion.targets(1823,5): warning : The referenced project '../h-common/h-common.csproj' does not exist. [/app/h-objdet.csproj]
Program.cs(17,11): error CS0246: The type or namespace name 'vafsb' could not be found (are you missing a using directive or an assembly reference?) [/app/h-objdet.csproj]
Score.cs(18,11): error CS0246: The type or namespace name 'vafsb' could not be found (are you missing a using directive or an assembly reference?) [/app/h-objdet.csproj]
Score.cs(20,9): error CS0246: The type or namespace name 'AudiBatchFrame' could not be found (are you missing a using directive or an assembly reference?) [/app/h-objdet.csproj]
Score.cs(37,16): error CS0246: The type or namespace name 'AudiBatchFrame' could not be found (are you missing a using directive or an assembly reference?) [/app/h-objdet.csproj]
The command '/bin/sh -c dotnet publish -c Release -o out' returned a non-zero code: 1
```