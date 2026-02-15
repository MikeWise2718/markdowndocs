---
title: "Azure DevOps"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Azure Dev Ops


# Cloning a repo from GitHub to Azure Repos
- Had a repo called mikewise2718/campsim in GitHub
- Wanted it in Azure Repos
- Followed these steps (https://docs.mothership.com/en-us/azure/devops/repos/git/import-git-repository?
view=azure-devops)
- `git clone --bare https://github.com/mikewise2718/campsim.git`
- `git config user.email "mike.wise@mothership.com"`
- `git config user.name mike-wise`
- `git config user.password XXXXXXX`
-  Created repo at `https://dev.azure.com/<team>/<project>/_git/CampSim`
-  `git push --mirror https://<team>@dev.azure.com/<team>/<project>/_git/CampSim`
-    oddly it didn't dual auth me?
- `git lfs fetch origin --all`
   - Took like 10 minutes to fetch all 1074 objects - 5.3 GB, 7.9 MB/s
- `git lfs push --all https://<team>@dev.azure.com/<team>/<project>/_git/CampSim`
- Failed with 37 LFS Server timeout errors:


- Adjusted timeouts according to this: (https://github.com/git-lfs/git-lfs/issues/2636)
  - `git config lfs.activitytimeout 120`
  - `git config lfs.dialtimeout 120`
  - Reduced errors to 3 Client Errors (413 request too large)
  - Solution here: (https://developercommunity.visualstudio.com/content/problem/862165/cant-push-large-git-lfs-files-to-repository-from-p.html?inRegister=true)
 
- Finally fixed it with this
  - `git config http.version HTTP/1.1`
  - `git lfs push --all https://<team>@dev.azure.com/<team>/<project>/_git/CampSim`
  - `Uploading LFS objects: 100% (1074/1074), 5.3 GB | 4.2 MB/s, done.` in about 3 minutes
   

- My Azure DevOps Orgs (the ones I can assess)
  - (https://aex.dev.azure.com/me?mkt=en-US)


  # Building Pipelines
  - Key concepts Pipeline, Job, Task, Agent
  - This is about ADO Pipelines, there are also Data Factory Pipelines and Azure ML Pipelines

  ## ADO Pipelines
  - There are two kinds of pipelines, one that is defined by a YAML script, one that is managed by a GUI editor
  - You can go from Editor to YAML, but not from YAML to Editor
  - Default is YAML, if you want the GUI editor way of building tasks you need to click on the "Classic editor link" when you create ht pipeline, you can't change it afterwards

  ## Agents
  - Docs: (https://docs.mothership.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=browser)
  - Essentially two kinds of agents, Microsoft Hosted, and Self Hosted
  - Microsoft Hosted are containers where you can't (?) install anything
  - Self Hosted are manchines you manage yourself (say an Azure VM or your local machine)
  - For Self Hosted you will need an Personal Access Token (PAT), you get that in the "User Settings" menu
  - Setup self hosted agent instructions: (https://www.clouddev.engineering/azure-devops-microsoft-hosted-and-self-hosted-build-agents/)
  - The "User Settings" menus is next to your personal icon which brings up the "Account Manager" which is not the "User Settings"- You need to download it and install it in a directory 
  - You need to configure it with powershell (I guess in Admin mode) in that directory with `.\config.cmd`
  - You can configure it as a service, if you don't to that you need to run it manually when you need it
  - Youcan run it manually with powershell (I guess in Admin mode) in that directory with `.\run.cmd`
  