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
   - Took like 10 minutes to fetch all 1074 objects - 5.3 GB, 7.9 MB/s
- `git lfs push --all https://AppliedInnovationTeam@dev.azure.com/AppliedInnovationTeam/UnityDevOps/_git/CampSim`
- Failed with 37 LFS Server timeout errors:


- Adjusted timeouts according to this: (https://github.com/git-lfs/git-lfs/issues/2636)
  - `git config lfs.activitytimeout 120`
  - `git config lfs.dialtimeout 120`
  - Reduced errors to 3 Client Errors (413 request too large)
  - Solution here: (https://developercommunity.visualstudio.com/content/problem/862165/cant-push-large-git-lfs-files-to-repository-from-p.html?inRegister=true)
 
- Finally fixed it with this
  - `git config http.version HTTP/1.1`
  - `git lfs push --all https://AppliedInnovationTeam@dev.azure.com/AppliedInnovationTeam/UnityDevOps/_git/CampSim`
  - `Uploading LFS objects: 100% (1074/1074), 5.3 GB | 4.2 MB/s, done.` in about 3 minutes
   