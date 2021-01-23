import pygments
from pygments.styles import get_all_styles
from wandbox.colorschemes import schemes


def init_lexers():
    pygments.lexers.find_lexer_class_by_name("D")
    pygments.lexers.find_lexer_class_by_name("ruby")
    pygments.lexers.find_lexer_class_by_name("rust")
    pygments.lexers.find_lexer_class_by_name("sql")
    pygments.lexers.find_lexer_class_by_name("lisp")
    pygments.lexers.find_lexer_class_by_name("go")
    pygments.lexers.find_lexer_class_by_name("f#")
    pygments.lexers.find_lexer_class_by_name("scala")
    pygments.lexers.find_lexer_class_by_name("swift")
    pygments.lexers.find_lexer_class_by_name("typescript")
    pygments.lexers.find_lexer_class_by_name("vim")
    pygments.lexers.find_lexer_class_by_name("lua")
    pygments.lexers.find_lexer_class_by_name("nim")
    pygments.lexers.find_lexer_class_by_name("php")
    pygments.lexers.find_lexer_class_by_name("elixir")
    pygments.lexers.find_lexer_class_by_name("python")
    pygments.lexers.find_lexer_class_by_name("cpp")
    pygments.lexers.find_lexer_class_by_name("c")
    pygments.lexers.find_lexer_class_by_name("javascript")
    pygments.lexers.find_lexer_class_by_name("coffeescript")
    pygments.lexers.find_lexer_class_by_name("java")
    pygments.lexers.find_lexer_class_by_name("haskell")
    pygments.lexers.find_lexer_class_by_name("bash")
    pygments.lexers.find_lexer_class_by_name("cmake")
    pygments.lexers.find_lexer_class_by_name("crystal")
    pygments.lexers.find_lexer_class_by_name("perl")
    pygments.lexers.find_lexer_class_by_name("pony")
    pygments.lexers.find_lexer_class_by_name("c#")


init_lexers()

lexers_dict = {
    "python": pygments.lexers.python.PythonLexer,
    "c++": pygments.lexers.c_cpp.CppLexer,
    "c#": pygments.lexers.dotnet.CSharpLexer,
    "cpp": pygments.lexers.c_cpp.CppLexer,
    "c": pygments.lexers.c_cpp.CLexer,
    "javascript": pygments.lexers.javascript.JavascriptLexer,
    "js": pygments.lexers.javascript.JavascriptLexer,
    "coffeescript": pygments.lexers.javascript.CoffeeScriptLexer,
    "cs": pygments.lexers.javascript.CoffeeScriptLexer,
    "java": pygments.lexers.jvm.JavaLexer,
    "haskell": pygments.lexers.haskell.HaskellLexer,
    "bash": pygments.lexers.shell.BashLexer,
    "cmake": pygments.lexers.make.CMakeLexer,
    "crystal": pygments.lexers.crystal.CrystalLexer,
    "elixir": pygments.lexers.erlang.ElixirLexer,
    "d": pygments.lexers.d.DLexer,
    "ruby": pygments.lexers.ruby.RubyLexer,
    "rust": pygments.lexers.rust.RustLexer,
    "sql": pygments.lexers.sql.SqlLexer,
    "sqlite": pygments.lexers.sql.SqlLexer,
    "lisp": pygments.lexers.lisp.CommonLispLexer,
    "go": pygments.lexers.go.GoLexer,
    "f#": pygments.lexers.dotnet.FSharpLexer,
    "scala": pygments.lexers.jvm.ScalaLexer,
    "swift": pygments.lexers.objective.SwiftLexer,
    "typescript": pygments.lexers.javascript.TypeScriptLexer,
    "ts": pygments.lexers.javascript.TypeScriptLexer,
    "vim": pygments.lexers.textedit.VimLexer,
    "lua": pygments.lexers.scripting.LuaLexer,
    "nim": pygments.lexers.nimrod.NimrodLexer,
    "php": pygments.lexers.php.PhpLexer,
    "perl": pygments.lexers.perl.PerlLexer,
    "pony": pygments.lexers.pony.PonyLexer,
}

spinners = [
    "point",
    "dots",
    "dots12",
    "dots9",
    "dots2",
    "simpleDotsScrolling",
    "bouncingBall",
]

themes = list(get_all_styles()) + schemes
themes = [list(themes[style : style + 2]) for style in range(0, len(themes), 2)]

languages_table = [
    ("python", "f#"),
    ("c++", "scala"),
    ("c", "swift"),
    ("javascript", "typescript"),
    ("java", "vim"),
    ("haskell", "lua"),
    ("bash", "nim"),
    ("cmake", "php"),
    ("elixir", "perl"),
    ("d", "pony"),
    ("sqlite", "go"),
    ("lisp", "ruby"),
    ("c#",),
]
