# Wandbox Cli
A cli tool which uses the wandbox api to compile over 26 languages instantly, [Wandbox](http://melpon.org/wandbox/) is a social compilation service.

![](wandbox_preview_cli.gif)

**Note**: The time for the output totally depends upon how fast your internet can make a post request, it can be as slow as mine or instantaneous

# Installation
You can install it with the python package manager `pip`
```sh
pip install wand-cli
```
After installing with pip, you will have the command available for you, so you can directly run by
```sh
wandbox [OPTIONS]
```  

## Commands
If you run the command without any option provided, you will be asked for the language name and then you can write your code in the terminal directly, and run it by pressing `esc + enter`  
### list
The list command, `wandbox --list` or `wandbox -l` is used to show the list of languages available.  
### file
The file command, `wandbox --file [FILE PATH]` or `wandbox -f [FILE PATH]` is used to compile a file.  
### theme
The theme command, `wandbox --theme [theme name]` or `wandbox -t [theme name]` is used to change the colorscheme for the in-place text editor  
### themelist
The themelist command (`wandbox --themelist` or `wandbox -tl`) is used to list all the available color schemes.  
### help
The help command, `wandbox --help` or `wandbox -h` shows a brief description on the command.  

# Languages
Here's a list of the languages which are available.
|     ..     |     ..     |
| :--------: | :--------: |
| python     | f#         |
| c++        | scala      |
| c          | swift      |
| javascript | typescript |
| java       | vim        |
| haskell    | lua        |
| bash       | nim        |
| cmake      | php        |
| elixir     | perl       |
| d          | pony       |
| sqlite     | go         |
| lisp       | ruby       |
