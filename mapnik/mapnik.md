---
title: "Mapnik"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- mapnik make extrodinarily high quality graphic maps. It is the engine used to generate the OpenStreetMap maps.
- Github repo: https://github.com/mapnik 
- Website: https://mapnik.org/
- Current version (as of 2019-01-21) is 3.0.21

# Windows
- Binaries only available for 2.2.0 
- Dropped support https://github.com/mapnik/node-mapnik/issues/848 
- Windows installation: https://github.com/mapnik/mapnik/wiki/WindowsInstallation
- Note there is no OSM plugin for Windows which makes it a bit useless
- Also had a lot of trouble installing it - needs to have all the binaries in the execuable directory
- Also only runs with 32-bit Python (ugh)

# Ubuntu
- So I moved to Ubuntu
- Cloned the repo https://github.com/mapnik 
- Made it according to these instructions: https://github.com/mapnik/mapnik/wiki/UbuntuInstallation
- Turns out Python bindings are no longer included in the distro
- So need to make the mapnik python bindings: https://github.com/mapnik/python-mapnik
- Which highly recommends a virtual environment (ugh)
