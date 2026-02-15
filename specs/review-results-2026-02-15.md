# Content Review Results — 2026-02-15

Review of all ~137 topic pages for embarrassing, wrong, or sensitive content.

---

## HIGH Severity (fix immediately)

### FILE: azcli/azcli.md
- **[HIGH]** Line ~40-47: Section titled "MetLife" with client name and specific storage account names (`pvxdeveusst001`, `pvxstorageaccount001`, `vaxdecodingdata`) publicly visible. A recruiter or MetLife employee seeing this would raise eyebrows. — DELETE or heavily redact this section.
- **[MEDIUM]** Line ~108: Truncated line "enter get clone https://repsol-digital" — possible second client name leak ("repsol-digital"). — DELETE or redact.

### FILE: azuremaps/azuremaps.md (actually azuremaps/template.md)
- **[HIGH]** Lines ~56-57: Azure Maps subscription keys embedded in URLs: `IdbTbLfVZWE6B5pnqB-ybmzk5KbM_lyQeLtt_YusYNc` — API keys published in the clear. Even if expired, this is a credential leak. — EDIT to redact all key values.

### FILE: mikrotik/mikrotik.md
- **[HIGH]** Lines ~42-48: Actual password attempts listed publicly ("Toor.125", "toor.125", "Netgear1618!", "admin/password"). — DELETE these lines.
- **[MEDIUM]** Line ~40: Serial number `65FA1B50A0060` and MAC address `C8:9E:43:9A:97:88` of network equipment. — DELETE.

### FILE: nuget/nuget.md
- **[HIGH]** Line ~27, 33: Partially redacted API key `oy2dmxphhoxdtce2bxxxxxxxxxxxxxxxxxqou5ihhmljqfnj23m` — may still be recognizable/reconstructable. — Fully redact.

### FILE: powerbi/powerbi.md
- **[HIGH]** Line ~12: Password hint "pass: bpi..." alongside username and email. — DELETE the password hint.

### FILE: pip/pip.md
- **[HIGH]** Line ~15: Link points to a Business Insider article about "best microscope images" instead of anything pip-related. — DELETE the link.

### FILE: visualstudio/visualstudio.md
- **[HIGH]** Lines ~1-9: Entire page is just "Opps..." — completely empty stub. — DELETE page or add real content.

### FILE: fritzbox/fritzbox.md
- **[HIGH]** Lines ~45-46: Image "VodafoneUserData.png" may contain real ISP credentials. — Verify image content, possibly DELETE.
- **[MEDIUM]** Line ~60: Image "PhoneDaten.png" may contain real SIP phone numbers/passwords. — Verify image content.

### FILE: azuredatabricks/azuredatabricks.md
- **[HIGH]** Lines ~43-46: Databricks connect token `dapi...afe9-2` published. — DELETE the token.

---

## MEDIUM Severity — Unprofessional / Embarrassing

### Rants and editorial comments
- **azureiotedge/azureiotedge.md** Line ~70: "how stupid is this?" about Microsoft's own tooling. — EDIT.
- **gazebo/gazebo.md** Line ~8: "Don't try and compile it under windows... It is a catasrophy" — rephrase professionally.
- **gazebo/gazebo.md** Line ~98: "After about 3 hours of getting nowhere I gave up" — EDIT.
- **hololens/hololens.md** Line ~30: "wtf are they?" — EDIT.
- **jetson/jetson.md** Line ~54: "Boo hiss..." — EDIT.
- **pythononvscode/pythononvscode.md** Line ~32: "Things that kind of suck about this REPL Experience" — tone down.
- **tensorflow/tensorflow.md** Lines ~12,16: "royal pia", "pain in the butt" — EDIT.
- **ssh/ssh.md** Line ~8: "It has a frigging web site" — EDIT.
- **xamarin/xamarin.md** Line ~8: "All that is left of Microsoft's mobile strategy?" — snarky, Xamarin now retired. — EDIT.

### Wrong / misleading content
- **azure/azure.md** Line ~25: Link to a Brexit Stack Exchange question instead of Azure App Service docs — wrong URL paste. — EDIT or DELETE.
- **climatemodels/climatemodels.md** Line ~16: CESM URL points to GEOS-5 (copy-paste of wrong URL). — EDIT.
- **dotnetcore/dotnetcore.md** Line ~9: States "Current version is 2.0" — .NET Core 2.0 is from 2017, long EOL. — EDIT.
- **suttonbarto/suttonbarto.md** Line ~13: Wrong equation: "c^2 = sqrt(a^2 + b^2)" should be "c = sqrt(a^2 + b^2)". — EDIT.
- **windowssetup/windowssetup.md** Line ~167: "bcdedit export" for both backup AND restore — restore should be "bcdedit import". Factually wrong, could cause data loss. — EDIT.
- **robocopy/robocopy.md** Line ~31: "Do it" command still has /L (list-only) flag, identical to "List only". — EDIT.
- **azureubuntu/azureubuntu.md** Lines ~112-114: Script installs nvidia drivers then immediately removes them; broken `sed` command. — FLAG as dangerous.

### Client / colleague names leaked
- **azureiotedge/azureiotedge.md** Line ~274: "Audi hack" heading with `audimunichacr.azurecr.io/audi_tf_models` — client/partner name. — EDIT to redact.
- **azuredevops/azuredevops.md** Lines ~20-21: Internal team "AppliedInnovationTeam" and project "UnityDevOps". — EDIT.
- **azuredatabricks/azuredatabricks.md** Line ~41: "Simulation and Autonomous Systems" internal team name. — EDIT.
- **curobo/curobo.md** Lines ~70-79: Chat messages from "Tommy Wu (External)" pasted verbatim with timestamps. — Anonymize.
- **azureubuntu/azureubuntu.md** Line ~88: "Script that we got from Yuval Mazor" — names a colleague. — EDIT.
- **git/git.md** Line ~227: Colleague name "erhunse" with internal project names ("pyvaxdecoder", "PFH.FURS.Vaccination"). — Anonymize.
- **omniverse/omniverse.md** Line ~195: References "Paul Rance" by name. — FLAG.
- **sonoff/sonoff.md** Lines ~9, 19: "Thank you Jonathan" / "on Jonathans recommendation". — FLAG.

### Credentials / tokens still exposed
- **azcopy/azcopy.md** Lines ~24, 29: SAS tokens with signatures published. — Redact signatures.
- **azureiotedge/azureiotedge.md** Lines ~298-299: Partially shown password `IBcNH....3lvVz68`. — Fully redact.
- **jetson/jetson.md** Line ~109: IoT Hub connection string with real hub name `MikesIoThub1618` and device ID. — Redact.
- **issacsim/isaacsim.md** Line ~109: Same IoT Hub name. — Redact.
- **comfyui/comfyui.md** Line ~76: CIVITAI username "mikewise1618471". — EDIT.

### Template titles / wrong titles left in YAML
- **csharp/csharp.md** Line ~2: Title says "Template Titles". — EDIT.
- **curobo/curobo.md** Line ~2: Title says "Template Titles". — EDIT.
- **hololens/hololens.md** Line ~2: Title says "Template Titles". — EDIT.
- **python/python.md** Line ~2: Title says "Template Titles". — EDIT.
- **r-grid/r-grid.md** Line ~2: Title says "Template Titles". — EDIT.
- **smb/smb.md** Line ~2: Title says "Zero MQ" instead of "SMB". — EDIT.
- **windowssetup/windowssetup.md** Line ~2: Title says "Windwos SetupTemplate Titles." — EDIT.

### 3dsmax license evasion suggestion
- **3dsmax/3dsmax.md** Line ~10: Suggests running trial in Hyper-V to avoid paying subscription. — EDIT or DELETE.

---

## MEDIUM Severity — Stubs / Near-Empty Pages

These pages have little to no useful content and make the site look abandoned:

| File | Content |
|------|---------|
| visualstudio/visualstudio.md | Just "Opps..." |
| teams/teams.md | 3 lines, "Not sure we need this" |
| powershell/powershell.md | 2 lines |
| zeromq/zeromq.md | 3 links only |
| Pytorch/pyrtorch.md | 2 links |
| morsecode/morsecode.md | 1 link |
| netlink/netlink.md | Incomplete intro sentence |
| keras/keras.md | Broken links, near-empty |
| homeautomation/homeautomation.md | 4 links only |
| androidstudio/androidstudio.md | 1 link + template placeholder |
| maya/maya.md | Intro + empty section |
| ocr/ocr.md | 2 links |
| onnx/onnx.md | Minimal content |
| vazirani/vazirani.md | Intro paragraph + image |
| rtvs/rtvs.md | 10 lines, RTVS is discontinued |
| pip/pip.md | Wrong link, near-empty |
| gcloud/gcloud.md | 14 lines, title typo "Gloud" |
| gamearch/gamearc.md | 17 lines |
| ffmpeg/ffmpeg.md | 18 lines |
| cmake/cmake.md | Just a build sequence |
| hyperv/hyperv.md | Sparse, random Stable Diffusion section |
| imagemagick/imagemagick.md | 1 command example |
| azureflask/azureflask.md | Thin, outdated |
| cryptomining/cryptomining.md | Thin, template boilerplate |

---

## Global Issues

### "mothership.com" domain substitutions
Across many files, Microsoft domains (`docs.microsoft.com`, `azure.microsoft.com`, etc.) have been replaced with `mothership.com` variants. **Every link to Microsoft documentation is broken** for visitors. This affects dozens of files including: android, copilot, csharp, dotnetcore, hololens, linq, nuget, and many more.

### Recurring "# Something Else" template placeholders
The following files still have empty `# Something Else` sections from the original template: alphaess, bonsai, chome, citiesskylines, climatemodels, colcon, comfyui, cryptomining, factorio, gamearch, kerbal.

---

## LOW Severity — Typos (selected, not exhaustive)

| File | Typo |
|------|------|
| android/android.md | "Huaewi" → "Huawei" |
| copilot/copilot.md | "deprecitated" → "deprecated", "Amzaon" → "Amazon" |
| cryptomining/cryptomining.md | "Etherium" → "Ethereum" |
| csharp/csharp.md | "C$" → "C#" |
| cuda/cuda.md | "requirecs" → "requires", "repositornomy" → "repository" |
| gcloud/gcloud.md | Title "Gloud" → "GCloud" |
| javascript/javascript.md | "JaveScript" → "JavaScript" |
| kerbal/kerbal.md | "explanatin", "Beginingers", "sperates", "unnessary", "Lauch" |
| mapnik/mapnik.md | "extrodinarily" → "extraordinarily" |
| plotly/plotly.md | "Ploty" → "Plotly" |
| ubuntu/ubuntu.md | "Ubunut" → "Ubuntu" |
| vi/vi.md | "curors" → "cursors" |
| git/git.md | Broken front matter uses `**` instead of `---`; all URLs use `*` instead of `-` |
| docker/docker.md | "tensorvlow" → "tensorflow" |
| jetson/jetson.md | "distirubtion", "actualy", "installl", "assocoated" |
| obs/obs.md | "DaVinici" → "DaVinci" |
| sillytavern/sillytavern.md | "Olama" → "Ollama" |
| protobuf/protobuf.md | Shebang "!#/bin/bash" → "#!/bin/bash" |

(Many more minor typos exist across nearly all files — these are the most noticeable ones.)

---

## LOW Severity — Personal Info (minor, non-critical)

- Local paths with `C:\Users\mike\...` appear in many files (hwinfo, issacsim, mcp, omniverse, vscode, etc.)
- Machine names like "Uxie", "Abra", "Fearow", "Luxray" appear in various files
- Forum username "MikeWise1618" appears in hwinfo, rainmeter, plotly
- Internal project paths `/home/mike/vafsb/`, `/mass/vafsb/imcap` in bash/zeromq.md

---

## Suggested Priority

1. **Immediate**: Delete/redact HIGH items (client names, credentials, API keys)
2. **Soon**: Fix MEDIUM embarrassing content (rants, wrong info, template titles)
3. **Consider**: Delete or unlist stub pages from index
4. **Low priority**: Fix typos, clean up personal paths
5. **Investigate**: The "mothership.com" domain issue — are these intentional or broken?
