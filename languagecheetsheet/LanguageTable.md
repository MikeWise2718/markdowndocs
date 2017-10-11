---
title: "Data Science Languages Cheatsheet"
output: 
  html_document:
     css: markdown.css
---

# Intro
This is a table comparing syntax in R, Python, and Matlab

<style
  type="text/css">

table th {
   border: 1px solid green;
   font-family:monospace;
   font-size:12px;
}

table td {
   border: 1px solid blue;
   border-bottom-color: blue;
   border-top-color: blue;
   border-left-color: blue;
   border-right-color: blue;
   font-family:monospace;
   font-size:9px;
   padding:0;
}

</style>


|Function	| R | 	Python |	Matlab |
| --------- |:---|:---------|:-----|
|help on "func" | ?func | help(func) | doc func |
|type of x |class(x) | type(x) | class(x) |
|Formatted print | print(sprintf(“pi:%$.2f”,pi))| print("pi:%.2f" % (numpy.pi)) | fprintf(“pi:%.2f”,pi)|
|for loop |for (j in 1:5){print(j)} |  for j in range(6)):<br>&nbsp;&nbsp;&nbsp;&nbsp;print(j) | for j=1:5 disp(j) end|
| list comprehension||  lst = [print(j) for j in range(5)] | |
| while loop |while(TRUE){<br>&nbsp;&nbsp; print(j)<br>&nbsp;&nbsp;  break<br>&nbsp;&nbsp;  } |  while True:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(j)<br>&nbsp;&nbsp;&nbsp;&nbsp;break | while true<br>&nbsp;&nbsp; j<br>&nbsp;&nbsp;  break;<br>&nbsp;&nbsp; end|
|function |	f <- function(x,y){ x+y }	 | def f(x,y)<br>&nbsp;&nbsp;&nbsp;&nbsp; x+y | function val = f(x,y)<br>val = x + y;|


   


