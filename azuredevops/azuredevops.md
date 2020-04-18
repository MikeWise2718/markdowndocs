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
- Followed these steps (https://docs.microsoft.com/en-us/azure/devops/repos/git/import-git-repository?
view=azure-devops)
- `git clone --bare https://github.com/mikewise2718/campsim.git`
- `git config user.email "mike.wise@microsoft.com"`
- `git config user.name mike-wise`
- `git config user.password XXXXXXX`
-  Created repo at `https://dev.azure.com/AppliedInnovationTeam/UnityDevOps/_git/CampSim`
-  `git push --mirror https://AppliedInnovationTeam@dev.azure.com/AppliedInnovationTeam/UnityDevOps/_git/CampSim`
-    oddly it didn't dual auth me?
- `git lfs fetch origin --all`
-   Took like 10 minutes to fetch all 1074 objects
- `git lfs push --all https://AppliedInnovationTeam@dev.azure.com/AppliedInnovationTeam/UnityDevOps/_git/CampSim`


