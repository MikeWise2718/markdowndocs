---
title: "boost"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Some kind of humongous super math/performance library for C++
- A pita to install and configure
- Uses like 0.5 GB on disk

- https://www.boost.org/doc/libs/1_55_0/more/getting_started/windows.html
- https://robots.uc3m.es/installation-guides/
- https://robots.uc3m.es/installation-guides/install-boost.html
   - Issue b2 variant=release address-model=64 link=static,shared to build 64-bit static and dynamic binaries in Release configuration for all available Boost components

# Something Else
- b2 --build-dir=d:\lib\boost --toolset=msvc --built-type=complete stage
- b2 --build-dir=d:\lib\boost --toolset=msvc --built-type=complete --link=static,shared stage

- failed with Python 3.10 
 - "libs/python/src/exec.cpp:109:14: error: '_Py_fopen' was not declared in this scope; did you mean '_Py_wfopen'?"
- started Anaconda 3.8 at 8:15,to 8:37...8:39
- b2 variant=release address-model=64 link=static,shared

```
common.copy D:\lib\boost_1_70_0\stage\lib\libboost_program_options-vc142-mt-gd-x32-1_70.lib
d:\lib\boost\boost\bin.v2\libs\program_options\build\msvc-14.2\debug\link-static\threading-multi\libboost_program_options-vc142-mt-gd-x32-1_70.lib
        1 file(s) copied.
...updated 2441 targets...
```

moved `d:\lib\boost\boost` to `d:\lib\boost`