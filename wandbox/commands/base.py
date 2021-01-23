import argparse


class Base:
    def run(self):
        prog = argparse.ArgumentParser(
            prog="wandbox",
            description="Compile code snippets through the wandbox api for over 26 languages",
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
            help="Change the default theme (solarized-dark) of code, to see available themes use -tl or --themelist",
            required=False,
        )

        prog.add_argument(
            "-tl",
            "--themelist",
            action="store_true",
            help="List all the available themes/colorschemes",
        )

        args = prog.parse_args()

        return args


Base = Base()