---
title: "OBS"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- OBS means Open Broadcast Software (https://obsproject.com)
- Great intro video - (https://www.youtube.com/watch?v=yTkpLd3tdbc)
- Apparently you should start it in Administrator mode

# Concepts
- Scene Collections (a collection of screens or tescenes)
- Source (a video, audio source, image, etc)
- Scene (a collection of sources (kind of as layers))
- Settings (a hellishly large collection of settings) (lower right panel Control/Settings)
- Profile (Collection of settigns)

# Workflow
- Pick a scene collection that is similar to something you did in the past
- Duplicate it (you need a new name)
- Change the output directories (find them in the panel `Contols/Settings/Output` (default in the lower right))
  - Don't forget `Apply`
- Start recording


# Powerpointing
- Select a scene collection that is similar to the one you want (like BaeSlideDeck) under "Scene Collections"
- Select "Duplicate" and give it a new name
- Change the output directories (find them in the panel `Contols/Settings/Output` (default in the lower right - probably want to save in a subdirector to videos))
  - Don't forget `Apply`
- Make sure you have the right sources
  - Audio Input Capture (make sure you don't have two microphones or it might be too faint, test with devices and make sure it is hitting 100 percent)
  - Display Capture allows you to capture an entire monitor - probably best to have it set to 1080p resolution beforehand
- Start Powerpoint on the display you want to capture on (the capture-display)
- Go to Presentation Mode (that wierd little icon on the bottom)
- Your presentation should occupy the capture-display
- It will be maximized for presentation on the other
  - On the other display hit "demaximize icon" on the top right
  - Now use "WindowsKey+left" arrow to move it to the left
  - Select OBS application to occupy the right
- For each slide:
  - In OBS select "Start Recording" and start talkings
  - When you hit "Stop recording" it will save the video
  - Repeat "Start/Stop Recording" until you think you are happy
  - Now go to the output direct and delete the false takes and look at the take you liked
  - If you like it give it a new name like "01-Intro"
  - Now do that for the next slide


# Windows
- To operate it you need all four panels, Scenes, Sources, Audio Mixer, and Controls
- They can be detached, put over each other as tabs, and moved around, so if you can't find one it could be anywhere
- You free a tab by clicking on the top right corner of thw window (the double window icon)

# Scenes and sources
- A scene is a group of sources


# Recording a video playing in a hyper-v
(screen shot)

# DaVinci Resolve
- you can't edit in OBS
- So use DaVinici Resolve
