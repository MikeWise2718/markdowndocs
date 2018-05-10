---
title: "Azure IoT Hub Stuff"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
hubba hubba.

# Concepts
- Azure Endpoints - At an abstract level this is a protocal, an internal port, and an externally visible point running over TCP
    - They are defined via Cloud Services: https://alexandrebrisebois.wordpress.com/2015/02/17/configuring-internal-endpoints-on-azure-cloud-services/ 

- IoT Endpoints - there are a lot of them: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-endpoints 
- IoT Hub Custom End Points - These are end points that serve as message sinks for IoT Hub. Currently they can only be Blob Storage, Event Hub, or Service Bus (Topics or Queues).
      - https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-endpoints 
- Hoever some services (like Stream Analytics and Azure Functions) can register to be called for every message (ASA for sure, Functions - I think so)

# Documentation

  ### Code
  
  ### Tutorials
  ### Guidance


# Configuring a storage endpoint
- Create a storage container with the desired level of access (anonymous access or not)
- Set up a custom endpoint in IoT hub pointing to that
- Set up a route in IoT hub with a sql query selecting the right messages
      - https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-query-language#get-started-with-device-to-cloud-message-routes-query-expressions
      

# Routing Rules
- You can have "custom endpoints" as an alternative to the normal "Events" endpoint
- Custom Endpoints can only currently be Event Hub, Storage End Point, or Service Bus (i.e. no ASA, no Function, etc)
- ASA can pick up events from the normal Events endpoint however. Wierd. 
            - But if you route everything somewhere else (like to storage), you will starve "Events", and thus ASA (I did this)
- Routing Rules - https://azure.microsoft.com/en-us/blog/iot-hub-message-routing-now-with-routing-on-message-body/ 

# Issues
 - Issue: Image was building but was not writing tag (ended up taged with <none> <none>>)
   - Date 2018-04-15 11:20
   - Resolution: Deleted a 3 day old image with the same tag and rebuilt - then it worked

