---
title: "Template Titles"
output: 
  html_document:
     css: ./markdown.css
---

# Intro
This is supposed to be a table showing how to do things in R, Python, and Matlab


Function	| R | 	Python |	Matlab
--------- | --|---------|-----
help on "func" | ?func | help(func) | doc func 
type of x |class(x) | type(x) | class(x) 
Formatted print | print(sprintf(“pi:%$.2f”,pi))| print("pi:%.2f" % (numpy.pi)) | fprintf(“pi:%.2f”,pi)
for loop |for (j in 1:5){print(j)} |  for j in range(6)):<br>&nbsp;&nbsp;&nbsp;&nbsp;print(j) | for j=1:5 disp(j) end
 list comprehension||  lst = [print(j) for j in range(5)] | |
 while loop |while(TRUE){<br>&nbsp;&nbsp; print(j)<br>&nbsp;&nbsp;  break<br>&nbsp;&nbsp;  } |  while True:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(j)<br>&nbsp;&nbsp;&nbsp;&nbsp;break | while true<br>&nbsp;&nbsp; print(j)<br>&nbsp;&nbsp;  break;<br>&nbsp;&nbsp; end
function |	f <- function(x,y){ x+y }	 | def f(x,y):<br>&nbsp;&nbsp;&nbsp;&nbsp; x+y | function val = f(x,y)<br>val = x + y;


   


