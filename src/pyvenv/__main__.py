import sys

from colorama import init
from pyvenv.cli import handle_command


def main():
    """PyVenv entrypoint for the CLI."""
    init()

    args = sys.argv[1:]
    handle_command(args)


if __name__ == '__main__':
    main()
