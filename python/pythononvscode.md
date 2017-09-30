---
title: "How Python with VScode works"
output: html_document
---

## VS Code
VS Code is a general editor, made for working with lots of different kinds of projects - but kept lightweight. Portability to platforms like MacOS and Linux are also high priorities.


VS Code is "folder based", that means it loads settings from a folder that you "open". Here you can specify if it is to operate in different kinds of modes. This document will mostly be around how to operate it in python model

VS Code changes frequently. You practially have to up date it every week. ALso the ways you work with it have changed over time.

There are a couple of good StackOverflow posts on this here:
http://stackoverflow.com/questions/29987840/how-to-execute-python-code-from-within-visual-studio-code


Particular this post is important from valad2135:

    All these answers are obsolete now.

    Currently you have to:

    1. install Python language extension (and python, obviously)
    2. open folder (important!), open any python file inside that folder
    switch to debug "tab"(?) and click on the gearbox (with hint 'Configure of Fix 'launch.json'')
    3. save opened launch.json file (it's placed in .vscode subdir in the folder opened on step #2)
    4. finally, click green triangle or hit F5
    No additional extensions or manual launch.json editing is required now.


More explanation of what this does can be found in the post fromLVT:

# Extentions
You will want make sure the following extensions are up to date:
 - Don Jaymanne python extention
 - pylint (?)




