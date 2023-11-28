from typing import List
from pyvenv.commands import create


DEFAULT_VENV_NAME = ".venv"


def handle_command(args: List[str]) -> None:
    """Handle the command with the given CLI arguments."""
    arg_count = len(args)

    if arg_count == 0:
        # TODO: Print current venv
        return

    command = args[0].lower()
    if command == 'create':
        venv_name = args[1] if arg_count > 1 else DEFAULT_VENV_NAME
        create(venv_name)
