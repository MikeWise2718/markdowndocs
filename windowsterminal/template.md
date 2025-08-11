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
- `set PROMPT=$E[1;35m$P$G$E[1;37m` (pruple)
- `set PROMPT=$E[1;36m$P$G$E[1;37m` (cyan)
- `set PROMPT=$E[1;33m$P$G$E[1;37m` (yellow)
- Needs background color set to dark blue
- To make permanent, add it as an environment variable (PROMPT)

With background and time:
```
color 1
PROMPT=$E[1;35m$T$H $P$G$E[1;37m
```

```
0     Turn Off Attributes
1     High Intensity
2     Normal Intensity
4     Underline (mono only)
5     Blink
7     Reverse Video
8     Invisible
30    Black
31    Red
32    Green
33    Yellow
34    Blue
35    Magenta
36    Cyan
37    White
40    Black
41    Red
42    Green
43    Yellow
44    Blue
45    Magenta
46    Cyan
47    White
```