---
title: "Windows Terminal"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Should have been called winterm
- Github repo: (https://github.com/microsoft/terminal)
- To get to JSON - Drop Down/Settings/JSon Settings (at bottom)

# Prompt info
- Color for Prompt: https://stackoverflow.com/questions/6297072/color-for-the-prompt-just-the-prompt-proper-in-cmd-exe-and-powershell


# Oh My Posh
- https://ohmyposh.dev/



# Best so far
- `set PROMPT=$E[1;35m$P$G$E[1;37m`
- Needs background color set to dark blue

With background and time:
```
color 1
PROMPT=$E[1;35m$T$H $P$G$E[1;37m
```