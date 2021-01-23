from rich.table import Table


class MakeTable:
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
    ]

    def mktbl(self):
        """Make the language table from rich library."""
        l_table = Table(show_header=False)
        l_table.add_column(width=12, justify="center")
        l_table.add_column(width=12, justify="center")

        for lang in self.languages_table:
            l_table.add_row(lang[0], lang[1])
        return l_table


MakeTable = MakeTable()
