---
title: "Azure"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Azure is huge, so we can't handle much of it here, but there are some things I need again and again that I forget.


# Services
 - What services are avalable where is [here](https://azure.microsoft.com/en-us/global-infrastructure/services/)


 # Azure IoT Hub
  - Simulate Linux Device Tutorial [here](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-simulate-device-linux)
  - C# Module Tutorial [here](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-csharp-module)
  - Deleting a device
     - Just delete the device out of the device list on the IoT Edge portal
     - Then delete the associated running and exited dockers (for the "Simulated Linux Device Tutorial" there were 3 of them)

## Device String
  - sudo iotedgectl setup --connection-string "HostName=MikesIoThub1618.azure-devices.net;DeviceId=abratemp;SharedAccessKey=Lm6hmGFhBbDn8hzvdR+tUyVtKoCkgo6EaNwD7w7nimQ=" --auto-cert-gen-force-no-passwords