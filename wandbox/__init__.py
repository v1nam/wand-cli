#!/usr/bin/env python3

import argparse
import os, sys

from rich.console import Console

from wandbox.utilities.utils import Utils
from wandbox.utilities.maketable import MakeTable
from wandbox.commands import commands_dict
from wandbox.utilities.constants import themes, languages_table
from wandbox.utilities.compilers import compilers_
from wandbox.utilities.lang_extensions import lang_extensions


def main():
    console = Console()

    args = commands_dict["base"]()

    if args.list:
        console.print(MakeTable.mktbl(languages_table))
        Utils.close()

    if args.themelist:
        console.print(MakeTable.mktbl(themes))
        Utils.close()

    elif args.file:
        data = commands_dict["fromfile"](args.file)
        args.Language = lang_extensions[args.file[args.file.rfind(".")+1:]]
    
    elif args.editor:
        data = commands_dict["frombuffer"](args.Language, args.editor)

    else:
        data = commands_dict["frominput"](args.theme, args.Language)

    width = os.get_terminal_size().columns - 5

    try:
        if data.get("status") == "0":
            output = data["program_output"].strip()
            console.print(
                f"\nYour {args.Language} code ran successfully UwU", style="green"
            )

            console.print(Utils.print_msg_box(output, width=width))

        elif data.get("signal") == "Killed":
            output = data["program_output"][:100].strip()
            console.print(
                "\nYour {args.Language} code ran successfully with status Killed", style="yellow"
            )
            console.print(Utils.print_msg_box(output, width=width))
            console.print("Truncated, output is too long", style="yellow")

        else:
            for k in tuple(data.keys()):
                if "error" in k:
                    output = data[k].strip()
                    break
            console.print(f"\nYour {args.Language} code errored out ;(", style="red")
            console.print(Utils.print_msg_box(output, width=width))
    except KeyError:
        console.print(Utils.print_msg_box("No output", width=width))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error:\n{e}")
