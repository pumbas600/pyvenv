from typing import List
from pyvenv.commands import create, current


DEFAULT_VENV_DIR = ".venv"


def handle_command(args: List[str]) -> None:
    """Handle the command with the given CLI arguments."""
    arg_count = len(args)

    if arg_count == 0:
        current()
        return

    command = args[0].lower()
    if command == 'create':
        venv_dir = args[1] if arg_count > 1 else DEFAULT_VENV_DIR
        create(venv_dir)
