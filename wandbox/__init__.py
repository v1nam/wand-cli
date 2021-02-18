#!/usr/bin/env python3

import argparse
import os, sys
import json

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
        args.Language = lang_extensions[args.file[args.file.rfind(".") + 1 :]]

    elif args.editor:
        if args.Language == "none":
            args.Language = Utils.lang_prompt()
        data = commands_dict["frombuffer"](args.Language, args.editor)

    else:
        if args.Language == "none":
            args.Language = Utils.lang_prompt()

        if sys.platform == "linux" or sys.platform == "darwin":
            path = f"{os.environ.get('HOME', '')}/.config"
            if not os.path.isdir(path):
                os.mkdir(f"{os.environ.get('HOME', '')}/.config")
        elif "win" in sys.platform:
            path = os.getenv("APPDATA") + os.sep + ".wand"
            if not os.path.isdir(path):
                os.mkdir(path)
        try:
            content = open(f"{path}/wand.json")
        except FileNotFoundError:
            open(f"{path}/wand.json", "a")
            content = ""

        if not content or not content.read():
            with open(f"{path}/wand.json", "w") as config:
                json.dump({"theme": args.theme}, config)
        elif not args.theme:
            content = open(f"{path}/wand.json")
            args.theme = json.load(content)["theme"]
        else:
            file = open(f"{path}/wand.json")
            content = json.load(file)
            content["theme"] = args.theme
            json.dump(content, open(f"{path}/wand.json", "w"))

        data = commands_dict["frominput"](args.theme, args.Language)

    width = os.get_terminal_size().columns - 5

    try:
        if data.get("status") == "0":
            output = data["program_output"].strip()
            console.print(
                f"\nYour {args.Language} code ran successfully", style="green"
            )

            console.print(Utils.print_msg_box(output, width=width))

        elif data.get("signal") == "Killed":
            output = data["program_output"][:100].strip()
            console.print(
                "\nYour {args.Language} code ran successfully with status Killed",
                style="yellow",
            )
            console.print(Utils.print_msg_box(output, width=width))
            console.print("Truncated, output is too long", style="yellow")

        else:
            for k in tuple(data.keys()):
                if "error" in k:
                    output = data[k].strip()
                    break
            console.print(f"\nYour {args.Language} code errored out :(", style="red")
            console.print(Utils.print_msg_box(output, width=width))
    except KeyError:
        console.print(Utils.print_msg_box("No output", width=width))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error:\n{e}")
