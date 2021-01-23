from wandbox.commands.frominput import FromInput
from wandbox.commands.fromfile import FromFile

commands_dict = {
    "fromfile": FromFile.runfile,
    "frominput": FromInput.askinp,
}
