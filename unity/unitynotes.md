---
title: "Template Titles"
output: html_document
---

# Intro
Unity3D is a powerful game engine. Here I keep notes on things that took me awhile to figure out that I think I might forget.

Note that to get a preview of this document in VS Code use Ctrl-Shift-V

Unity Subscription FAQ: [Unity FAQ](https://unity3d.com/unity/faq)

Unity Technical Forums: [Unity] http://answers.unity3d.com/page/faq.html



# Layout notes
There are game windows but only one scene window. New The game windows get associated with a display (can be set on the upper left), and a camera is associated with a dispaly too. That is how it is done. Input goes to only one game window though, not sure which one.
To create a new window, you create a new tab in an old window, and then drag it to a new location. Can even be detached from the application, so on another screen.
You can grab the tag of a game window and drag it to another window in the layout,or even to a new place in the same window, which will cause it to create a new window there splitting up the space. This is kind of odd, but it does make it easy to do pretty much any kind of layout quickly


# Where to find things
Asset Store is hidden in the window menu. To find out what assets you have bought, go to the "inbox-tray" icon in the Asset Store window.

# Assets 
 - Modern People 1.1
 - Handy Hacks (Measuring Tools)
 - Vostopia Mecanim Demo (broken, but I like the Xbox like people)

# Finding the pivot point of an object
The "pivot point" is the point that the object rotates around when you chose the rotate tool in the button bar. To find it:
- Select the object
- then select the rotate tool (pressed in button below)
- Then create a cylinder or a sphere at that point. 
- now just examine the coordinates of its "Postion" in the Inspector window.
- Those coordinates are the pivot point

![Finding Pivot](FindingPivot.png)
