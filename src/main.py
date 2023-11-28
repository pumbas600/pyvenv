import sys

from pyvenv.cli import handle_command

def main():
    """Venv entrypoint for the CLI."""
    args = sys.argv[1:]
    handle_command(args)


if __name__ == '__main__':
    main()
