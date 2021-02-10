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

# PySpark
- Really based on PySpark
- API Docs: (https://spark.apache.org/docs/latest/api/python/index.html)


# Delta Lake
- Delta Lake on Databricks - (https://databricks.com/discover/getting-started-with-delta-lake-tech-talks/making-apache-spark-better-with-delta-lake)


# Lamda, Kappa, and Delta Architectures in Databricks
- Databricks Delta - (https://jixjia.com/delta-architecture/)
- CAP Theeorem - (https://en.wikipedia.org/wiki/CAP_theorem) 
- Lambda - How to beat CAP - (http://nathanmarz.com/blog/how-to-beat-the-cap-theorem.html)
  - retains input data unchanged
  - Nathan Marz GOTO 2012 presentation - (https://www.youtube.com/watch?v=ucHjyb6jv08)
- Kappa - Questioning Lambda - (https://www.oreilly.com/radar/questioning-the-lambda-architecture/)
- Delta - Beyond Lambda: Introducing Delta Architecture - (https://www.youtube.com/watch?v=FePv0lro0z8)


#  Data Wrangling
- Data Wrangling with PySpark for Data Scientists Who Know Pandas - Andrew Ray (https://www.youtube.com/watch?v=XrpSRCwISdk)


# Databrick Connect
- Docs - (https://docs.databricks.com/dev-tools/databricks-connect.html#:~:text=Download%20and%20unpack%20the%20open,%2Flocal%2Flib%2Fpython3.)
- As of 9-Feb-2021 using Python 3.7 and Cluster Runtime 7.5
- `pip install -U databricks-connect==7.3.*`, note 7.5 was not available
- Databricks instance: WeDataBricksTest in WestEurope - Simulation and Autonomous Systems
    - Need to collect these:
    - URL: https://adb-3181657523121670.10.azuredatabricks.net
    - Cluster ID: 0208-163407-lapse941
    - databricks-connect-token dapi489a396c389a7f0687f5d9649926afe9-2
    - orgid: 3181657523121670
    - port: 15001
- Includes how to set up with VS Code and Miniconda
- Install JRE 8
  - Install JRE  8 without logging into Oracle: (https://www.java.com/en/download/)
- Install winutils - (https://stackoverflow.com/questions/50637728/pyspark-failed-to-locate-the-winutils-binary-in-the-hadoop-binary-path)
   - Copied downloaded `bin` and `something` into a `d:\python\winutils`
   - Added `HADOOP_HOME=d:\python\winutils` to environment
   - Restarted command shell
- `databricks-connect test`
    - to get around mismatched client/server use `set DEBUG_IGNORE_VERSION_MISMATCH=1` as error message says
Successful Test:
```
(databricks) D:\python\databricks>set DEBUG_IGNORE_VERSION_MISMATCH=1

(databricks) D:\python\databricks>databricks-connect test
* PySpark is installed at c:\users\mike\anaconda3\envs\databricks\lib\site-packages\pyspark
* Checking SPARK_HOME
* Checking java version
java version "1.8.0_281"
Java(TM) SE Runtime Environment (build 1.8.0_281-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.281-b09, mixed mode)
* Skipping scala command test on Windows
* Testing python command
21/02/10 18:49:37 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
21/02/10 18:49:38 WARN MetricsSystem: Using default name SparkStatusTracker for source because neither spark.metrics.namespace nor spark.app.id is set.
View job details at https://adb-3181657523121670.10.azuredatabricks.net/?o=3181657523121670#/setting/clusters/0208-163407-lapse941/sparkUi
* Simple PySpark test passed                                       (0 + 8) / 48]
* Testing dbutils.fs
[FileInfo(path='dbfs:/databricks-datasets/', name='databricks-datasets/', size=0), FileInfo(path='dbfs:/databricks-results/', name='databricks-results/', size=0), FileInfo(path='dbfs:/tmp/', name='tmp/', size=0)]
* Simple dbutils test passed
* All tests passed.

(databricks) D:\python\databricks>SUCCESS: The process with PID 37472 (child process of PID 45400) has been terminated.
SUCCESS: The process with PID 45400 (child process of PID 25228) has been terminated.
SUCCESS: The process with PID 25228 (child process of PID 25596) has been terminated.
```

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

