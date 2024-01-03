---
title: "Jupyter"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
I think of Jupyter as R-Markdown for Python, but that is not really true.

# Installation
* pip install jupyter
* Anaconda has it by default 
* 29.12.2020 - https://medium.com/analytics-vidhya/making-a-new-conda-environment-and-using-it-inside-jupyter-notebook-3191e3362dc9
* 29.12.2020 - Anaconda does not have it by default now and I had to do this to install the kernels:
* `conda install nb_conda_kernels -y`

# Configuration
 * There is no configuration by default. 
 * The command `jupyter notebook --generate-config` generates a commented out config file in the `~/.jupyter` directory
 * You can disable auth by commenting out a couple of lines
 * You can also set the default notebook directory, otherwise the default is the directory you start "jupyter notebook" from
 * you are supposed to activate the conda environment before you start jupyter, but there is also a tab you can select it from in the UI

# Startup
* go to the directory where the notebook is
* `jupyter notebook mynotebook.ipynb`
* Note that the command window will then start echoing the jupyter log - this is highly useful for debugging problems

 # Remote usage (from another machine)
 * Start jupyter 
 * When it comes up it will give you a token to start from
 * Jupyter by default uses port `8888` (?)


# Log
- login with putty
- `source ~/tf27gpu/bin/activate`   # prompt should change
- `. tfon` 
- `cd tfrepos/models/research/object_detection`
- `. cdod` 
- `jupyter notebook --ip='192.168.25.12' object_detection_tutorial.ipynb`
- You get a command like ` http://192.168.25.12:8888/?token=f6982adb2e4bcb93bf0f15f2bd5e64ef22b22d7                                                                                                                                                     9bc8c0f75` 
- you can login with that, or just enter the token subsequently


# Jupyter Lab
- Start jupyter lab by installing jupyter, then starting it
    - `pip install jupyter`
    - `juptyer lab`

- Has native support for MathJax (I think)


# MathJax samples
- 