import argparse
import os

from rich.console import Console

from commands.frominput import FromInput
from commands.fromfile import FromFile
from utilities.utils import Utils
from utilities.maketable import MakeTable

console = Console()

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

args = prog.parse_args()

if args.list:
    console.print(MakeTable.mktbl())
    Utils.close()

if args.file:
    data = FromFile.runfile(args.file)

else:
    data = FromInput.askinp()

width = os.get_terminal_size().columns - 5

try:
    if data.get("status") == "0":
        output = data["program_output"].strip()
        console.print("\nYour code ran successfully with return code 0", style="green")

        console.print(Utils.print_msg_box(output, width=width))

    elif data.get("signal") == "Killed":
        output = data["program_output"][:20].strip()
        console.print("\nYour code ran successfully with status Killed", style="yellow")
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
