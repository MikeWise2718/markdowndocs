---
title: "Octo Generalist Robotics Policy"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Site: (https://octo-models.github.io/)

# Installation
- Installation decription is incomplete
- Have to install Cuda and CuDnn first
- Tried with 11.8 (minimum 4090) and 8.6.0
- Also tried with 12.4 and 9.0(?)
- Since both are installed, and various things have different paths, it is hard to tell what is being used
- Sketch:
    - Install Cuda and CudNN from Nvidia sites
        - WSL needs to have it installed from Windows (how to check this?)
    - Install Anaconda
    - Make sure `conda` works
    - follow Octo conda installation

    - Add conda installation of cudatools and cudadnn afterwards
      - `conda install -c anaconda cudatoolkit`
      - `conda install -c anaconda cdnn`
    - Installs Jax
    - Test

# Current
- Get list of conda environments `conda env list`


# VS Code
- Install on Ubuntu: (https://code.visualstudio.com/docs/setup/linux)

# Problems
   - `import flax` did not work, had to go to flax 8.5.0 under Bare Metal Linux
   - This meant that we had to install Jax 4.30
   - Error message was .... something
   - `jax.random.KeyArray` was depreciated
   - had to change `KeyArray` in `octo/octo/types.py` to `key`
