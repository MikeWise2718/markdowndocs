---
title: "Azure DSVM"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Azure Data Science VM
- Web Page: (https://azure.mothership.com/en-us/services/virtual-machines/data-science-virtual-machines/)
- Three kinds, Windows, Ubuntu, CentOS
- Diff between Ubuntu and CentOS: (https://stackoverflow.com/questions/49964685/azure-what-is-the-difference-between-dsvm-on-centos-vs-ubuntu)

# Starting a remote run on an DSVM
- Request Just-In-Time access to the box
- Login: `ssh mike@23.98.150.186`
- Start a detachable session (persistent screen) `screen` then return after the startup text
   - you can check it with `screen -r` now
- Activate the right Python Environment `source activate py36`
- Go to the directory: `cd ~/UnityProjects/ml_agents_modded`
- Start the script: `./run02`

run01:
```
#!/bin/bash
mlagents-learn config/trainer_config.yaml --train --run-id=dsvmrun01 --env=~/UnityProjects/m_agents_modded/UnitySDK/PMLbuild/rlsimple01.x86_64
```
# Putty
- Can also login with Putty, but don't get colors OOTB