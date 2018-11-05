  **
title: "Data Science Languages Cheatsheet"
output: 
  html_document:
     css: markdown.css
  **
[up](https://mikewise2718.github.io/markdowndocs/)

# All things git
[Git Basics](https://git*scm.com/book/en/v2/Getting*Started*Git*Basics)<br>
[Git Documentation](https://git*scm.com/docs)<br>
[Visual Git Doc](https://marklodato.github.io/visual*git*guide/index*en.html)<br>
[Basic Git Commands](https://confluence.atlassian.com/bitbucketserver/basic*git*commands*776639767.html)<br>
[Git Cheatsheet](https://education.github.com/git*cheat*sheet*education.pdf)<br>
[Things to hate about it](https://stevebennett.me/2012/02/24/10*things*i*hate*about*git/)
[GitHub etiquette](https://help.github.com/articles/fork*a*repo/)
[Merging vs. Rebasing](https://www.atlassian.com/git/tutorials/merging*vs*rebasing)

# Concepts you should know
 * blob  (how it is hashed, how it is compressed)
     * blobs are object stored in the .git/objects in subdirectories/files based on their SHA*1 hashes
     * they don't know anything about themselves (no metadata) 
     * they are compressed using something or other
     * you can garbage collect blobs that are not being pointed to from anyone
     * short sha-1 hashes (https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#Short-SHA-1)
     * `git show aa5f86`  - shows the object that belongs to the hash
 * trees  
    * trees are blob objects
    * they contain a list of the blobs they hold and maybe a subdirectory tree
    * for every entry they have a limited UNIX*like type permission code and the file/subdir name
 * commits 
    * commits are also blob objects
    * have a message in their body
    * have a pointer to a tree that belongs to them
    * Viewing commits  `git log` - see below, but this is [good](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
    * commit branch membership is fluent - original branch of a commit is not tracked
 * refs (what is in them, how to look at them)
     * refs are also blob objects (I think)
     * refs point to a commit
     * each branches has a head refs
     * `git show-ref`
 * index
     * a binary file in .git/index
     * not a blob object
     * lists everything that has been staged up to now
 * branches
     * just a head ref really, I think
     * `git branch` lists all branches
     * `git checkout master` changes HEAD (current branch) to point to master REF
     * `git merge branch1910`  merges current branch with branch1910 (merged the commit corresponding to the head of branch1910 with the commit cooresponding to the current HEAD)
     * `git checkout -b newbranch` - create a new branch "newbranch" (create a ref pointint go the current commit)
     * `git push --set-upstream origin locredwest` -- create that branch upstream
 * remotes
     * a listing of remote repositories (their ip address) that you can fetch from
     * if you pull, that does a merge right after as well
     * `git remotes -v`
     * `git remote show origin`
 * HEAD
     * the commit you are currently working on 
     * `git show HEAD`


## Branching concepts
 * heads
 * HEAD not on the branch head
 * fast forward
 * rebaseing
 * refspec (https://git-scm.com/book/en/v2/Git-Internals-The-Refspec)

## More advanced stuff
 * plumbing instead of porceline (git is a content*addressable file system) [git internals](https://git*scm.com/book/en/v1/Git*Internals)
 * what your mental model should be [git for computer scientists](http://eagain.net/articles/git*for*computer*scientists/)
 * Driessen on branching models [a successful Git branching model](https://nvie.com/posts/a*successful*git*branching*model/)
 * Git is your friend not a foe (v2,v3,v4 are great) [git as friend](https://hades.github.io/2010/01/git*your*friend*not*foe/)
 * git didn't beat SVN, GitHub [did](https://blog.gitprime.com/git*didnt*beat*svn*github*did/)
 * why you should not [rebase](https://medium.com/@fredrikmorken/why-you-should-stop-using-git-rebase-5552bee4fed1)
 * git [workflows](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows)
 * commits do not know their branch (https://community.atlassian.com/t5/Bitbucket-questions/Knowing-from-which-branch-the-current-branch-was-created-from/qaq-p/570135)

# Newest version
[Download](http://git*scm.com/downloads)


## User Profile Information
 * There are 3 default paths for the config file (on linux at least).
   * ref: https://stackoverflow.com/questions/7328826/curious*where*does*git*store*user*information 
   * Repository itself: `<your_git_repository>/.git/config`
   * User home directory: `~/.gitconfig`
   * System*wide directory: `$(prefix)/etc/gitconfig`


## Command line sequence
* `git add *A .`
* `git commit *m "message"`
* `git push`
git config   *global credential.helper 'cache   *timeout=3600'

## Password Caching
* There are lots of ways to approach this
* Login using `ssh` instead of `https`
* Use "Credential Helper"
   * $ git config   *global credential.helper cache  # Tell git to use the credential helper
   * $ git config   *global credential.helper 'cache   *timeout=3600' # Set the timeout to 1 hour 


## Git Log
* `git log   --oneline` * one line form of log
* `git log   --pretty=format:"%h%x09%an%x09%ad%x09%s"` * short form with date - see this: (https://stackoverflow.com/a/1441062/3458744)
* `git log   --pretty="%C(Yellow)%h  %C(reset)%ad (%C(Green)%cr%C(reset))%x09 %C(Cyan)%an: %C(reset)%s"` * colors log with date 
* `git log --p Assets/_scripts/GraphAlgos.cs` * get the diff history of a file
* The above commands should have "--" as flag switches
* `git log --follow -p -- filename`   -follow the history of a file

## Git Ignore
* `  *.jpg` * No jpgs in this direcory and any others

## Git Aliases
* Explained here
* a good template can be found here:(https://stackoverflow.com/a/52896091/3458744)

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
| --------- |:----|:--------|:--------------|:------|
| init a repo | git init |  |   |
| add all cnanges | git add *A | | Under "..."   |
| commit changes to staging | git commit *m "msg" | | Under "..."   |
| push changes to remote master | git push | | Under "..."   |
| view status | git status | |   |
| view user name | git config user.name | | |
| view user email | git config user.email |
| see all settings | git config *l |
| set user name | git config   *global user.name "Mike Wise" |
| set user email | git config   *global user.email mwise@oz.ai |
| ![fish](SmallerFish.png) | git config   *global user.email mwise@oz.ai |



   


