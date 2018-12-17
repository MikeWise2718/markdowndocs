---
title: "TensorFlowSharp"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
* Miguel Deicaza's foray into Tensorflow
* Repo is here: <https://github.com/migueldeicaza/TensorFlowSharp>
* Installing


# Testing
There are no instructions for testing. So I did the following:
* created a TensorflowSharp directory (bad name it turned out)
* created a console project in that directory
* added the sampe program after the Program.cs template giving me this:
```
using System;
using TensorFlow;

namespace tensorflowsharptest
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            using (var session = new TFSession())
			{
				var graph = session.Graph;

				var a = graph.Const(2);
				var b = graph.Const(3);
				Console.WriteLine("a=2 b=3");

				// Add two constants
				var addingResults = session.GetRunner().Run(graph.Add(a, b));
				var addingResultValue = addingResults.GetValue();
				Console.WriteLine("a+b={0}", addingResultValue);

				// Multiply two constants
				var multiplyResults = session.GetRunner().Run(graph.Mul(a, b));
				var multiplyResultValue = multiplyResults.GetValue();
				Console.WriteLine("a*b={0}", multiplyResultValue);
			}
        }
    }
}
```
- Got a cycle error
```
D:\transfer\tensorflowsharp>dotnet build
Microsoft (R) Build Engine version 15.7.179.6572 for .NET Core
Copyright (C) Microsoft Corporation. All rights reserved.

  Restoring packages for D:\transfer\tensorflowsharp\tensorflowsharp.csproj...
D:\transfer\tensorflowsharp\tensorflowsharp.csproj : error NU1108: Cycle detected.
D:\transfer\tensorflowsharp\tensorflowsharp.csproj : error NU1108:   tensorflowsharp -> TensorFlowSharp (>= 1.12.0).
  Restore failed in 187.84 ms for D:\transfer\tensorflowsharp\tensorflowsharp.csproj.

Build FAILED.
D:\transfer\tensorflowsharp>
```
- fixed that by changing the namespace to tfsharptest
- got it to compile by adding a packagereference to the csproj
```
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>netcoreapp2.1</TargetFramework>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="TensorFlowSharp" Version="1.12.0" />
  </ItemGroup>
</Project>
```
* did a `dotnet run`, and it then  failed with 
```
Unhandled Exception: System.TypeLoadException: Could not load type 'TensorFlow.TFSession' from assembly 'tensorflowsharp, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null'.
   at tfsharptest.Program.Main(String[] args)
```
* then compiled with `dotnet run --runtime win10-x64` - it installed some new packages and compiled
* `dotnet run` Still failed with the same error as above 
* changed directory to: `cd D:\transfer\tensorflowsharp\bin\Debug\netcoreapp2.1\win10-x64` and ran `tftest.exe` directly
* It worked with this output:
```
D:\transfer\tensorflowsharp\bin\Debug\netcoreapp2.1\win10-x64>tftest
Hello World!
2018-12-15 13:46:31.950668: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
a=2 b=3
a+b=5
a*b=6
```
