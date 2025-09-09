---
title: "Claude code"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Claude code

# Powershellinstallation
- `irm https://claude.ai/install.ps1 | iex`
   - "invoke rest method" - downloads it
   - `iex` executes it
   - Seems to have installed with bun, not node
   - Executable lands in `c:\users\mike\.local\bin\claude.exe`
- `npm install -g @anthropic-ai/claude-code`
   - needs to have npm already installed
   - seems to want the latest node 22.18.0 (LTS)
   - "Executable" lands in `c:\users\mike\AppData\Roaming\npm\claude.cmd`


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

