import json
import random
import requests

from rich.console import Console

from wandbox.utilities.constants import spinners
from wandbox.utilities.utils import Utils
from wandbox.utilities.lang_extensions import lang_extensions_


class FromFile:
    def __init__(self):
        self.console = Console()
        self.output_json = dict()
        self.spinners = spinners

        self.extensions = lang_extensions_

    def runfile(self, file):
        """Send code form file to the api and return the response."""
        try:
            code = open(file)
            code = code.read()

            if not any(file.endswith("." + ext) for ext in self.extensions):
                self.console.print(
                    "File Extension language is not supported!", style="bold red"
                )
                Utils.close()

            self.output_json["code"] = code
            self.output_json["compiler"] = self.extensions[file[file.rfind(".") + 1 :]]

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
        except FileNotFoundError:
            self.console.print("Path is invalid; File not found", style="bold red")
            Utils.close()


FromFile = FromFile()
