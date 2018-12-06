---
title: "Robocopy"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Robocopy is an awesome copy command for windows - one of the few utilities that exceeds anything on Linux
- Robycopy is a directory copy command, not a file copy command - keep that in mind
- Technet - <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc733145(v=ws.10)>
- Richcopy - Gui on top <https://docs.microsoft.com/en-us/previous-versions/technet-magazine/dd547088(v=msdn.10)>
- See my github repo for experiment with this at <https://github.com/MikeWise2718/roboexper>

# Use  diff to see the difference between two directories
-  `diff --brief -r "21-AI FY19" "21-AI FY19_old"`
-  `diff -b -r "21-AI FY19" "21-AI FY19_old"`

# examples
- Using minimal switches seems to usually do the right thing - `robocopy dir1 dir2 /s /l`
- Switch `/s` means do the subdirectories
- remove the `/l` at the end to actually do it
