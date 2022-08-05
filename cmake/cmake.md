---
title: "CMake"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- CMake - can't really live without it these days
- Good tutorial: (https://riptutorial.com/cmake)



# Build Sequence on Windows
```
> mkdir build
> cd build
> cmake ..
> cmake --build .
> devenv helloworld.sln /build
or
> msbuild hello_world.sln /property:Configuration=Release /property:Platform=x64
```
