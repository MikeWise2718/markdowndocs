---
title: "Bash"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Shebang bin bash
- Getting started - https://www.linux.com/learn/writing-simple-bash-script
- 

# Interesting scripts
Change a directory - cdod - (has to be called with a ".", as in ". cdod")
```
#!/bin/bash
cd /home/mike/tfrepos/models/research/object_detection
```

File Diff - vapydiff
```
#!/bin/bash
SDIR=/home/mike/tfrepos/models/research/object_detection/
DDIR=/home/mike/vafsb/h-mod/h-objdet/vapy/
find . -name "va_*.py" -exec diff -q {}  $DDIR{} \;
```

Delete lots of stuff - camclean
```
#!/bin/bash
sudo find /mass/vafsb/imcap -name "c*.jpg"  -delete
sudo find /mass/vafsb/imcap/pyOutput -name "*.txt"  -delete
sudo find /mass/vafsb/imcap/output_redaction -name "*.csv"  -delete
sudo find /mass/vafsb/imcap/output_redaction/boxplots/ -name "*.jpg"  -delete
sudo find /mass/vafsb/imcap/output_redaction/redacted/ -name "*.jpg"  -delete
sudo find /mass/vafsb/imcap/output_redaction/cropped/ -name "*.jpg"  -delete

```