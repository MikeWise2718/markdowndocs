---
title: "How Python with VScode works"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

## VS Code
VS Code is a general editor, made for working with lots of different kinds of projects - but kept lightweight. Portability to platforms like MacOS and Linux are also high priorities.


VS Code is "folder based", that means it loads settings from a folder that you "open". Here you can specify if it is to operate in different kinds of modes. This document will mostly be around how to operate it in python model

VS Code changes frequently. You practially have to update it every week. ALso the ways you work with it have changed over time.

What to do:
- Install VS Code
- Install a  good Python Language Extnestion, the one from Don Jayamanne is the most common
- You might need to close VS Code now if you need a python envionment

To activate a particular python environment
- Go to the top level menu and enter `/View/Command Palette..`
- From the Text Box that now opens, select `Python: Select Python Interpreter`
- You should get a list of available Python versions with their environments listed underneath them

# Usint it as a REPL
- To run right-click on a python file in explorer and select `Run Python File in Terminal`
- This should cause a terminal window to open up with the correct environment activated (you can see the command in the terminal window)
- You then need to start python by typing `python` (huh?)
- Now you can select code portions, right click and select `Run Selection/Line in Python`
- On the command line you can query the variable stats with print statmenets

### Things that kind of suck about this REPL Experience
- There is no variable window like in R-Studio, RTVS, or Spyder
- There is no up-arror or down arrow to select recent statements
- There is no "source" button or command anywhere
- Sometimes when you right click on the code, there is no `Run Selection/Line in Python`, but something similar that send it to a non-existent Jupyter notebook and give you a "Noteboook not selected/started" error from the Jupyter Extension. Horrible...

# Running with Debugging
 - Check link [here](https://code.visualstudio.com/docs/python/debugging)
 - and [here(https://code.visualstudio.com/docs/editor/debugging)]
 - It creates the `launch.json` when you click the gear after you clicked on the debugger bug icon.
 - Then you have to set things
 - The following `launch.json` worked for me when I loaded `main.py` from that directory, and made it the current file. 
``` 
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "args": [
                "-e 1"
            ]
        }
    ]
}
```
 - Note that it specifies an "-e 1" parameter as an argument.
 - specifying `main.py` as the program curiously did not work.

# Running without Debugging
- Just do this from a seperate CLI window, or from the Terminal window
- You have to make sure the directory is correct

# Extensions
You will want make sure the following extensions are up to date:
 - Don Jaymanne python extention (0.7.0 as of 2017-10-02)
 - Jupyter 1.1.3 Don Jaymanne python extention (1.1.3 as of 2017-10-02)
 
# Documentation
https://code.visualstudio.com/docs/languages/python

 # Icon Bar
 On the left, we have five icons for the 
 * file explorer
 * search (find)
 * source code control (git)
 * run and debug
 * extensions

 Things to note
 - You can get to the user settings by clicking on the gear icon/settings in the lower left, or from the menu File/Preferences/Settings

# Virtual Environments with Python
- If it is after October, install new python and include path in environment variable
- 
