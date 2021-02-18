# Wandbox Cli
A cli tool which uses the wandbox api to compile over 26 languages instantly, [Wandbox](http://melpon.org/wandbox/) is a social compilation service.

![](wandbox_preview_cli.gif)

**Note**: The time for the output totally depends upon how fast your internet can make a post request, it can be as slow as mine or instantaneous

# Installation

## Arch Linux
You can install through the `AUR`
```sh
yay -S wand
```
## Pip
You can install it with the python package manager `pip`
```sh
pip install wand-cli
```
After installing with pip, you will have the command available for you, so you can directly run by
```sh
wand [OPTIONS] language
```  

## Commands
If you run the command without any option provided, you will be asked for the language name and then you can write your code in the terminal directly, and run it by pressing `esc + enter`  
### list
The list command, `wand --list` or `wand -l` is used to show the list of languages available.  
### file
The file command, `wand --file [FILE PATH]` or `wand -f [FILE PATH]` is used to compile a file.  
### editor
The editor command, `wand --editor [editor-name]` or `wand -e [editor-name]` is used to open a temporary buffer in an editor to edit files, the code is run after the editor is closed, **note**: its recommended to use a terminal editor for this, gui editors can cause unexpected behaviour.  
### theme
The theme command, `wand --theme [theme name]` or `wand -t [theme name]` is used to change the colorscheme for the in-place text editor  
### themelist
The themelist command (`wand --themelist` or `wand -tl`) is used to list all the available color schemes.  
### help
The help command, `wand --help` or `wand -h` shows a brief description on the command.  

# Languages
Here's a list of the languages which are available.  

```
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃    python    ┃      f#      ┃
│     c++      │    scala     │
│      c       │    swift     │
│  javascript  │  typescript  │
│     java     │     vim      │
│   haskell    │     lua      │
│     bash     │     nim      │
│   crystal    │     php      │
│    elixir    │     perl     │
│      d       │     pony     │
│    sqlite    │      go      │
│     lisp     │     ruby     │
│      c#      │ coffeescript │
│     rust     │              │
└──────────────┴──────────────┘

```
