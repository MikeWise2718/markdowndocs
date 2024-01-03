---
title: "Template Titles"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Python needs no stinkin' intro

# Virtual Environments
* It is a confusing space - differneces: <https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe>
* `virtualenv` is here: <https://virtualenv.pypa.io/en/stable/>
* VEs Explained here: <https://docs.python.org/3//tutorial/venv.html>

# Modules
- The `PYTHONPATH` environment variable sets the search path for importing python modules


# Flake8 
Useful Flake8 commands
  - Turn off everything `# flake8: noqa`
  - Turn off one rule `# flake8: noqa: E501`
  - just add `# noqa` to the end of a line
  - in `.vscode\settings.json` (have to start and restart vscode to get it to see changes)
  ```
{
    "python.analysis.typeCheckingMode": "basic",
    "python.linting.flake8Args": [
        "--max-line-length=120",
        "--ignore=E402,F841,F401,E302,E305"
    ]    
}
  ```