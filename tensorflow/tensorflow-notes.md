---
title: "Tensorflow Notes"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Tensorflow - main install link: [link](https://www.tensorflow.org/install/)
 - 9 March 2017 TF 1.0.1 installed into Anaconda3 (from file dates)
 - Actually installing TF is a royal pia every time. Switching to Docker.


![TensorFlow logo](tflogo.png)

# Docker
First you ahve to install docker of course. Try [this](https://docs.docker.com/get-started/#container-diagram)
Then this command gets you far:
docker run -it -p:8888:8888 tensorflow/tensorflow


# Installing with anaconda
Start with the anaconda command prompt
  - windows key 
  - type "anaconda"
  - click on the command prompt icon

Start with a naked enironment and then activate it
 - conda create --name tf python=3.6
 - conda tf

Then install Tensorflow
  - pip install --upgrade tensorflow

Then test it
  - see the tensorflow install page for a little test program

Then you might want to install jupyter
 - pip install --upgrade jupyter


# Links
 - Repository - [link](https://github.com/tensorflow)
 - Newest Release notes - [link](https://github.com/tensorflow/tensorflow/blob/master/RELEASE.md)


# Command line commands
 - Get version:
   - "python -c 'import tensorflow as tf; print(tf.__version__)'"  # for Python 3
 - Get version with conda 
    - "--upgrade "


# Running Models 
These are examples basically
- You have to download the tensorflow.models repository, it used to be part of TF, but has now been seperated out.
- You need to have "bazel" (a make tool installed) to run some of the examples
- You need to install "chocolaty" in order to install "bazel" (sheesh...)
   - [chocolaty link](https://chocolatey.org/)
   - Start powershell as administrator
   - That was just a single line powershell script:
   - "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
   - close and restart powershell as admin
   - goes quickly
- To install bazel:
   - [bazel link](https://bazel.build/versions/master/docs/install-windows.html)
   - "choco install bazel"
   - That installed version 0.4.5 which had a bug (see my SO post)
       - bazel help gets you the version number
       - bug is here: https://github.com/bazelbuild/bazel/issues/2708
       - choco install bazel --version 0.5.0-rc6
   - It pollutes the c drive with a c:\tools\msys64 directory
   - takes ages to execute, downloads all kinds of crap, etc.
   - afterwards you have to set an environment variable:
      - BAZEL_SH=c:/tools/msys64/usr/bin/bash.exe
      - (optional) BAZEL_VS="C:/Program Files (x86)/Microsoft Visual Studio 14.0"
      - (optional)BAZEL_PYTHON=C:/Python27/python.exe
    - If you want to start over 
    - Never actually got it to work

# model - textsum
   - Model and Readme can be found here:
       -  https://github.com/tensorflow/models/tree/master/textsum
   - This builds all the scripts
        - bazel build -c opt --config=cuda textsum/...
   - Used this bash under a Powershell with admin priveleges:
        - C:\tools\msys64\usr\bin\bash
   - This does the training: 
          - "bazel-bin/textsum/seq2seq_attention --mode=train --article_key=article --abstract_key=abstract --data_path=data/training-* --vocab_path=data/vocab  --log_root=textsum/log_root --train_dir=textsum/log_root/train"
   - Failed complaining TF was not installed (it is because it was running Python 2.7)
      - noticed c:\Python27;c:\Python27Scripts had made it to top of my path after installing bazel, deleted them
      - That made it use my Anaconda (4.1.164 - bit) Python 3.5.2
   - It did not run in the D: drive, had to move everything to the C: drive to get it to work.
   - Finally ran but with lots of "Assertion Error: Empty filelist."
          - Could be related to my tensorflow 1.0.1 which is old at this point
          - Ran using all 8 CPUs, CPU usage around 25%, GPU usage around 3%


# seq2seq - 6 Dec 2017
 - Tried to get this installed on my "new" Surface Book
 - Installed Anaconda 3.6, and then TensorFlow 1.4, following instructions on TensorFlow site
 - Used the TensorFlow gpu version (which was probably a mistake)
 - Had to install a couple extra packages like yaml and something else before it worked
 - There were a couple lines I had to change in one of the files to get two of the libraries to work
     from tensorflow.contrib.distributions import  Bernoulli
     from tensorflow.contrib.distributions import Categorical
 - Changes were to this file: C:\tensorflow\seq2seq\seq2seq\contrib\seq2seq\helper.py

 #boltzmann-machine notes

- pip install nosetest 
 - changed nosetest path in makefile to "which nosetest" path
 - make test &> err.txt
 - gedit err.txt
 - pip install tqdm
 - pip install seaborn
 - sudo apt-get install python-tk
 - Final text
 - Ran 8 tests in 29.171s
 - OK
 - pip install jupyter
 - changed path in makefile to which jupyter path
 - pip install JSAnimation
 - pip install sklearn