import sys, os


class Utils:
    def close(self):
        """Exit the program."""
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)

    def print_msg_box(self, msg, indent=1, width=None, title=None):
        """Print message-box with optional title."""
        lines = msg.split("\n")
        true_lines = []

        for line in lines:
            if len(line) > width:
                for trimmed in range((len(line)//width)+1):
                    true_lines.append(line[width*trimmed:width+(trimmed*width)])
            else:
                true_lines.append(line)

        lines = [i for i in true_lines if i]
        space = " " * indent
        if not width:
            width = max(map(len, lines))
        box = f'┏{"━" * (width + indent * 2)}┓\n'
        if title:
            box += f"┃{space}{title:<{width}}{space}┃\n"
            box += f'┃{space}{"-" * len(title):<{width}}{space}┃\n'
        box += "".join([f"┃{space}{line:<{width}}{space}┃\n" for line in lines])
        box += f'┗{"━" * (width + indent * 2)}┛'
        return box


Utils = Utils()
