import json
import os
import random
import sys

import requests
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles.pygments import style_from_pygments_cls as sfpc
from pygments.styles import get_style_by_name
from rich.console import Console
from rich.syntax import Syntax

from utilities.lang_lexers import init_lexers, lexers_dict, spinners
from utilities.utils import Utils


class FromInput:
    def __init__(self):
        init_lexers()

        with open("utilities/compilers.json") as compilers:
            self.compilers = json.load(compilers)

        self.console = Console()
        self.output_json = dict()
        self.spinners = spinners

    def get_lang(self):
        """Prompt the user for the programming language, close program if language not supported."""
        language = self.console.input("[green]Enter language:[/green] ").lower()

        if language not in self.compilers:
            self.console.print("Language is not supported!", style="bold red")
            Utils.close()
        return language

    def askinp(self):
        """
        Make a multiline prompt for code input and send the code to the api.

        The compiled output from the api is returned.
        """
        language = self.get_lang()
        self.console.print("Enter your code, (press esc + enter to run)", style="green")
        style = sfpc(get_style_by_name("monokai"))

        code = prompt(
            "",
            lexer=PygmentsLexer(lexers_dict[language]),
            include_default_pygments_style=False,
            style=style,
            multiline=True,
        )

        self.output_json["code"] = code
        self.output_json["compiler"] = self.compilers[language]

        with self.console.status(
            "Compiling", spinner=random.choice(self.spinners)
        ) as status:
            headers = {"Content-type": "application/json"}
            data = requests.post(
                "https://wandbox.org/api/compile.json",
                headers=headers,
                data=json.dumps(self.output_json),
            ).json()
        return data


FromInput = FromInput()