---
title: "Python"
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

# Whitespace stripping
- You can get VS Code to strip ending whitespace on a file save (https://stackoverflow.com/a/53663494)
- Menu -> Preference → Settings → User Settings Tab → Text Editor → Files → Trim Trailing Whitespace

# Flake8
Useful Flake8 commands
  - Turn off everything `# flake8: noqa`
  - Turn off one rule `# flake8: noqa: E501`
  - just add `# noqa` to the end of a line
  - in `.vscode\settings.json` (have to start and restart vscode to get it to see changes)
  - E226 - ignore whitespace around arithmetic operators
  - E301 - expected 1 blank lines, found 0
  - E302 - expected 2 blank lines, found 0
  - E303 - too many blank lines (3)
  - E305 - expected 2 blank lines after end of function or class
  - E402 - module level import not at top of file
  - E501 - line too long
  - E731 - do not assign a lambda expression, use a def
  - F401 - ignore unused variable warning
  - F841 - local variable name is assigned to but never used
  - W503 - line break before binary operator
  - `E***/W***`: pep8 errors and warnings (https://pep8.readthedocs.io/en/latest/intro.html#error-codes)
  - `F***` - PyFlakes warnings (https://flake8.pycqa.org/en/2.5.5/warnings.html)
  - `C9**` - McCabe (https://github.com/PyCQA/mccabe)
  - `N9**` - pep8-naming (https://github.com/PyCQA/pep8-naming)
```
{
    "python.analysis.typeCheckingMode": "basic",
    "python.linting.flake8Args": [
        "--max-line-length=120",
        "--ignore=E226,E402,E501,F401,F841"
    ]
}
```

# Whitespace stripping
- You can get VS Code to strip ending whitespace on a file save (https://stackoverflow.com/a/53663494)

# Windows 11 preveiw edition keeps deleting python and its environment
- configuring Auditing from (https://discuss.python.org/t/python-deleting-itself/22830/3)
```
First, run the management console snap-in “secpol.msc”. Make the following change to enable access auditing:

-Expand “Security Settings” → “Local Policies”.
-Click “Audit Policy”.
-Double click “Audit object access”.
-Under “Audit these attempts”, enable “Success”.
-Close the security policy snap-in.

Then in Explorer, for each folder:

-Right-click the folder and select “Properties”.
-Select the “Security” tab and click the “Advanced” button.
-Select the “Auditing” tab
-If asked, click “Continue” to allow administrator access, and “Yes” if prompted for consent.
-Click “Add”.
-Click “Select a principal”.
-Enter “Everyone”, and click “OK”.
-In the “Type” drop-down box, select “Success”.
-In the “Applies to” drop-down box, select how the rule should be inherited:
-If the directory itself is always deleted, select “This folder only”.
-If sometimes just a subdirectory or file is deleted, select “This folder, subfolders, and files”.
-Click “Clear all” to uncheck the basic permissions.
-Click “Show advanced permissions”.
-Enable “Delete”. It should be the only enabled permission.
-Click OK to close the auditing entry dialog.
-Click OK to close the advanced security settings dialog.
-Click OK to close the properties dialog.

After one of the monitored directories or files gets mysteriously deleted or moved, open the management console’s event-viewer snap-in “eventvwr.msc”. Expand “Windows Logs”, and click “Security”. Click on the first event in the list, and press Ctrl+F to open the search box. Search for the name of the directory or file. If an event is found, double click on it to show the event properties. Among other things, the auditing event will show the user account, process ID, and process name that successfully opened the file or directory with delete access.

Once you no longer need access auditing, disable it in the security-policy snap-in, and remove the auditing rules from the directories.
```


