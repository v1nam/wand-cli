from pygments.styles import get_all_styles
from rich.table import Table


class MakeTable:
    def mktbl(self, cont):
        """Make a table list from rich library."""
        l_table = Table(show_header=False)
        l_table.add_column(width=12, justify="center")
        l_table.add_column(width=12, justify="center")

        for lang in cont:
            l_table.add_row(lang[0], lang[1])
        return l_table


MakeTable = MakeTable()
