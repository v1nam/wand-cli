import argparse


class Base:
    def run(self):
        prog = argparse.ArgumentParser(
            prog="wandbox",
            usage="%(prog)s [options] Language",
            description="Compile code snippets through the wandbox api for over 27 languages",
        )

        prog.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all the available languages",
        )

        prog.add_argument(
            "-f",
            "--file",
            type=str,
            help="Compile a file directly, full path to the file must be provided",
            required=False,
        )

        prog.add_argument(
            "-t",
            "--theme",
            type=str,
            help="Change the default theme (monokai) of code, to see available themes use -tl or --themelist",
            required=False,
        )

        prog.add_argument(
            "-tl",
            "--themelist",
            action="store_true",
            help="List all the available themes/colorschemes",
        )

        prog.add_argument(
            "Language",
            type=str,
            help="The language you want to compile.",
            nargs="?",
            default="python",
        )

        prog.add_argument(
            "-e",
            "--editor",
            type=str,
            help="""Open an editor of choice to write code in a temporary buffer\n
                    Please use a terminal editor for this, gui editors work differently \
                    and can cause unexpected behaviour.
                 """,
            required=False,
        )
        return prog.parse_args()


Base = Base()
