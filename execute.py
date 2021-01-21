import json
import sys
import os
import requests
import random
from rich.console import Console
from rich.syntax import Syntax
from rich.markdown import Markdown
import pygments
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles.pygments import style_from_pygments_cls as sfpc
from pygments.styles import get_style_by_name
from lang_lexers import init_lexers, lexers_dict

init_lexers()

lines = []
output_json = dict()


def close():
    try:
        sys.exit(1)
    except SystemExit:
        os._exit(1)


with open("compilers.json") as compilers:
    compilers = json.load(compilers)

console = Console()
language = console.input("[green]Enter language:[/green] ").lower()

if language not in compilers:
    console.print("Language is not supported!", style="bold red")
    close()

spinners = [
    "point",
    "dots",
    "dots12",
    "dots9",
    "dots2",
    "simpleDotsScrolling",
    "bouncingBall",
]

console.print("Enter your code, (press esc + enter to run)", style="green")
style = sfpc(get_style_by_name("monokai"))

code = prompt(
    "",
    lexer=PygmentsLexer(lexers_dict[language]),
    include_default_pygments_style=False,
    style=style,
    multiline=True,
)

output_json["code"] = code
output_json["compiler"] = compilers[language]

with console.status("Producing output", spinner=random.choice(spinners)) as status:
    headers = {"Content-type": "application/json"}
    data = requests.post(
        "https://wandbox.org/api/compile.json",
        headers=headers,
        data=json.dumps(output_json),
    ).json()

if data.get("status") == "0":
    output = data["program_output"]
    console.print("Your code ran successfully with return code 0", style="green")
    md = Markdown(f"```\n{output}")
    console.print(md)

elif data.get("signal") == "Killed":
    output = data["program_output"][:20]
    md = Markdown(f"```\n{output}")
    console.print(md)
    console.print("Truncated, output is too long", style="yellow")

else:
    for k in tuple(data.keys()):
        if "error" in k:
            output = data[k]
            break
    console.print("Your code errored out with return code 1", style="red")
    md = Markdown(f"```\n{output}")
    console.print(md)
