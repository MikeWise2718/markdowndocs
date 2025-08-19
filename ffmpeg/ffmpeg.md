---
title: "ffmpeg"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Command line manipulation of mpg and other things - https://ffmpeg.org/


# Install
- Easist way:
   - `winget install Gyan.FFmpeg -e`
   - This also sets a path to it so you can use it from anywhere


# Cool things
- Set Transparent Pixel in a png
   - `ffmpeg -i basemap_for_transparency.png -vf "colorkey=0xff00ff:0.1:0.1" transparent_basemap.png`