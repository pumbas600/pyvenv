import sys

from typing import Optional


def activate(venv_name: Optional[str]) -> None:
    pass


def current() -> None:
    print(sys.prefix)
    print(_is_venv_active())


def _is_venv_active() -> bool:
    """
    Return `True` if the current Python interpreter is running in a virtual environment,
    `False` otherwise.
    """
    return sys.prefix != sys.base_prefix
