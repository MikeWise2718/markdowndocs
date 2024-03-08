---
title: "grep"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
I use grep all the time but forget how to use it rather often.
It has some issues as there are several versions with different execution models.

# Grep
* Find proto messages `grep -r message . --include=*.proto`
* Sometimes there is a bug where it only finds things in the current direcotry - watch out for that


# Windows and Findstr
* There are various greps, you should use `where grep` to find out which one you are using
* But it is probably best to use `findstr` instead of `grep` to avoid the whole piping from `find` thing
* `findstr /s /i grep *.md`
* `findstr /s Findstr *.md`
* Findstr Caveats:
  *  if you forget to add a wildcard file specifier it just seems to hang while pretending to work - this has been a huge waste of my time in the past.

# Using gnu grep with windows and colosr
- If you have git installed and in your path, you can use grep in windows
- It colorizes better than findstr which will not highlight a matched string
- This worked for me `grep -r world . --include=*.py --color=always`
- Got this from SuperUser (https://superuser.com/questions/666577/grep-does-not-recurse-for-files-with-a-specific-extension)

# Linux
The whole `{} \;` thing is a bit mystifying, sometimes it works without it, sometimes it doesn't work no matter what you do. Googling didn't help. Probably should just use the grep recursive flag, but that has issues too.

- find files and pipe to grep - `find . -path '*/src/*.h' -exec grep PATTERN {} \;`
- same with filename and line - `find . -path '*/src/*.h' -exec grep -Hn PATTERN {} \;`
   - see this https://unix.stackexchange.com/questions/131535/recursive-grep-vs-find-type-f-exec-grep-which-is-more-efficient-faster
- Another example of finding with grep:   `find . -path '*.mk' -type f -exec grep -i 'UBUNTU_PKG_NAME =' {} +`
- After finding things we need to change: `find . -path '*.mk' -type f -exec sed -i 's/nvidia-367/nvidia-384/g' {} \;`
- change field 3 to AD - `awk '{$3 = "AD"; print}' infile > outfile`
- lookin in markdown for a whole word pattern 'iot' with file name and line number -- `find . -name '*.md' -exec grep -Hn -w iot {} \;`
- count how many hits -- `find . -name '*.md' -exec grep  -w iot {} \; | wc -l`
