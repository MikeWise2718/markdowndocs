---
title: "Data Science Languages Cheatsheet"
output: 
  html_document:
     css: markdown.css
---

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


|Function	| R | 	Python |	Matlab/Octave |
| --------- |:---|:---------|:-----|
|help on "func" | ?func | help(func) | doc func |
|type of x |class(x) | type(x) | class(x) |
|Formatted print | print(sprintf(“pi:%$.2f”,pi))| print("pi:%.2f" % (numpy.pi)) | fprintf(“pi:%.2f”,pi)|
|for loop |for (j in 1:5){print(j)} |  for j in range(6)):<br>&nbsp;&nbsp;&nbsp;&nbsp;print(j) | for j=1:5 disp(j) end|
|list comprehension||  lst = [j for j in range(5)] | |
| while loop |while(TRUE){<br>&nbsp;&nbsp; print(j)<br>&nbsp;&nbsp;  break<br>&nbsp;&nbsp;  } |  while True:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(j)<br>&nbsp;&nbsp;&nbsp;&nbsp;break | while true<br>&nbsp;&nbsp; j<br>&nbsp;&nbsp;  break;<br>&nbsp;&nbsp; end|
|function |	f <- function(x,y){ x+y }	 | def f(x,y)<br>&nbsp;&nbsp;&nbsp;&nbsp; x+y | function val = f(x,y)<br>val = x + y;|


   


