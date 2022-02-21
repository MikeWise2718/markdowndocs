---
title: "USD - Universal Scene Descriptor"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Pixar's baby - homepage: (https://graphics.pixar.com/usd/release/index.html)


# Tutorials
- (https://graphics.pixar.com/usd/release/tut_usd_tutorials.html)

# Unity USD Package
- Unity USD Package - (https://github.com/Unity-Technologies/usd-unity-sdk)
- Examples are in Package, but you have to specify them to be exported or they wont be there
- Scene Docs - (https://docs.unity3d.com/Packages/com.unity.formats.usd@3.0/api/USD.NET.Scene.html)

# USDTools
- you need these
- Hard to compile
  - Followed instructions mostly
  - X86 command prompt
  - Needed cmake, NASM, and python to execute build
  - wouldn't work with newer versions of python
     -  `AttributeError: module 'subprocess' has no attribute 'mswindows'. Did you mean: '_mswindows'?`
  - Had to use conda because I needed a different version of python
    - 
  - had to use python 2.7 in the end because conda has forgotten about python 3.4 and below
    - `conda create --name USDtools python=2.7`
  - Had to get the x86 to use the conda environment
     - `C:\Users\mike\anaconda3\condabin\conda.bat activate USDtools`
  - Couldn't have a space in the installation directory (like they suggested)
     - `python build_scripts\build_usd.py "C:\Program Files\USD" does not work`, fails building TBB or 
```
STATUS: Installing zlib...
STATUS: Installing boost...
2021-12-03 12:25
bootstrap.bat --prefix="C:\Program Files\USD"
Building Boost.Build engine
=C:\Program was unexpected at this time.
```

- This is what success looks like:
```
(USDtools) D:\transfer\USD>python build_scripts\build_usd.py "D:\transfer\USDtools"

Building with settings:
  USD source directory          D:\transfer\USD
  USD install directory         D:\transfer\USDtools
  3rd-party source directory    D:\transfer\USDtools\src
  3rd-party install directory   D:\transfer\USDtools
  Build directory               D:\transfer\USDtools\build
  CMake generator               Default
  CMake toolset                 Default
  Downloader                    curl

  Building                      Shared libraries
    Variant                     Release
    Imaging                     On
      Ptex support:             Off
      OpenVDB support:          Off
      OpenImageIO support:      Off
      OpenColorIO support:      Off
      PRMan support:            Off
    UsdImaging                  On
      usdview:                  On
    Python support              On
      Python Debug:             Off
      Python 3:                 Off
    Documentation               Off
    Tests                       Off
    Examples                    On
    Tutorials                   On
    Tools                       On
    Alembic Plugin              Off
      HDF5 support:             Off
    Draco Plugin                Off
    MaterialX Plugin            Off

  Dependencies                  zlib, boost, TBB, OpenSubdiv
STATUS: Installing zlib...
STATUS: Installing boost...
STATUS: Installing TBB...
STATUS: Installing OpenSubdiv...
STATUS: Installing USD...

Success! To use USD, please ensure that you have:

    The following in your PYTHONPATH environment variable:
    D:\transfer\USDtools\lib\python

    The following in your PATH environment variable:
    D:\transfer\USDtools\bin
    D:\transfer\USDtools\lib
```

Bat file to setup environment to use USDtools:
```
set PYTHONPATH=D:\transfer\USDtools\lib\python
C:\Users\mike\anaconda3\condabin\conda.bat activate USDtools
```

# Examples
- Activate Python
   - `conda activate USDtools`
   - `cd D:\transfer\USD\extras\usd\tutorials\animatedTop`
   - `usdview top.geom.usd`