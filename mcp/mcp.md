---
title: "MCP"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- MCP is the way to give ChatBots access to programs. It is quite dangerous.
- Good elementry YT on how to install: (https://www.youtube.com/watch?app=desktop&v=DfWHX7kszQI)


# General Claude Code MCP commands
- `claude mcp hepp`
- `claude mcp list`
- `claude mcp add --scope user|project|local <name> -- <command> <arg1> ... <argn>`
- if you leave off scope, the scope is local
- `claude remove <name>`
- `claude mcp get <name>`


# Unity
- There are quite a few MCP Servers
- Using this one: `https://github.com/CoplayDev/unity-mcp`
- Open Pakcage Manager
   - In main menu select `Windows/Package Management/Package Manager`
   - Hit Plus sign (+) in the top left.
   - Select "Install from git url"
   - Use this url: `https://github.com/CoplayDev/unity-mcp.git?path=/UnityMcpBridge`
   - Copy and paste repo URL into text box
   - Return, it should install
   - For errors see messages in the console window
- Will be listed under "Packages - Coplay" if top icon selected, in front of "Packages - Unity"
- Should see UnityMCP under Window
- Old
    - `claude mcp add --scope user Unity-MCP -- uv run --directory C:\Users\mike\AppData\Local\Programs\UnityMCP\UnityMcpServer\src server.py`
- CosplayDev 3.1
    - `claude mcp add unity-mcp -- uv run --directory C:\Users\mike\AppData\Local\Programs\UnityMCP\UnityMcpServer\src server.py`


## Problems and fixes
- Wasn't connecting when I got back from Houston 5 Sept 2025
- Took an hour to fix 
- Ran and coonected when I ran directly from the command line, but claude reprted "could't connect"
  - Used the same command copy and pasted from the `claude mcp list`
- Not sure of fix - did the following things
  - Upgrade the Unity package (using the upgrade button in Unity Package Manager)
  - Upgraded Claude from 1.0.75 to 1.0.104 (using `claude upgrade`)
  - Tried the "Autoconnect button" from the UnityMCP menu dialog 
    - That seemed to configure a `unity-mcp` MCP entry that didn't work but then my `UnityMCP` entry did work after that
    - so deleted the `unity-mcp` 
    - Said it worked but Claude couldn't read console logs using the MCP - vexing
    - I think once I hit "Play" - that caused something to change that made claude able to read the logs


# Sketchup
- Repo: (https://github.com/mhyrr/sketchup-mcp)
- Installed repo.
- tried `uvx build` - don't remember if it worked
- Need to install rbz file
    - Reddit thread on rbz - https://www.reddit.com/r/mcp/comments/1jc21gr/sketchupmcp_connects_sketchup_to_claude_ai/ 
    - downloaded rbz from dropbox, but I could have built it
- I think `uvx --from build pyproject-build.exe` is what worked 
- claude command to install sketchup-mcp - `claude mcp add sketchup-mcp -- uvx sketchup-mcp`

# Blender
- Repo: (https://github.com/ahujasid/blender-mcp)
- Set cwd to `blender-mcp`
- `uv build`
- Install addon into Blender
   - `Preferences/Addons/` 
   - click on little down arrow in the upper right
   - `Install from disk`
   - navigagte to `blender-mcp` dir and select `addon.py`
- Add to Claude Code
   - from `blender-mcp` directory
   - `claude mcp add blender-mcp -- uvx blender-mcp`
   - `claude mcp add blender-mcp -- uvx d:\python\blender-mcp\blender-mcp`


# Campsim
- `claude mcp add  campsim -- C:\Users\mike\miniconda3\Scripts\uv.exe run --directory ./mcp-bridge python -m src.campsim_mcp_server`