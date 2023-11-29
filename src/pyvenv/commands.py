import sys

from pathlib import Path
from venv import EnvBuilder
from typing import Optional
from colorama import Fore


def create_venv(venv_dir: str) -> None:
    """
    Create a new virtual environment at the given directory.
    
    venv_dir -- The directory to create the virtual environment at
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

    venv_name = _get_current_venv_name()
    print(f'Current virtual environment: {Fore.LIGHTGREEN_EX + venv_name}')


def _is_venv_active() -> bool:
    """
    Return `True` if the current Python interpreter is running in a virtual environment,
    `False` otherwise.

    See: https://docs.python.org/3/library/venv.html#how-venvs-work.
    """
    return _get_current_venv_dir() != sys.base_prefix


def _get_current_venv_dir() -> str:
    """
    Return the directory of the current virtual environment. If there is no current virtual
    environment, this is the same as `sys.base_prefix`.
    """
    return sys.prefix


def _get_current_venv_name() -> str:
    """
    Return the name of the current virtual environment. This is defined as the name of
    the folder containing the virtual environment.
    """
    venv_path = Path(_get_current_venv_dir())
    return venv_path.parent.name
