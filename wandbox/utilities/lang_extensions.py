from wandbox.utilities.compilers import compilers_

lang_extensions = {
    "py": "python",
    "cpp": "cpp",
    "cpp": "c++",
    "c": "c",
    "js": "javascript",
    "coffee": "coffeescript",
    "java": "java",
    "hs": "haskell",
    "bash": "bash",
    "cr": "crystal",
    "exs": "elixir",
    "d": "d",
    "rb": "ruby",
    "rs": "rust",
    "sql": "sqlite",
    "lisp": "lisp",
    "go": "go",
    "fs": "f#",
    "scala": "scala",
    "swift": "swift",
    "ts": "typescript",
    "vim": "vim",
    "lua": "lua",
    "nim": "nim",
    "php": "php",
    "pl": "perl",
    "pony": "pony",
    "cs": "c#"
}

lang_extensions_ = {i:compilers_[v] for i,v in lang_extensions.items()}
lang_names = {v:i for i,v in lang_extensions.items()}
