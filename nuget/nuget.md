---
title: "NuGet"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
* .Net package manager
* Been around awhile - 2010
* Essentially a zip file with package artifacts (javascript, dlls, etc.)


# Login
* https://www.nuget.org/
* User is MikeWise
* Email is mwise@mothership.com
* Uses corp login so no password

# How to
* See your packages - login with your account and go to username/Manage Packages: <https://www.nuget.org/account/Packages>
* Create and publish with the dotnet CLI - https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package-using-the-dotnet-cli

# Example
- Manage your published nugets on <https://www.nuget.org/>
    - Login name is `MikeWise`
    - Email is `mwise@somecompany.com`
- API key: `YOUR_NUGET_API_KEY`
- Key will expire one year from 7 Feb 2019 (when I created it)
- Command to push library to nuget.org: 
    - increment the version number in `common.csproj`
    - `dotnet build` as usual
    - then change to directory with nuget package (`.\bin\Debug\`) 
    - then enter `dotnet nuget push .\VafspLib.1.0.0.nupkg -k YOUR_NUGET_API_KEY -s https://api.nuget.org/v3/index.json`
    - then wait for it to publish, which can take up to an hour