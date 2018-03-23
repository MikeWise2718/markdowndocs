---
title: "Azure IoT Edge Stuff"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Living close to the edge.

# Documentation
  - Simulate Linux Device Tutorial [here](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-simulate-device-linux)
  - C# Module Tutorial [here](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-csharp-module)
  - Deploying via Azure CLI 2.0 [here](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-create-deployment-with-cli-iot-extension)
  - Deployment Manifests [here](https://docs.microsoft.com/en-us/azure/iot-edge/module-composition)


# How tos
  - Deleting a device
     - Just delete the device out of the device list on the IoT Edge portal
     - Then delete the associated running and exited dockers (for the "Simulated Linux Device Tutorial" there were 3 of them)
  - Create a module 
     - Notes
        - This is documented in the C# Module tutorial above in a rather verbose fashion
        - it is easiest to use VS Code with its built in commands
        - but you can figure out what is happening by looking at the powershell output
     - Install Azure IoT Edge Extentsion in VS Code
     - Update the AzureIoTEdgeModule template and generate a new module project with: 
        - `dotnet new -i Microsoft.Azure.IoT.Edge.Module` 
        - `dotnet new aziotedgemodule -n FilterModule`
     - Make your code edits adding your real biz logic
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

