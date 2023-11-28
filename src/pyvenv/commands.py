import sys

from venv import EnvBuilder
from typing import Optional


def create(venv_dir: str) -> None:
    """Create a new virtual environment at the given directory."""
    builder = EnvBuilder()
    builder.create(venv_dir)


def activate(venv_name: Optional[str]) -> None:
    pass


def current() -> None:
    print(sys.prefix)
    print(_is_venv_active())


def _is_venv_active() -> bool:
    """
    Return `True` if the current Python interpreter is running in a virtual environment,
    `False` otherwise.

    See: https://docs.python.org/3/library/venv.html#how-venvs-work.
    """
    return sys.prefix != sys.base_prefix
