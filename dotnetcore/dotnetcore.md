---
title: ".NET Core"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
* The new open-sourced cross-platform version of .Net
* Current version is 2.0
* Main Repo: https://github.com/dotnet/core

# Docs
* Docs: https://dotnet.github.io/
* Get Started: https://www.microsoft.com/net/learn/get-started/windows


# Dotnet commands
* They are documented here: https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet?tabs=netcore2x
* `dotnet new console` - makes a .dot net console app using the console template in the current directory
* `dotnet restore` - adds all the crap to make it work (from version 2.0 run automatically by new, build and run)
* `dotnet build` - build from the csproj in the directory
* `dotnet publish` - go get all the dlls and things you need to run this and copy everything needed to the bin directory
* `dotnet run something.dll` - runs it - note that if your program has changed, dotnet will run the 
* `dotnet --version` - query the version
* `dotnet new -l` - list all the templates


# Packages
* Can add from command window in VS Code (Open with ctrl-` (ctrl-backtick))
* `dotnet add package packagename` 
    * `dotnet add package Newtonsoft.Json` 
* `dotnet uninstall package packagename` 
* `dotnet nuget locals all --list` 

More info here: https://docs.microsoft.com/en-us/nuget/tools/dotnet-commands 

# Build File
* The build file is ths `*.csproj` file.


# Linking Libraries
* You probably want to start with a library template

* You need a section added to the build file that looks like this:
```
  <ItemGroup>
    <ProjectReference Include="..\h-common\h-common.csproj" />
  </ItemGroup>
```

# Current Version
As of 18 April 2018
```
C:\Users\mike>dotnet --version
2.1.2
```

# Templates
* `dotnet new -l`   - list available templates
```
C:\Users\mike>dotnet new -l
Usage: new [options]

Options:
  -h, --help          Displays help for this command.
  -l, --list          Lists templates containing the specified name. If no name is specified, lists all templates.
  -n, --name          The name for the output being created. If no name is specified, the name of the current directory is used.
  -o, --output        Location to place the generated output.
  -i, --install       Installs a source or a template pack.
  -u, --uninstall     Uninstalls a source or a template pack.
  --type              Filters templates based on available types. Predefined values are "project", "item" or "other".
  --force             Forces content to be generated even if it would change existing files.
  -lang, --language   Specifies the language of the template to create.


Templates                                         Short Name           Language          Tags
------------------------------------------------------------------------------------------------------------
Console Application                               console              [C#], F#, VB      Common/Console
Class library                                     classlib             [C#], F#, VB      Common/Library
Azure IoT Edge Module                             aziotedgemodule      [C#], F#          Console
Unit Test Project                                 mstest               [C#], F#, VB      Test/MSTest
xUnit Test Project                                xunit                [C#], F#, VB      Test/xUnit
ASP.NET Core Empty                                web                  [C#], F#          Web/Empty
ASP.NET Core Web App (Model-View-Controller)      mvc                  [C#], F#          Web/MVC
ASP.NET Core Web App                              razor                [C#]              Web/MVC/Razor Pages
ASP.NET Core with Angular                         angular              [C#]              Web/MVC/SPA
ASP.NET Core with React.js                        react                [C#]              Web/MVC/SPA
ASP.NET Core with React.js and Redux              reactredux           [C#]              Web/MVC/SPA
ASP.NET Core Web API                              webapi               [C#], F#          Web/WebAPI
global.json file                                  globaljson                             Config
NuGet Config                                      nugetconfig                            Config
Web Config                                        webconfig                              Config
Solution File                                     sln                                    Solution
Razor Page                                        page                                   Web/ASP.NET
MVC ViewImports                                   viewimports                            Web/ASP.NET
MVC ViewStart                                     viewstart                              Web/ASP.NET
```