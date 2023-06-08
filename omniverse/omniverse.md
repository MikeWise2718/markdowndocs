---
title: "Omniverse"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Nvidia's Omniverse

# Docs
- Omniverse API docs: (https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/API.html)
- Frequently used snippets: (https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/reference_python_snippets.html)
- Omni Cheat Sheet (a bit old): (https://mtw75.medium.com/omniverse-kit-cheat-sheet-9d2a7cce9fb)
- USD Cookbook: (https://github.com/ColinKennedy/USD-Cookbook)
- Finding commands (search in commands): (https://forums.developer.nvidia.com/t/is-there-a-naming-convention-for-commands-in-omni-kit-commands/212926)

# Apps
- All live in `c:\users\mike\AppData\local\ov\pkg\*`
- For Spearrow I installed into `d:\nv\ov\pkg`
- Launcher lives elsewhere `c:\users\mike\AppData\
- Command line: (Where did I get this?)
   - `"C:\Users\mike\AppData\Local\ov\pkg\create-2022.2.0\kit\kit.exe"  "C:\Users\mike\AppData\Local\ov\pkg\create-2022.2.0\apps/omni.create.kit"  `
- Kit App initialization and configuration explained: (https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/configuring.html)
- Omniverse Laucher using Create "Launch" button starts `D:\nv\ov\pkg\create-2022.3.3\omni.create.bat`
- There are alternate bats you can launch from instead
Original `omni.create.bat`:
```
@echo off
setlocal
call "%~dp0kit\kit.exe" "%%~dp0apps/omni.create.kit"  %*
```
Paul Rance's:
```
call "%~dp0kit\kit.exe" "%%~dp0apps/omni.create.kit" --/exts/omni.ui/raster/default_rasterpolicy_enabled=true --/renderer/multiGpu/enabled=true --/exts/omni.kit.widget.graph/raster_nodes=true %*
```

# API Basics
- Its all based on Pixar's stuff, you have to know their docs too
- USD Main page - (https://openusd.org/dev/api/index.html)
- USD Core Docs - (https://openusd.org/dev/api/usd_page_front.html)
- USD Python API - (https://docs.omniverse.nvidia.com/prod_usd/prod_kit/dev_usd/quick-start/api.html)
```
# analog to the UsdGeomSphere() constructor in C++
from pxr import Usd, UsdGeom

invalid_prim = Usd.Prim()
sphere = UsdGeom.Sphere(invalid_prim)
```


# Useful BAT things
- The %~dp0 (that's a zero) variable when referenced within a Windows batch file will expand to the drive letter and path of that batch file
`run_pip.bat` - for run python just trim off the `-m pip install %*` below
```
@echo off
setlocal
pushd "%~dp0"
set ROOT_DIR=%~dp0
set USD_LIB_DIR=%ROOT_DIR%_build\windows-x86_64\release
set PYTHON=%ROOT_DIR%_build\target-deps\python\python.exe
set PATH=%PATH%;%USD_LIB_DIR%
set PYTHONPATH=%USD_LIB_DIR%\python;%USD_LIB_DIR%\bindings-python
set CARB_APP_PATH=%USD_LIB_DIR%
if not exist "%PYTHON%" (
    echo Python, USD, and Omniverse Client libraries are missing.  Run prebuild.bat to retrieve them.
    popd
    exit /b
)
"%PYTHON%" -m pip install  %*
popd
EXIT /B %ERRORLEVEL%
```




# Kit
- Kit docs - (https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/kit_overview.html)
- Scripting a kit app - (https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/python_scripting.html)
- Writing an extension - (- https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/extensions_basic.html)
- printed python path with "import sys; print(sys.path)" - for code it was 21k long!

# Services
- List of services running: (http://localhost:3080/)

# Misc
- For GPU status: `nvidia-smi`
- Issac Sim - Hello World: (https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/tutorial_core_hello_world.html)
- Python Snippets: (https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/reference_python_snippets.html)
- Forums - (https://forums.developer.nvidia.com/)

# Cortex
- Video

# Connectors 
- Installed Connectors from "Nvidia Omniverse Launcher"
   - EXCHANGE, then scroll down to connectors, then install "Connect Sample Omniverse Connector" (version 201.0.0)
![sample-connector](images/sample-connector.png)


- It installed into "d:\nv\ov\pkg\connectsample-201.0.0"
- Interested in running "run_py_live_session.bat"
- Had to run "prebuild.bat" first
- Had to have a Nucleus server available (used a localhost)
- Using an OV app like "Create" 
- Created a file with a single object "Sphere" and saved it to:
     - Make sure it is a "Mesh" (should say so in the Stage window)
     - "Omniverse://localhost/mike/testconnector.usda"
     - Clicked on "Live" upper right and created a session "sphere1"
     - Ran it specifying the file and the Sphere, and the session
     - When I pressed "t" the sphere moved around - so it worked 
```
D:\nv\ov\pkg\connectsample-201.0.0>run_py_live_session.bat -e Omniverse://localhost/Users/mike/testconnector.usda -m Sphere
[2023-05-31 14:55:05 PyChannelManager (INFO)] Starting Omniverse Channel Manager...
Select a live session to join:
 [0] sphere1
 [n] Create a new session
 [q] Quit
Select a live session to join: 0
[2023-05-31 14:55:10 PyLiveSessionChannelManager (INFO)] Awaiting a join channel: omniverse://localhost/Users/mike/.live/testconnector.live/sphere1.live/__session__.channel
[2023-05-31 14:55:10 PyChannelManager (INFO)] Starting to join channel: omniverse://localhost/Users/mike/.live/testconnector.live/sphere1.live/__session__.channel
[2023-05-31 14:55:10 PyChannelManager (INFO)] Join channel omniverse://localhost/Users/mike/.live/testconnector.live/sphere1.live/__session__.channel successfully.
[2023-05-31 14:55:10 PyChannelManager (INFO)] Send JOIN message to channel omniverse://localhost/Users/mike/.live/testconnector.live/sphere1.live/__session__.channel, content: {}
[2023-05-31 14:55:10 PyLiveSession (INFO)] Selected session URL: omniverse://localhost/Users/mike/.live/testconnector.live/sphere1.live/root.live
[2023-05-31 14:55:10 PyLiveSession (INFO)] Begin Live Edit on /World/Sphere
[2023-05-31 14:55:10 PyLiveSession (INFO)] Enter an option:
 [t] transform the mesh
 [o] list session owner/admin
 [u] list session users
 [g] emit a GetUsers message (note there will be no response unless another app is connected to the same session)
 [c] log contents of the session config file
 [v] validate the current state of the session layer
 [m] merge changes and end the session
 [q] quit.

[2023-05-31 14:55:10 PyChannelManager (INFO)] Message received from user with id W8DFGDY2WU0T27KQ.
[2023-05-31 14:55:10 PyChannelManager (INFO)] Hello message from user with id W8DFGDY2WU0T27KQ, name mike.
[2023-05-31 14:55:10 PyLiveSessionChannelManager (INFO)] User mike joined.
[2023-05-31 14:55:10 PyLiveSession (WARNING)] mike - Create is in the live session
[2023-05-31 14:55:14 PyLiveSession (INFO)] Setting pos [-149.88, -0.00, 77.19] and rot [0.00, 15.00, 0.00]
[2023-05-31 14:55:14 PyLiveSession (INFO)] Setting pos [-144.88, -0.00, 85.85] and rot [0.00, 30.00, 0.00]
```
![ConnectorText](images/ConnectorText.png)
![SampleScene](images/SampleScene.png)


# Code
`C:\Users\mike\AppData\Local\ov\pkg\isaac_sim-2022.1.1\exts\omni.isaac.demos\omni\isaac\demos\utils`
`C:\Users\mike\AppData\Local\ov\pkg\isaac_sim-2022.1.1\exts\omni.isaac.demos\omni\isaac\demos\ur10_scenarios`
`C:\Users\mike\AppData\Local\ov\pkg\isaac_sim-2022.1.1\exts\omni.isaac.examples\omni\isaac\examples\hello_world`

# Logs
- Start with logs outputting to a CMD windows:
   - `cd C:\Users\mike\AppData\Local\ov\pkg\create-2022.2.0`
   - `ommi.create.bat`
- `https://forums.developer.nvidia.com/t/create-crashing-on-launch/179671`


# Getting Started writing extensions
- https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/extensions_basic.html
- Can create directory wherever you want
   - The selected folder will be prepopulated with a new extension.
   - `exts` subfolder will be automatically added to extension search paths.
   - `app` subfolder will be linked (symlink) to the location of your Kit based app.
   - The folder gets opened in Visual Studio Code, configured and ready to hack!
   - The new extension is enabled and a new UI window pops up:
   - Note the TOML config file location (under `config` subfolder)


# Code Places
- Directory of `Mesh Seperate` extension in `Audio2Face` app: 
    - Go to `Window\Extensions\` then serch for `Mesh`, click on `Mesh Seperate` then click on the folder icon on the top to get: above
```
D:\nv\ov\pkg\audio2face-2022.2.1\extscache\omni.kit.mesh_separate-1.1.7
```
- Diector of `Hello World` example from `Issac Sim` app
    - Go to `Menu\Issac Examples\Hello World` then in the dialog that opens, click on the folder icon on top to get `HelloWorld.py` in this:
```
D:\nv\ov\pkg\isaac_sim-2022.2.0\exts\omni.isaac.examples\omni\isaac\examples\user_examples
```