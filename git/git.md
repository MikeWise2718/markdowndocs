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

# Tutorials
 * I really liked David Mahler's systematic approach https://www.youtube.com/channel/UCEoaojfEY_6L5TWWjIn9t9Q
   * lots of great commands in there summarized in the YouTube video header
 * This guy - Dan Gitschooldude - has a very large number around many specialized topics. Quality varies from very good to "meh": https://www.youtube.com/channel/UCshmCws1MijkZLMkPmOmzbQ
 * John Britton Pretty detailed tutorial on how git works internally: https://www.youtube.com/watch?v=lG90LZotrpo
 * John Scott Chacon of GitHubs lecture: https://www.youtube.com/watch?v=ZDR433b0HJY 

# Concepts you should know
 * Working folder
     * the folder you are working on
 * Index or Staging area 
     * the files that will make up the next commit (if you do one now)
 * blob  (how it is hashed, how it is compressed)
     * blobs are object stored in the .git/objects in subdirectories/files based on their SHA*1 hashes
     * they don't know anything about themselves (no metadata) 
     * they are compressed using something or other
     * you can garbage collect blobs that are not being pointed to from anyone
     * short sha-1 hashes (https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#Short-SHA-1)
     * `git show aa5f86`  - shows the object that belongs to the hash
 * trees  
    * trees are blob objects that can be thought of as pointing to a directory
    * tree-ish is something that might eventual resolve to a tree - like HEA
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
 * HEAD
     * The ref that points to the current checkout commit (the one you can see in the directory)
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


## Stage changes, commit, and push t omaster command line sequence
* `git add -A .`
* `git commit -m "message"`
* `git push`

## Checkout a new branch
* Git help: <https://gist.github.com/markSci5/5916003>
* `git branch <branch_name>` followed by `git checkout <branch_name>`
* or just `git checkout -b <branch_name>`

## Merge branch
* Git Help <https://help.github.com/articles/merging-an-upstream-repository-into-your-fork/>
*  `git checkout master` 
*  `git pull` 
*  Resolve conflicts
* 

git config   -global credential.helper 'cache   -timeout=3600'

## Password Caching
* There are lots of ways to approach this
* Login using `ssh` instead of `https`
* Use "Credential Helper"
   * $ git config   -global credential.helper cache  # Tell git to use the credential helper
   * $ git config   -global credential.helper 'cache   -timeout=3600' # Set the timeout to 1 hour 

## Undo commit
- From (https://www.reddit.com/r/git/comments/ep40we/how_to_undo_a_commit_in_git/)
- Medium article: (https://itnext.io/how-to-undo-a-commit-in-git-2c7d49deabe0)
- Softway: `git revert HEAD` - this leaves a record
- Hardway: `git reset HEAD~ --hard` - this leaves no record


## Git Log
* `git log   --oneline` * one line form of log
* `git log   --pretty=format:"%h%x09%an%x09%ad%x09%s"` * short form with date - see this: (https://stackoverflow.com/a/1441062/3458744)
* `git log   --pretty="%C(Yellow)%h  %C(reset)%ad (%C(Green)%cr%C(reset))%x09 %C(Cyan)%an: %C(reset)%s"` * colors log with date 
* `git log --p Assets/_scripts/GraphAlgos.cs` * get the diff history of a file
* The above commands should have "--" as flag switches
* `git log --follow -p -- filename`   -follow the history of a file

## Git Ignore
* `  *.jpg` * No jpgs in this directory and any others
* Note that gitignore will not ignore a directory that is alread in the repo
* You have to delete it explicity - see this: (https://stackoverflow.com/questions/24290358/remove-a-folder-from-git-tracking)
* Whitelisting files -  mostly doesn't work becaues after blacklisting the directory won't be scanned and indexed so the whitelisted files will not be known by git
* See this: (https://stackoverflow.com/a/52295765/3458744)

## Git Replace
- Finally - as of version 2.23 (https://stackoverflow.com/a/58019011/3458744)
```
git fetch
git restore -s origin/master -- path/to/file
```


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

# Unfork Repo
Got it from here: (https://intellipaat.com/community/21779/unfork-github-how-to-unfork-the-github-repository)
How to "unfork" a project in four easy steps:

1. git clone --bare https://github.com/{username}/{repository}

2. Delete original repository in https://github.com/{username}/{repository}/settings.

3. Create new repository with the name {repository} at https://github.com/new.

4. cd {repository}.git and git push --mirror https://github.com/{username}/{repository}


   
# Keeping up to date
- Link here: (https://stefanbauer.me/articles/how-to-keep-your-git-fork-up-to-date)
- I think this is all assuming you are only working on one branch, "master"
- Basically
  1. `git fetch upstream`
  2. `git status` (see how up to date it is)
  3. `git merge upstream/master master`
  4. `git push`

- If you have been adding work, you should be adding to a branch

   4. `git rebase upstream/master`


# Rename a branch
A stack overflow answer (https://stackoverflow.com/a/6591218/3458744)
 1. Rename with  `git branch -m <oldname> <newname>` 
 2. Can use capital M of force rename if newbranch exists, or windows upper/lower case madness
 
 A Better answer: (https://linuxize.com/post/how-to-rename-local-and-remote-git-branch/)
 1. Switch to that local branch with `git checkout <oldname>`
 2. Rename the local branch with `git branch -m <newname>`
 3. Push new name and reset the upstream branch with: `git push origin -u <newname>`
 4. Delete <oldname> remote branch: `git push origin --delete <oldname>`


# see what changed betwen branches
- diff between branches -  `git diff --name-status master`
```
git diff --name-status master
M       com.unity.ml-agents/Runtime/Academy.cs
M       com.unity.ml-agents/Runtime/Agent.cs
M       com.unity.ml-agents/Runtime/Communicator/RpcCommunicator.cs
A       ml-agents/ml-agents-env/mlagents_envs/base_env.py
A       ml-agents/ml-agents-env/mlagents_envs/communicator.py
A       ml-agents/ml-agents-env/mlagents_envs/environment.py
A       ml-agents/ml-agents-env/mlagents_envs/exception.py
A       ml-agents/ml-agents-env/mlagents_envs/rpc_communicator.py
A       ml-agents/ml-agents-env/mlagents_envs/rpc_utils.py
A       ml-agents/ml-agents/mlagents/trainers/agent_processor.py
M       ml-agents/mlagents/trainers/agent_processor.py
A       ml-agents/protobuf-definitions/proto/mlagents_envs/communicator_objects/environment_statistics.proto
A       ml-agents/protobuf-definitions/proto/mlagents_envs/communicator_objects/unity_rl_output.proto
```
- diff between branches and one specific file
    - `git diff  custom-tb-obs -- Project/ProjectSettings/ProjectVersion.txt`   
```
diff --git a/Project/ProjectSettings/ProjectVersion.txt b/Project/ProjectSettings/ProjectVersion.txt
index d364145c..9bebbca9 100644
--- a/Project/ProjectSettings/ProjectVersion.txt
+++ b/Project/ProjectSettings/ProjectVersion.txt
@@ -1,6 +1 @@
-<<<<<<< HEAD
-m_EditorVersion: 2019.3.3f1
-m_EditorVersionWithRevision: 2019.3.3f1 (7ceaae5f7503)
-=======
 m_EditorVersion: 2018.4.18f1
->>>>>>> upstream/master
```
- replace that file with the one in another branch
   - `git  checkout  custom-tb-obs Project/ProjectSettings/ProjectVersion.txt`   

## Interactive rebasing
- Useful commands
- `git log --oneline --graph`
- `git log --oneline --graph -10`
- `git rev-parse HEAD~2`
- `git -i rebase HEAD~2