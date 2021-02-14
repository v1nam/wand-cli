import json
import random
import tempfile

import requests
from subprocess import call

from rich.console import Console
from wandbox.utilities.compilers import compilers_
from wandbox.utilities.constants import spinners
from wandbox.utilities.lang_extensions import lang_names
from wandbox.utilities.utils import Utils

class FromBuffer:
    def __init__(self):
        self.compilers = compilers_
        self.console = Console()
        self.spinners = spinners
        self.output_json = {}
    
    def create_buffer(self, language, editor):
        """Validate language entered and create a buffer for the code editor given."""
        if language not in lang_names:
            self.console.print("Language is not supported!", style="bold red")
            Utils.close()

        with tempfile.NamedTemporaryFile(suffix="."+lang_names[language]) as tf:
            tf.write(b"")
            tf.flush()
            call([editor, tf.name])

            tf.seek(0)
            code = tf.read().decode("utf-8")

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
        

FromBuffer = FromBuffer()
