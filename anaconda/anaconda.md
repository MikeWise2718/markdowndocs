---
title: "Anaconda"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Anaconda - probably the main Python package for scientific computing.

# Starting it
- To start anaconda start the prompt "Anaconda prompt" from the windows Icon
- You can see where it installed with the where command:
 - I had it in "C:\Program Files (x86)\Microsoft Visual Studio\VS15Preview\Anaconda3_64\python.exe"


# Installation
- WHen you install it you can choose a directory.
- My default when installing on windows was "C:\Users\mike\Anaconda3"
- Seems that in the past it might have put it in "C:\Users\mike\AppData"

# Always work in environments
- Managing environment link <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually>


# Creating a first environment
- `conda env create -f first.yml`


first.yml:

```
name: osm-bld-heights
channels:
  - anaconda
  - conda-forge
  - anaconda-fusion
  - defaults
dependencies:
  - numpy
  - matplotlib
  - pandas
  - pip
  - scikit-learn
  - scipy
  - jupyterlab
```