---
title: "Blender"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Blender is THE open source renderer home page:(https://www.blender.org/)

# Blender Vocab and UI Notes (as of 2.93.4)

## Workspaces, Windows, Layouts
- Described here: (https://docs.blender.org/manual/en/latest/interface/window_system/workspaces.html)
- Workspaces are predefined layouts
- Default workspace is 3D Viewport, Outliner, Properties, Timeline
- There are other workspaces for Modeling, Sculpting, Animation, Rendering etc.
- Tutorial (Blender Guru (Australian guy) is not bad)
## Editors
- Blender "Editors" are what other usually refer to as "Toolbars"
- The default Active Editor is vertically extended on the upper-left
- You can change the Active Editor (default is 3D-Viewport) with the icon dropdown in the extreme upper-left (directly under the Blender icon)

# Coordinate System
- RHS normally Y is up, and you look between X and Z ()

# View Navigation

|Navigation	| Three-Button Mouse	| Emulated 3-Button Mouse
| :------------- | :----------: | -----------: |
|Orbit	| Middle-click	| Alt+left-click
|Pan	| Shift+middle-click	| Shift+Alt+left-click
|Zoom	| Middle-wheel or Ctrl+middle-click	| Ctrl+Alt+left-click

# Move an Object
- To move an object select the Move icon (4 arrows) out of the Active Toolbar 
- Then select the object, it will be highlighted and its properties will fill the properties windows
- Now select one of the RGB-axes arrows that appear there and move it around
- Its position values will change in the properties windows (Location)

# Change material
- In the Outliner window find the object (clicking on it should highlight it)
- Its material will appear there, you can edit it there

# Render 
- Fastest way is press F12


# Blender import into Unity - FBX
- Notes from working on the Staples Stadium project 13.11.2021
- You can in principle import .blend files directly into Unity, but Unity just invokes Blender to export it as an FBX, so that is not really much of a feature as you need to have Blender installed for it to work.
- So you are going to want to export it as FBX or OBJ
- FBX seems to be higher fidelity and has more information though it is a binary format
- FBX is owned by Autodesk and can be apparently either binary or text
(https://en.wikipedia.org/wiki/FBX)
- Materials are embedded in FBX, but the texture files are normally separate PNGs or JPGs
- You probably want to put the FBX in a separate folder under Assets (but not under Resources) in your Unity folder
- Then you probably want to drag it into the scene, and drag a copy (thus a prefab) into some Resources subfolder
- Then it can be loaded with Resource.Load<GameObject>
- Include all the texture files in the same folder as the FBX
- If you want to refer to the material files with Resource.Load<Material> (and I did) then you will need to extract the materials
- You can export a material from an FBX by right-clicking on the material (you can select multiple materials) and select "Extract Material". You then need to select a folder for it to be extracted to and it will be deleted from the FBX.
