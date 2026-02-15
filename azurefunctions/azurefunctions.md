---
title: "Azure Functions"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Serverless computing


# Troubleshooting connection to ASA
- Key post - https://stackoverflow.com/questions/46514057/stream-analytics-egress-to-azure-functions




# Python Functions
- Developer guide: (https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- Have to follow a certain file folder layout: (https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#folder-structure)
- You probably want to develop against Microsoft Store Python because that is what is deployed
- The Azure Function Template configured an environment in the `.venv` directory
- How to configure that: (https://code.visualstudio.com/docs/python/environments)
- This environment gets set and initialized with the `requirements.txt` before start up
- staring the host is the `func host start` command (or something like that)
- You can activate that environment from the terminal with `.venv\Scripts\activate.bat`
- you can then see what is installed with `pip freeze`
- kill the terminal with `exit`
- you might want to install or uninstall something
- you probably want to have a few `azure` modules as possible so don't just use `pip freeze` to make a `requirements.txt`
- see this"ModuleNotFoundError" article for dragons and hints about handcrafting `requirements.txt`
- (https://docs.microsoft.com/en-us/azure/azure-functions/recover-python-functions?tabs=vscode#troubleshoot-modulenotfounderror)


To debug it in VS Code you need a `launch.json` file in your `.vscode` directory something like this:
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Attach to Python Functions",
            "type": "python",
            "request": "attach",
            "port": 9091,
            "preLaunchTask": "func: host start"
        }
    ]
}
```
