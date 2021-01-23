import os
from wandbox.colorschemes.nord import NordStyle
from wandbox.colorschemes.gruvbox import GruvboxStyle
from wandbox.colorschemes.dracula import DraculaStyle


scheme_dict = {
    "nord": NordStyle.get_nord,
    "gruvbox": GruvboxStyle.get_gruvbox,
    "dracula": DraculaStyle.get_dracula,
}

schemes = list(scheme_dict.keys())