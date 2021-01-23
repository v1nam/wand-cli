from wandbox.commands.frominput import FromInput
from wandbox.commands.fromfile import FromFile
from wandbox.commands.base import Base

commands_dict = {
    "fromfile": FromFile.runfile,
    "frominput": FromInput.askinp,
    "base": Base.run,
}
