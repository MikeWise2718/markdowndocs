# Content Review Results — 2026-02-15

Review of all ~137 topic pages for embarrassing, wrong, or sensitive content.

---

## HIGH Severity (fix immediately) — ALL FIXED ✅

### FILE: azcli/azcli.md
- ✅ **[HIGH]** Line ~40-47: Section titled "MetLife" with client name and specific storage account names (`pvxdeveusst001`, `pvxstorageaccount001`, `vaxdecodingdata`) publicly visible. — REDACTED.
- ✅ **[MEDIUM]** Line ~108: Truncated line "enter get clone https://repsol-digital" — possible second client name leak ("repsol-digital"). — REDACTED.

### FILE: azuremaps/azuremaps.md (actually azuremaps/template.md)
- ✅ **[HIGH]** Lines ~56-57: Azure Maps subscription keys embedded in URLs. — REDACTED.

### FILE: mikrotik/mikrotik.md
- ✅ **[HIGH]** Lines ~42-48: Actual password attempts listed publicly. — DELETED.
- ✅ **[MEDIUM]** Line ~40: Serial number and MAC address of network equipment. — DELETED.

### FILE: nuget/nuget.md
- ✅ **[HIGH]** Line ~27, 33: Partially redacted API key. — FULLY REDACTED.

### FILE: powerbi/powerbi.md
- ✅ **[HIGH]** Line ~12: Password hint "pass: bpi..." alongside username and email. — DELETED.

### FILE: pip/pip.md
- ✅ **[HIGH]** Line ~15: Link points to a Business Insider article instead of anything pip-related. — PAGE DELETED.

### FILE: visualstudio/visualstudio.md
- ✅ **[HIGH]** Lines ~1-9: Entire page is just "Opps..." — FIXED with real content.

### FILE: fritzbox/fritzbox.md
- ✅ **[HIGH]** Lines ~45-46: Image "VodafoneUserData.png" may contain real ISP credentials. — REMOVED.
- ✅ **[MEDIUM]** Line ~60: Image "PhoneDaten.png" may contain real SIP phone numbers/passwords. — REMOVED.

### FILE: azuredatabricks/azuredatabricks.md
- ✅ **[HIGH]** Lines ~43-46: Databricks connect token published. — DELETED.

---

## MEDIUM Severity — Unprofessional / Embarrassing — ALL FIXED ✅

### Rants and editorial comments — ALL FIXED ✅
- ✅ **azureiotedge/azureiotedge.md** Line ~70: "how stupid is this?" — Rephrased to "not very intuitive".
- ✅ **gazebo/gazebo.md** Line ~8: "It is a catasrophy" — Rephrased professionally.
- ✅ **gazebo/gazebo.md** Line ~98: "After about 3 hours of getting nowhere I gave up" — Rephrased.
- ✅ **hololens/hololens.md** Line ~30: "wtf are they?" — Rephrased to "unclear where these are".
- ✅ **jetson/jetson.md** Line ~54: "Boo hiss..." — Rephrased.
- ✅ **pythononvscode/pythononvscode.md** Line ~32: "Things that kind of suck" — Changed to "Limitations".
- ✅ **tensorflow/tensorflow.md** Lines ~12,16: "royal pia", "pain in the butt" — Rephrased professionally.
- ✅ **ssh/ssh.md** Line ~8: "It has a frigging web site" — Rephrased.
- ✅ **xamarin/xamarin.md** Line ~8: Snarky remark — Replaced with factual note about .NET MAUI succession.

### Wrong / misleading content — ALL FIXED ✅
- ✅ **azure/azure.md** Line ~25: Brexit Stack Exchange link — Replaced with correct Azure App Service docs URL.
- ✅ **climatemodels/climatemodels.md** Line ~16: CESM URL pointed to GEOS-5 — Fixed to correct CESM/UCAR URL.
- ✅ **dotnetcore/dotnetcore.md** Line ~9: "Current version is 2.0" — Updated to note .NET 5+ succession.
- ✅ **suttonbarto/suttonbarto.md** Line ~13: Wrong equation c^2 = sqrt(...) — Fixed to c = sqrt(...).
- ✅ **windowssetup/windowssetup.md** Line ~167: bcdedit export for restore — Fixed to bcdedit /import.
- ✅ **robocopy/robocopy.md** Line ~31: "Do it" command had /L flag — Removed /L.
- ✅ **azureubuntu/azureubuntu.md** Lines ~112-114: Script removed just-installed drivers — Commented out with warning.

### Client / colleague names leaked — ALL FIXED ✅
- ✅ **azureiotedge/azureiotedge.md** Line ~274: "Audi hack" + ACR URL — Redacted to "Client project".
- ✅ **azuredevops/azuredevops.md** Lines ~20-21: "AppliedInnovationTeam" / "UnityDevOps" — Replaced with placeholders.
- ✅ **azuredatabricks/azuredatabricks.md** Line ~41: "Simulation and Autonomous Systems" — Removed.
- ✅ **curobo/curobo.md** Lines ~70-79: "Tommy Wu (External)" chat messages — Anonymized to summary.
- ✅ **azureubuntu/azureubuntu.md** Line ~88: "Yuval Mazor" — Removed.
- ✅ **git/git.md** Line ~227: "erhunse" + internal project names — Anonymized.
- ✅ **omniverse/omniverse.md** Line ~195: "Paul Rance" — Replaced with "Alternative version".
- ✅ **sonoff/sonoff.md** Lines ~9, 19: "Jonathan" references — Replaced with "colleague".

### Credentials / tokens still exposed — ALL FIXED ✅
- ✅ **azcopy/azcopy.md** Lines ~24, 29: SAS tokens — Redacted signatures.
- ✅ **azureiotedge/azureiotedge.md** Lines ~298-299: ACR password — Fully redacted.
- ✅ **jetson/jetson.md** Line ~109: IoT Hub connection string — Redacted with placeholders.
- ✅ **issacsim/isaacsim.md** Line ~109: IoT Hub name — Was already clean, no action needed.
- ✅ **comfyui/comfyui.md** Line ~76: CIVITAI username — Redacted.

### Template titles / wrong titles left in YAML — ALL FIXED ✅
- ✅ **csharp/csharp.md** — Changed to "C#".
- ✅ **curobo/curobo.md** — Changed to "CuRobo".
- ✅ **hololens/hololens.md** — Changed to "HoloLens".
- ✅ **python/python.md** — Changed to "Python".
- ✅ **r-grid/r-grid.md** — Changed to "R Grid".
- ✅ **smb/smb.md** — Changed from "Zero MQ" to "SMB".
- ✅ **windowssetup/windowssetup.md** — Changed to "Windows Setup".

### 3dsmax license evasion suggestion — FIXED ✅
- ✅ **3dsmax/3dsmax.md** Line ~10: License evasion suggestion — Replaced with neutral "trial edition is available for evaluation".

---

## MEDIUM Severity — Stubs / Near-Empty Pages — PARTIALLY ADDRESSED

| File | Content | Status |
|------|---------|--------|
| visualstudio/visualstudio.md | Just "Opps..." | ✅ Fixed (HIGH fix added content) |
| teams/teams.md | 3 lines, "Not sure we need this" | ✅ PAGE DELETED |
| powershell/powershell.md | 2 lines | Not addressed |
| zeromq/zeromq.md | 3 links only | Not addressed |
| Pytorch/pyrtorch.md | 2 links | Not addressed |
| morsecode/morsecode.md | 1 link | Not addressed |
| netlink/netlink.md | Incomplete intro sentence | ✅ PAGE DELETED |
| keras/keras.md | Broken links, near-empty | Not addressed |
| homeautomation/homeautomation.md | 4 links only | Not addressed |
| androidstudio/androidstudio.md | 1 link + template placeholder | Not addressed |
| maya/maya.md | Intro + empty section | Not addressed |
| ocr/ocr.md | 2 links | Not addressed |
| onnx/onnx.md | Minimal content | Not addressed |
| vazirani/vazirani.md | Intro paragraph + image | Not addressed |
| rtvs/rtvs.md | 10 lines, RTVS is discontinued | Not addressed |
| pip/pip.md | Wrong link, near-empty | ✅ PAGE DELETED |
| gcloud/gcloud.md | 14 lines, title typo "Gloud" | ✅ Title fixed to "GCloud" |
| gamearch/gamearc.md | 17 lines | Not addressed |
| ffmpeg/ffmpeg.md | 18 lines | Not addressed |
| cmake/cmake.md | Just a build sequence | Not addressed |
| hyperv/hyperv.md | Sparse, random Stable Diffusion section | Not addressed |
| imagemagick/imagemagick.md | 1 command example | Not addressed |
| azureflask/azureflask.md | Thin, outdated | ✅ PAGE DELETED |
| cryptomining/cryptomining.md | Thin, template boilerplate | ✅ PAGE DELETED |

---

## Global Issues — PARTIALLY ADDRESSED

### "mothership.com" domain substitutions — FIXED ✅
~~Across many files, Microsoft domains (`docs.microsoft.com`, `azure.microsoft.com`, etc.) have been replaced with `mothership.com` variants.~~ Fixed: 106 broken URLs restored to correct `microsoft.com` equivalents across 26 files. Email addresses (`@mothership.com`) and `onmothership.com` references left as intentional redactions of internal Microsoft info.

### Recurring "# Something Else" template placeholders
The following files still have empty `# Something Else` sections from the original template: alphaess, bonsai, chome, citiesskylines, climatemodels, colcon, comfyui, ~~cryptomining~~, factorio, gamearch, kerbal.

---

## LOW Severity — Typos (selected, not exhaustive) — ALL LISTED TYPOS FIXED ✅

| File | Typo | Status |
|------|------|--------|
| android/android.md | "Huaewi" → "Huawei" | ✅ |
| copilot/copilot.md | "deprecitated" → "deprecated", "Amzaon" → "Amazon" | ✅ |
| cryptomining/cryptomining.md | "Etherium" → "Ethereum" | ✅ (page later deleted) |
| csharp/csharp.md | "C$" → "C#" | ✅ |
| cuda/cuda.md | "requirecs" → "requires", "repositornomy" → "repository" | ✅ |
| gcloud/gcloud.md | Title "Gloud" → "GCloud" | ✅ |
| javascript/javascript.md | "JaveScript" → "JavaScript" | ✅ |
| kerbal/kerbal.md | "explanatin", "Beginingers", "sperates", "unnessary", "Lauch" | ✅ |
| mapnik/mapnik.md | "extrodinarily" → "extraordinarily" | ✅ |
| plotly/plotly.md | "Ploty" → "Plotly" | ✅ |
| ubuntu/ubuntu.md | "Ubunut" → "Ubuntu" | ✅ |
| vi/vi.md | "curors" → "cursors" | ✅ |
| git/git.md | Broken front matter `**` → `---`; URLs `*` → `-` | ✅ |
| docker/docker.md | "tensorvlow" → "tensorflow" | ✅ |
| jetson/jetson.md | "distirubtion", "actualy", "installl", "assocoated" | ✅ |
| obs/obs.md | "DaVinici" → "DaVinci" | ✅ |
| sillytavern/sillytavern.md | "Olama" → "Ollama" | ✅ |
| protobuf/protobuf.md | Shebang "!#/bin/bash" → "#!/bin/bash" | ✅ |

---

## LOW Severity — Personal Info (minor, non-critical) — PARTIALLY FIXED

- Local paths with `C:\Users\mike\...` appear in many files — **Not addressed** (embedded in command examples, low value to change)
- Machine names like "Uxie", "Abra", "Fearow", "Luxray" — ✅ **Fixed in prose** (azure, curobo, wsl, tinkerpop); `mike@Abra` prompts left in terminal transcripts
- Forum username "MikeWise1618" — ✅ **Fixed** in hwinfo, powerbi, rainmeter
- Internal project paths `/home/mike/vafsb/`, `/mass/vafsb/imcap` — ✅ **Fixed** in bash/zeromq.md

---

## Suggested Priority

1. ✅ ~~**Immediate**: Delete/redact HIGH items (client names, credentials, API keys)~~
2. ✅ ~~**Soon**: Fix MEDIUM embarrassing content (rants, wrong info, template titles)~~
3. **Consider**: Delete or unlist remaining stub pages from index
4. ✅ ~~**Low priority**: Fix typos, clean up personal paths~~
5. **Investigate**: The "mothership.com" domain issue — are these intentional or broken?
