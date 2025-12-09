---
title: "Claude code"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Claude code
- github - https://github.com/anthropics/claude-code
- Discord - https://discord.com/invite/6PPFFzqPDZ 
- Issues - https://github.com/anthropics/claude-code/issues 


# Anthropic
- There seem to be two Antrhopic billing mechanisms, one about claude code, one about claude api
  - API - https://console.anthropic.com 
     - Login using google ID (if not cached)
     - balance - htps://https://console.anthropic.com/settings/billing
     - keys - https://console.anthropic.com/keys
  - Claude Code
     - home page- https://claude.ai
     - Login using google ID
     - Click on Accountt (should see an M with "MAX Plan" in the lower left corner)
     - Go to Usage to see how much you hav eused
     - Go to Billing to see your bills
   - ccusage
     - Program to show usage 
     - https://ccusage.com/guide/installation 
     - npx ccusage@latest
     - npx ccusage@latest monthly -s 20250601


# Google Gemini
- Page to create API key: https://aistudio.google.com/app/api-keys
   - used over chrome and it immediately regonized me and had me logged in under my gmail user

# Powershellinstallation
- `irm https://claude.ai/install.ps1 | iex`
   - "invoke rest method" - downloads it
   - `iex` executes it
   - Seems to have installed with bun, not node
   - Executable lands in `c:\users\mike\.local\bin\claude.exe`
   
- `npm install -g @anthropic-ai/claude-code`
   - needs to have npm already installed
   - seems to want the latest node 22.18.0 (LTS)
   - In Syther - "Executable" lands in `c:\users\mike\AppData\Roaming\npm\claude.cmd`
   - No longer...
   - `npm list -g --depth=0` lists top level globally installed packages
   - `npm root -g` shows where things are installed to
   - 


# Installation Methods
- There are at lesat two native, and npm
- Windows is a bit tricky and is only fully supported under WSL
- `claude doctor` will show you the installation method
- if it says unknown, it means you have a screwed up instllation

## Native Install (Windows)
   - Pros:
      - Standalone; no Node/npm setup required
      - No permission errors, fewer updates to dependencies break things
      - Works best for pure Windows users
   - Cons:
      - Manual updates (you must re-download to upgrade)
      - Slightly less integrated with Node.js developer workflow
      - Still relatively new (may lack rare advanced options)
      - Needs Chocolatey to manage dependencies at install
  - Docs: (bad) https://smartscope.blog/en/generative-ai/claude/claude-code-windows-native-installation/
    - Does not mentionion Chocolatey
    - Powwershell install line (DO NOT USE!!)
      - `Invoke-RestMethod -Uri https://gist.githubusercontent.com/bjornmage/f4b136150f6904b812c1ece49e49d12e/raw/claudecode_installer.ps1 | Invoke-Expression`
      - This repreatedly tried to do an npm install no matter what I did - so forget it.
  - Docs: (good) https://docs.claude.com/en/docs/claude-code/setup
     - Command that worrked from windows command shell (not powershell)
       - `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`
       - It does not appear to use Chocolatey (looked into the `install.cmd`)
   - Settings then is loaded from `c:\users\username\.claude\settings.json`


## ccstatline
- Need to have Node 18+ or bun installed
- test by `npx -y ccstatusline@latest`

current  `c:\users\mike\.claude\settings.json` -  11/11/2025
```
{
  "statusLine": {
    "type": "command",
    "command": "npx -y ccstatusline@latest",
    "padding": 0
  },
  "alwaysThinkingEnabled": true
}
```
- to dustomize `ccstatline` fields edit `c:\users\mike\.config\ccstatusline\settings.json`
- example:
```
{
  "version": 3,
  "lines": [
    [
      {"id": "1", "type": "model", "color": "cyan"},
      {"id": "2", "type": "separator"},
      {"id": "3", "type": "context-length", "color": "brightBlack"},
      {"id": "4", "type": "separator"},
      {"id": "5", "type": "session-clock", "color": "cyan"}
    ],
    [
      {"id": "6", "type": "current-working-dir", "color": "magenta"},
      {"id": "7", "type": "separator"},
      {"id": "8", "type": "git-worktree", "color": "magenta"},
      {"id": "9", "type": "separator"},
      {"id": "10", "type": "git-branch", "color": "magenta"},
      {"id": "11", "type": "separator"},
      {"id": "12", "type": "git-changes", "color": "yellow"}
    ],
    []
  ],
  "flexMode": "full-minus-40",
  "compactThreshold": 60,
  "colorLevel": 2,
  "inheritSeparatorColors": false,
  "globalBold": false,
  "powerline": {
    "enabled": false,
    "separators": [""],
    "separatorInvertBackground": [false],
    "startCaps": [],
    "endCaps": [],
    "autoAlign": false
  }
}
```
    

## npm Install
      - Pros:
        - Super simple for those with existing Node.js environments
        - Easy updates via npm
        - Fits smoothly into Node-based teams and Unix-based setups
      - Cons:
        - May require WSL for best experience on Windows​
        - Prone to npm or Node version conflicts, especially on multi-user or multi-project setups
        - More potential for permission problems or broken PATH entries

## Install Chcocolaty
- `https://chocolatey.org/install`
- Right-click "Windows PowerShell" and select Run as administrator.
- You should see "Administrator: Windows PowerShell" in the window title.
- Run the following script:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
- Installed `Chocolatey v2.5.1` 

## Windows Recommendation
   - For most Windows users, the `native installer` is preferred for simplicity, reliability, and no external dependencies. 
   - Use the `npm install` only if you’re already comfortable managing Node/npm versions and want the fastest possible updates or are running in WSL/Linux/macOS.
   - Both deliver nearly identical features and capabilities inside the Claude CLI itself.​

# Purging Claude
   - npm uninstall -g @anthropic-ai/claude-code
   -  remove any leftover binaries from:
      - C:\Users\<username>\AppData\Roaming\npm
      - C:\Users\<username>\.local\bin

# ccstatusline
- Repo - https://github.com/sirmalloc/ccstatusline
- Quick Start - https://github.com/sirmalloc/ccstatusline?tab=readme-ov-file#-quick-start 
   - See settings file above
   - for settings options search for "git-worktree" in actual code in repo, have found no actual docs
- %USERPROFILE%\.claude\settings.json
or
- %USERPROFILE%\.config\ccstatusline\settings.json

# Where converstaions are stored
- In `C:\Users\mike\.claude\projects\`
- same for both bun and node
- claude told me how to do this
- tested by runing `claude "test-mssage"`
- found by using procmon, then filtering on "ProcessName contains claude" and "Operation equald CreateFile"
- wrote 4000 or so entries to a csv and had claude figure out which one it was.
- results:
```
Perfect! I found it. The conversation is being saved at:

  C:\Users\mike\.claude\projects\D--csharp-test\72e590ea-0585-44e0-8ff6-c5b5e76d06a7.jsonl

  This file is opened and accessed multiple times at timestamps 5:52:51.1049873 and 5:52:51.1113691, which
  corresponds to when Claude started processing this conversation in the current working directory (D:\csharp\test).

  The naming pattern shows Claude stores conversations in:
  - Base path: C:\Users\mike\.claude\projects\
  - Project-specific folder based on the working directory (with path separators replaced by --)
  - Individual conversation files with UUID names and .jsonl extension (JSON Lines format)
```

```
● Good to know! Your conversations are safe in C:\Users\mike\.claude\projects.

  The C:/Users/mike/AppData/Roaming/Claude directory contains the Claude desktop app's runtime data (cache, session
  state, etc.), not your conversation history.

  You can safely clear the problematic session file without losing any conversations:

  rm "C:/Users/mike/AppData/Roaming/Claude/sentry/session.json"

  Or if that doesn't work, clear the entire AppData directory:

  rm -rf "C:/Users/mike/AppData/Roaming/Claude"

  This will reset Claude's runtime state and should fix the hanging issue with claude -c, while your conversations
  in C:\Users\mike\.claude\projects remain untouched.
```

# Hanging error
- claude -c --debug
```
```

# Deinstalling
## Steps for Complete Removal on Windows
1. Remove the Executable:

Delete the Claude Code binary file, usually found at:

```
%UserProfile%\.local\bin\claude.exe
```
If this location does not exist, check other folders like:

```
%UserProfile%\.local\share\claude
%UserProfile%\.local\state\claude
%UserProfile%\.cache\claude
```
and delete any claude or related subfolders.

2. Remove Configuration Files (optional for a thorough uninstall):

3. Delete configuration files and directories:
```
%UserProfile%\.claude.json
%UserProfile%\claude.json.backup
%UserProfile%\.claude\ NO....contains converstaions . save this
```

4. Clean up Environment Variables or Shortcuts (if set):

5. If you manually added Claude to your system PATH or created shortcuts, remove those entries as well.

6. Verify Removal:

Open a new terminal or PowerShell window and run:

```
claude --version
```

# Installing on Windows
- The powershell install will fall back to NPM install, don't use that.
- See the "Native Install" section above and install that way
- You should install and test ripgrep beforehand
   - https://docs.claude.com/en/docs/claude-code/troubleshooting#search-and-discovery-issues
   - Then set USE_BUILTIN_RIPGREP=0 in your environment

# TAC - Tactical Agentic Coding (Oct 2025)
- Channel IndyDevDan
- The tac course url: https://agenticengineer.com/tactical-agentic-coding/course 


## Installing TAC claude commands
- Just copy the directory `.claude/commands`
- If it doesn't read them it is probably due to RIPGREP not working, check the claude debug log for errors
   - claude -c --debug

## TAC On Windows 
- Python uses code page `cp1252` by default on Windows in Western countries for some odd reason. You will need to set an environment variable to get it to use `utf-8` by default.
   - `set PYTHONUTF8=1`
   - or `setx PYTHONUTF8=1`
   - or just put it in the settings dialog box
- Additionally you will need to add more variables to the environment filter in `adws/adw_modules/utils.py`
- These are in the  `utils.py` under the `function get_safe_subprocess_env()` around line 200
```
        # Windows-specific environment variables (needed for DLL loading)
        "SYSTEMROOT": os.getenv("SYSTEMROOT"),
        "WINDIR": os.getenv("WINDIR"),
        "TEMP": os.getenv("TEMP"),
        "TMP": os.getenv("TMP"),
        "PATHEXT": os.getenv("PATHEXT"),
        "COMSPEC": os.getenv("COMSPEC"),   
        
        # Windows user profile variables (needed for config/cache access)
        "USERPROFILE": os.getenv("USERPROFILE"),
        "USERNAME": os.getenv("USERNAME"),
        "HOMEDRIVE": os.getenv("HOMEDRIVE"),
        "HOMEPATH": os.getenv("HOMEPATH"),
        "APPDATA": os.getenv("APPDATA"),
        "LOCALAPPDATA": os.getenv("LOCALAPPDATA"),             
        
        # Python-specific variables that subprocesses might need
        "PYTHONPATH": os.getenv("PYTHONPATH"),
        "PYTHONUNBUFFERED": "1",  # Useful for subprocess output
        "PYTHONUTF8": os.getenv("PYTHONUTF8", "1"),  # Force UTF-8 encoding on Windows
```

# Context and Status line context
- Status line context (purple Ctx field at bottom) does not include the Autocompact buffer (45k tokens) does this:
  - Ex1: `Model: Sonnet 4.5 | Ctx: 97.8k | Session: 74hr 52m`
  - Ex2: `Model: Sonnet 4.5 | Ctx: 46.9k | Session: 17hr 46m`
- Top line /context output looks like this:
  - Ex1:  `claude-sonnet-4-5-20250929 · 143k/200k tokens (72%))` 
  - Ex2:  `claude-sonnet-4-5-20250929 · 91k/200k tokens (46%)`
- Auto-Compactification occurs at 200k minus 45k ac-buffer tokens, so at around 155k tokens
  - Ex1 has about  50k of context left and has used about 2/3 of what it can use
  - Ex1 has about 110k of context left and has used about 1/3 of what it can use
- Think of Ctx field as "size of prompt transmitted to the LLM"
- I don't know hey they include the model name in the top lince

<img alt="Ex1 Context image" title="Ex1" src=ContextEx1.png width=400 />
<img alt="Ex2 Context image" title="Ex2" src=ContextEx2.png width=400 />
