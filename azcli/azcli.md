---
title: "Azure CLI 2.0"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
 - Azure command line interface.
 - 2.0 is a rewrite in Python from Node.js - who knows why?
 - Runs on Linux nicely, freeing Azure from PowerShell dependence.
 - Docs here -  https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest
 - Scripts here - https://docs.microsoft.com/en-us/azure/batch/scripts/batch-cli-sample-run-job

# Installation
- Linux Install Instructions - https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest

# Upgrade version
- `az version`
- Check current version number here - https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest
- Upgrade on Windows
   - Just download the MSI installer under Windows from above and reinstall
- Upgrade on Linux:
   - `sudo apt-get update && sudo apt-get install --only-upgrade -y azure-cli`

# Account Commands
- `az login                               `  # Makes you go to a web page and enter an 8 digit alfanum code 
- `az account show                        `  # What account am I using
- `az account list --output table`        `  # List all the accounts you have
- `az account set -s "Account Name"       `  # Set a particular account  (did not work on Ubuntu)
- `az account set --subscription "2 - Smart Parking Solution"` # This worked on Ubutntu
- 

# Log into KHI sub
- `az login`
- `az account set --subscription 2659c0ca-a6ad-4edc-82ad-4ea8c599bd18`
- `az acr login --name edgecontainermodule`
- `sudo docker run -it --rm edgecontainermodule.azurecr.io/ros-signalr-hmi:latency`


# MetLife
```
az version
az account set -s "ProjectSomethingOrOther"
az storage account list --output table
az storage container list --account-name pvxdeveusst001 --output table
az storage blob list --container vaxdecodingdata --account-name pvxstorageaccount001 --output table
```

# What locations are there   
- `az account list --output table         `  # List azure locations

```
D:\transfer\azurecrtest>az account list --output table
Name                                  CloudName    SubscriptionId                        State    IsDefault
------------------------------------  -----------  ------------------------------------  -------  ---------
Mike Wise's XX Azure Account          AzureCloud   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  Enabled  True
Microsoft Azure Internal Consumption  AzureCloud   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  Enabled
Another Account                       AzureCloud   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  Enabled
Yet Another Account                   AzureCloud   xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  Enabled
```

# Locations
```
C:\Users\mike>"C:\Rtools\bin\date.exe"
Mon Mar 12 16:33:32 WEST 2018

C:\Users\mike>az account list-locations --output table
DisplayName            Latitude    Longitude  Name
-------------------  ----------  -----------  ------------------
East Asia               22.267      114.188   eastasia
Southeast Asia           1.283      103.833   southeastasia
Central US              41.5908     -93.6208  centralus
East US                 37.3719     -79.8164  eastus
East US 2               36.6681     -78.3889  eastus2
West US                 37.783     -122.417   westus
North Central US        41.8819     -87.6278  northcentralus
South Central US        29.4167     -98.5     southcentralus
North Europe            53.3478      -6.2597  northeurope
West Europe             52.3667       4.9     westeurope
Japan West              34.6939     135.502   japanwest
Japan East              35.68       139.77    japaneast
Brazil South           -23.55       -46.633   brazilsouth
Australia East         -33.86       151.209   australiaeast
Australia Southeast    -37.8136     144.963   australiasoutheast
South India             12.9822      80.1636  southindia
Central India           18.5822      73.9197  centralindia
West India              19.088       72.868   westindia
Canada Central          43.653      -79.383   canadacentral
Canada East             46.817      -71.217   canadaeast
UK South                50.941       -0.799   uksouth
UK West                 53.427       -3.084   ukwest
West Central US         40.89      -110.234   westcentralus
West US 2               47.233     -119.852   westus2
Korea Central           37.5665     126.978   koreacentral
Korea South             35.1796     129.076   koreasouth
France Central          46.3772       2.373   francecentral
France South            43.8345       2.1972  francesouth
```


# Clone from vsts from Linux
Go to vsts
Go to profile
Go to security
Add an access token for that machine
Copy the login token to notepad or something
go to where you want to clone it
enter "get clone https://repsol-digital
