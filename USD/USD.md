---
title: "USD - Universal Scene Descriptor"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Pixar's baby - homepage: (https://graphics.pixar.com/usd/release/index.html)


# USDTools
- you need these
- Hard to compliple
  - Followed instructions mostly
  - X86 command prompt
  - Needed cmake, NASM, and python to execute build
  - wouldn't work with newer versions of python
     -  `AttributeError: module 'subprocess' has no attribute 'mswindows'. Did you mean: '_mswindows'?`
  - Had to use conda because I needed a different version of python
    - 
  - had to use python 2.7 in the end because conda has forgotten about python 3.4 and below
    - conda create --name USDtools python=2.7
  - Had to get the x86 to use the conda environment
     - `C:\Users\mike\anaconda3\condabin\conda.bat activate USDtools`
  - Couldn't have a space in the installation directory (like they suggested)
     - `python build_scripts\build_usd.py "C:\Program Files\USD" does not work`, fails building TBB or maybe Boos
```
STATUS: Installing zlib...
STATUS: Installing boost...
2021-12-03 12:25
bootstrap.bat --prefix="C:\Program Files\USD"
Building Boost.Build engine
=C:\Program was unexpected at this time.
```


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