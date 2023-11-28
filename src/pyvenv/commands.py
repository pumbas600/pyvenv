import os
import sys

from venv import EnvBuilder
from typing import Optional


def create_venv(venv_dir: str) -> None:
    """
    Create a new virtual environment at the given directory.
    
    venv_dir - The directory to create the virtual environment at.
    """
    builder = EnvBuilder()
    builder.create(venv_dir)


def activate(venv_name: Optional[str]) -> None:
    pass


def display_current_venv() -> None:
    """
    Display the current active virtual environment. If there is no virtual environment
    active then this is indicated to the user.
    """
    if not _is_venv_active():
        print("No virtual environment is currently active.")
        return

    # Include the separator at the end of the current working directory so that it gets
    # removed by `str.removeprefix()`.
    cwd = os.getcwd() + os.sep
    venv_dir = sys.prefix

    if venv_dir.startswith(cwd):
        venv_dir = venv_dir.removeprefix(cwd)

    print(f'Current virtual environment: {venv_dir}')


def _is_venv_active() -> bool:
    """
    Return `True` if the current Python interpreter is running in a virtual environment,
    `False` otherwise.

    See: https://docs.python.org/3/library/venv.html#how-venvs-work.
    """
    return sys.prefix != sys.base_prefix
