import os
import sys

if not __package__:
    sys.path[0] = sys.path[0][: sys.path[0].rfind("/")]

import wandbox


if __name__ == "__main__":
    try:
        sys.exit(wandbox.main())
    except Exception as e:
        print(f"Error: \n{e}")
