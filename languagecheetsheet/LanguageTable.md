---
title: "Data Science Languages Cheatsheet"
output: 
  html_document:
     css: markdown.css
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Data Science Languages Cheetsheet
This is a table comparing syntax in R, Python, and Matlab/Octave 

Language Reference for [R](https://cran.r-project.org/doc/manuals/r-release/R-lang.html)<br>
Language Reference for [Python](https://docs.python.org/3/reference/index.html)<br>
Language Reference for [Matlab](https://www.mathworks.com/help/matlab/language-fundamentals.html?s_tid=gn_loc_drop)<br>

Cheatsheet for [R](https://cran.r-project.org/doc/contrib/Short-refcard.pdf)<br>
Cheatsheet for [Python 2.7](http://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html)<br>
Cheatsheet for [Python 3](http://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html)<br>
Cheatsheet for [Octave](http://www.lehman.edu/academics/cmacs/documents/refcard-a4.pdf)<br>

<style
  type="text/css">

table th {
   border: 1px solid blue;
   font-family:monospace;
   font-size:12px;
}

table td {
   border: 1px solid gray;
   font-family:monospace;
   font-size:9px;
   padding:0;
}

</style>

## Amost always imports
|  R | 	Python |	Matlab/Octave |
| --------- |:---|:---------|:-----|
| library(tidyverse) |import numpy as np|
|  | import pandas as pd|


## Basics
| Construct	| R | 	Python |	Matlab/Octave |
| --------- |:---|:---------|:-----|
|help on "func" | ?func | help(func) | doc func |
|comment | # comment | # comment | % comment |
| import | library | import | import
|string | "it's" or 'it"s' |"it's" or 'it"s' |   "it's" or 'it"s' (strings or chars) |
| int | 1234L | 1234 | 1234 |
| longint | none | switches transparently<br> even to bigints | int64(1234) |
|type of x |class(x) | type(x) | class(x) |
|Formatted print | print(sprintf(“pi:%$.2f”,pi))| print("pi:%.2f" % (numpy.pi)) | fprintf(“pi:%.2f”,pi)|


## Control
| Construct	| R | 	Python |	Matlab/Octave |
| --------- |:---|:---------|:-----|
|for loop |for (j in 1:5){print(j)} |  for j in range(6)):<br>&nbsp;&nbsp;&nbsp;&nbsp;print(j) | for j=1:5 disp(j) end|
|list comprehension||  lst = [j for j in range(5)] | |
| while loop |while(TRUE){<br>&nbsp;&nbsp; print(j)<br>&nbsp;&nbsp;  break<br>&nbsp;&nbsp;  } |  while True:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(j)<br>&nbsp;&nbsp;&nbsp;&nbsp;break | while true<br>&nbsp;&nbsp; j<br>&nbsp;&nbsp;  break;<br>&nbsp;&nbsp; end|
|function |	f <- function(x,y){ x+y }	 | def f(x,y)<br>&nbsp;&nbsp;&nbsp;&nbsp; x+y | function val = f(x,y)<br>val = x + y;|



## Arrays and Matrices
| Construct	| R | 	Python |	Matlab/Octave |
| --------- |:---|:---------|:-----|
| array | a = 1:3 | a = np.array([1,2,3]) | a = [1,2,3]
| matrix | m = matrix(1:4,2,2) | m = np.matrix('1 2; 3 4') | m = np.matrix('1 2; 3 4') 
| number of elements | length(m) | np.size(m) | numel(m)
| dimensions | dim(m) | np.shape(m) | size(m)
| list | l <- list(c(1,2,3)) | lst = [1,2,3] | not used much I think |



Data Frames might be [Tables in Matlab](https://blogs.mathworks.com/loren/2013/09/10/introduction-to-the-new-matlab-data-types-in-r2013b/)<br>
Intro to pandas [10 minutes to pandas](http://pandas.pydata.org/pandas-docs/version/0.15.2/10min.html)<br>

## Data Frames
| Construct	| R | 	Python |	Matlab/Octave |
| --------- |:---|:---------|:-----|
|Simple Data Frame| df <- data.frame(x=c(1,2,3),y=(4,5,6)) |  df = pd.DataFrame({ 'x' : [1,2,3],'y':[4,5,6] })    | ? |
|Read csv| df <- read.csv("mydata.csv") |  df = pd.read_csv('foo.csv')    | ? |
|Extract column| x <- df$x |  x = df.x    | ? |


   


