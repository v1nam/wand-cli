#!/usr/bin/env python3

import argparse
import os, sys

from rich.console import Console

from wandbox.utilities.utils import Utils
from wandbox.utilities.maketable import MakeTable
from wandbox.commands import commands_dict
from wandbox.utilities.constants import themes, languages_table


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

    else:
        data = commands_dict["frominput"](args.theme)

    width = os.get_terminal_size().columns - 5

    try:
        if data.get("status") == "0":
            output = data["program_output"].strip()
            console.print(
                "\nYour code ran successfully with return code 0", style="green"
            )

            console.print(Utils.print_msg_box(output, width=width))

        elif data.get("signal") == "Killed":
            output = data["program_output"][:100].strip()
            console.print(
                "\nYour code ran successfully with status Killed", style="yellow"
            )
            console.print(Utils.print_msg_box(output, width=width))
            console.print("Truncated, output is too long", style="yellow")

        else:
            for k in tuple(data.keys()):
                if "error" in k:
                    output = data[k].strip()
                    break
            console.print("\nYour code errored out with return code 1", style="red")
            console.print(Utils.print_msg_box(output, width=width))
    except KeyError:
        console.print(Utils.print_msg_box("No output", width=width))


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"Error:\n{e}")
