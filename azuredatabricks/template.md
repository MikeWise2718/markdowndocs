---
title: "Azure Databricks"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Azure Databricks (ADB) - main Microsoft page here: (https://azure.microsoft.com/en-us/services/databricks/)
- Decent tutorial here: (https://jcbaey.com/azure-databricks-hands-on?utm_source=medium&utm_campaign=db-hands-on)
  - Includes how to use normal ADB storge and Azure DL Gen2 
  - Shows how to configure secrets
  - Part 2 - advanced, but not step-by-step (https://jcbaey.com/getting-started-on-databricks-with-python-examples)

# Delta Lake
- Delta Lake on Databricks - (https://databricks.com/discover/getting-started-with-delta-lake-tech-talks/making-apache-spark-better-with-delta-lake)


# Lamda, Kappa, and Delta Architectures in Databricks
- Databricks Delta - (https://jixjia.com/delta-architecture/)
- CAP Theeorem - (https://en.wikipedia.org/wiki/CAP_theorem) 
- Lambda - How to beat CAP - (http://nathanmarz.com/blog/how-to-beat-the-cap-theorem.html)
  - retains input data unchanged
- Kappa - Questioning Lambda - (https://www.oreilly.com/radar/questioning-the-lambda-architecture/)
- Delta 


#  Data Wrangling
- Data Wrangling with PySpark for Data Scientists Who Know Pandas - Andrew Ray (https://www.youtube.com/watch?v=XrpSRCwISdk)


# Databrick Connect
- Docs - (https://docs.databricks.com/dev-tools/databricks-connect.html#:~:text=Download%20and%20unpack%20the%20open,%2Flocal%2Flib%2Fpython3.)
- Includes how to set up with VS Code and Miniconda

# Secret Scopes  
- Secret Scopes - (https://docs.microsoft.com/en-us/azure/databricks/security/secrets/secret-scopes)

# ADB CLI - Command line interface
- Docs - (https://docs.databricks.com/dev-tools/cli/index.html)
- There is a python based command line databricks CLI 
  - `pip install databricks-cli`
- Azure install and configuration: (https://docs.microsoft.com/en-us/azure/databricks/dev-tools/cli/)

## ADB CLI Authentication
- Two types of auth: ADB Personal Access Tokens (more convenient) or AAD Tokens (more secure)

### ADB Personal Access Tokens 
- docs(https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/authentication)
- created in DataBricks under user setting (click on person icon in the upper right to get menu link)
- Example configuration of ADB CLI and then a test command - note the token didn't get echoed when I pasted it:
```
PS /home/mike> databricks configure --token
Databricks Host (should begin with https://): https://adb-1013519808979862.2.azuredatabricks.net
Token:
PS /home/mike> more ~/.databrickscfg
[DEFAULT]
host = https://adb-1013519808979862.2.azuredatabricks.net
token = da.......df

PS /home/mike> databricks secrets list-scopes
Scope                  Backend         KeyVault URL
---------------------  --------------  ------------------------------------------
blobaccess-primarykey  AZURE_KEYVAULT  https://testdatabricks-kv.vault.azure.net/
testdb-secret-scope    AZURE_KEYVAULT  https://testdatabricks-kv.vault.azure.net/
PS /home/mike>
```

### AAD Tokens 
- docs(https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/aad/)

