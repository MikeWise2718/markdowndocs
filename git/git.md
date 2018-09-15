---
title: "Data Science Languages Cheatsheet"
output: 
  html_document:
     css: markdown.css
---
[up](https://mikewise2718.github.io/markdowndocs/)

# All things git
[Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)<br>
[Git Documentation](https://git-scm.com/docs)<br>
[Visual Git Doc](https://marklodato.github.io/visual-git-guide/index-en.html)<br>
[Basic Git Commands](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html)<br>
[Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)<br>
[Things to hate about it](https://stevebennett.me/2012/02/24/10-things-i-hate-about-git/)
[GitHub etiquette](https://help.github.com/articles/fork-a-repo/)


# Newest version
[Download](http://git-scm.com/downloads)


## User Profile Information
 - There are 3 default paths for the config file (on linux at least).
   - ref: https://stackoverflow.com/questions/7328826/curious-where-does-git-store-user-information 
   - Repository itself: `<your_git_repository>/.git/config`
   - User home directory: `~/.gitconfig`
   - System-wide directory: `$(prefix)/etc/gitconfig`


## Command line sequence
- `git add -A .`
- `git commit -m "message"`
- `git push`
git config --global credential.helper 'cache --timeout=3600'

## Password Caching
- There are lots of ways to approach this
- Login using `ssh` instead of `https`
- Use "Credential Helper"
   - $ git config --global credential.helper cache  # Tell git to use the credential helper
   - $ git config --global credential.helper 'cache --timeout=3600' # Set the timeout to 1 hour 


## Git Log
- `git log --oneline` - one line form of log
- `git log --pretty=format:"%h%x09%an%x09%ad%x09%s"` - short form with date (see this: https://stackoverflow.com/a/1441062/3458744)
- `git log --pretty="%C(Yellow)%h  %C(reset)%ad (%C(Green)%cr%C(reset))%x09 %C(Cyan)%an: %C(reset)%s"` - colors log with date 
- `git log -p Assets/_scripts/GraphAlgos.cs` - get the diff history of a file
- 

## Git Ignore
- `**.jpg` - No jpgs in this direcory and any others

## Favorites

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



| Construct	| git | git gui | VSCode | 	Visual Studio
| --------- |:----|:--------|:-------|:--------------|
| init a repo | git init |  |   |
| add all cnanges | git add -A | | Under "..."   |
| commit changes to staging | git commit -m "msg" | | Under "..."   |
| push changes to remote master | git push | | Under "..."   |
| view status | git status | |   |
| view user name | git config user.name | | |
| view user email | git config user.email |
| see all settings | git config -l |
| set user name | git config --global user.name "Mike Wise" |
| set user email | git config --global user.email mwise@oz.ai |
| ![fish](SmallerFish.png) | git config --global user.email mwise@oz.ai |



   


