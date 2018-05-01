---
title: "VI"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Okay, it is sort of stone age, but it is very useful. But I forgot a lot of it.

There are 4 essential modes

- `vi mode` (you can move around with the curors, ctrl-F, ctrl-B, h j k l)
- `input mode` (you can enter text- leave with `ESC`)
- `command mode` (als `ex` mode you have a: and the cursoris ther,e you can ender commands)
- `visual mode` - VIM only, you can mark a block with the `v` key and cursoring around

And a few esoteric ones
- `block visual mode` - Ctrl-V for rectangular editing

For more see this: - https://en.wikibooks.org/wiki/Learning_the_vi_Editor/Vim/Modes


# Startup
- Got my .vimrc from here:  https://gist.github.com/simonista/8703722 

# Search  (and replace)
- `/` to find, then enter `return` when you are done, then use `n` to jump to the next, and `N` (big n) to go backwards
- `*` on a word highlights all the words and then you can go back and forth with `n` and `N`
- `:noh` turns off the highlighting
- `%s/foo/bar/g` changes `foo` into `bar` everywhere

# Settings
- `:set` will display all options that are different from default
-  `echo &ft` will display the current ft setting
- `:verbose set autoread?`



# Turn off automatic wordrap
- There is this: http://vim.wikia.com/wiki/Toggle_auto-wrap
- And then there is this: https://stackoverflow.com/questions/1290285/why-cant-i-stop-vim-from-wrapping-my-code 
- I need to try this in my .vimrc
- `:set nowrap`  # turns off the apperans, but not the insertion of line breaks
- `:set textwidth=0`
- `:echo &ft`
- `:set textwidth=0 `
- `:set textwidth=0 `
- `:set wrapmargin=0`
- `:set formatoptions-=t` turns off autowrapping (this one actually works)

# Something Else
