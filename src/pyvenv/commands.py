import os
import sys

from pathlib import Path
from venv import EnvBuilder
from colorama import Fore


def create_venv(venv_dir: str) -> None:
    """
    Create a new virtual environment at the given directory.
    
    :param venv_dir: The directory to create the virtual environment at
    """
    builder = EnvBuilder(with_pip=True)
    builder.create(venv_dir)


def activate_venv(venv_dir: str) -> None:
    """
    See: https://docs.python.org/3/library/os.html#os.name
    See: https://docs.python.org/3/library/venv.html#how-venvs-work
    """
    venv_path = Path(venv_dir)
    if not _is_venv_dir(venv_path):
        print(f'Could not find the virtual environment "{Fore.LIGHTCYAN_EX + venv_dir + Fore.RESET}"')
        return

    if os.name == 'posix':
        pass
    elif os.name == 'nt': # Windows
        os.system('echo Hi')
    else: # Java
        pass # Not supported


def display_current_venv() -> None:
    """
    Display the current active virtual environment. If there is no virtual
    environment active then this is indicated to the user.
    """
    if not _is_venv_active():
        print("No virtual environment is currently active.")
        return

    venv_name = _get_current_venv_name()
    print(f'Current virtual environment: {Fore.LIGHTGREEN_EX + venv_name + Fore.RESET}')


def _is_venv_dir(venv_path: Path) -> bool:
    """
    Return `True` if the given path is to a virtual environment directory,
    `False` otherwise. This is determined by checking that the directory exists,
    and it contains the `pyvenv.cfg` file.
    
    :param venv_path: The path to the virtual environment directory
    """
    return venv_path.exists() and venv_path.is_dir() and venv_path.joinpath('pyvenv.cfg').exists()


def _is_venv_active() -> bool:
    """
    Return `True` if the current Python interpreter is running in a virtual
    environment, `False` otherwise.

    See: https://docs.python.org/3/library/venv.html#how-venvs-work
    """
    return _get_current_venv_dir() != sys.base_prefix


def _get_current_venv_dir() -> str:
    """
    Return the directory of the current virtual environment. If there is no
    current virtual environment, this is the same as `sys.base_prefix`.
    """
    return sys.prefix


def _get_current_venv_name() -> str:
    """
    Return the name of the current virtual environment. This is defined as the
    name of the folder containing the virtual environment.
    """
    venv_path = Path(_get_current_venv_dir())
    return venv_path.parent.name
