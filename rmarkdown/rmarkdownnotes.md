---
title: "How R-markdown works"
output: html_document
---

## R Markdown Intro

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents.

This document also documents how R-markdown works for me, because I always forget what I have learned.

# Using it
That is the easy part. See here <http://rmarkdown.rstudio.com> for example.
Also check out the R-mardkwown Cheat Sheet: <http://www.rstudio.com/wp-content/uploads/2016/03/rmarkdown-cheatsheet-2.0.pdf>

## YAML
An R-markdown is really embedded in a YAML stream. YAML is a somewhat bizaar "data serialization language" - to be compared with JSON or XML a bit. Those are YAML directives at the top of this document, two documents seperated by "---" in a single stream (I think). The first document is refered to as the YAML header. Ugh.

## Compilation Flow
The cheatsheet above has some useful information on how R-markdown gets rendered under the section "Set render options with YAML". And man is this an archaic flow. While the output format can be pdf, or word, or a few others, we are mostly concered with HTML. It uses the knitr and the pandoc programs to do its thing. The flow looks like this:

 - An **xxx.rmd** file like this one is read into *knitr*
 - *knitr* spits out an **xxx.md** file
 - *pandoc* reads in the **xxx.md** file
 - *pandoc* creates the final **xxx.html** file
 
 you can do these from the R-console of course:
 




```r
summary(cars)
```

```
##      speed           dist       
##  Min.   : 4.0   Min.   :  2.00  
##  1st Qu.:12.0   1st Qu.: 26.00  
##  Median :15.0   Median : 36.00  
##  Mean   :15.4   Mean   : 42.98  
##  3rd Qu.:19.0   3rd Qu.: 56.00  
##  Max.   :25.0   Max.   :120.00
```

## Including Plots

You can also embed plots, for example:

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.
