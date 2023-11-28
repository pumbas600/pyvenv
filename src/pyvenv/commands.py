import sys

from venv import EnvBuilder
from typing import Optional


def create(venv_name: str) -> None:
    builder = EnvBuilder()
    builder.create(venv_name)


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
