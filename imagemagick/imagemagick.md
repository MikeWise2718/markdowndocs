---
title: "Image Magick"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Imagemagick - (https://imagemagick.org)
 - Command line tools: (https://imagemagick.org/script/command-line-tools.php)

# Annotate white text "Version 1.0" in the lower-right corner
- `convert Splash2.png -gravity South-East -fill "#ffffff" -pointsize 30 -annotate 0  "Version 1.0" temp1.jpg`