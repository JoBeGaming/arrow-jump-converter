# Tools for the converter.

# (c) JoBe, 2025


from .config import (
    ARROW,
    DASH,
    PIPE
)


__all__ = [
    "cleanup"
]


def cleanup(line: str) -> str:
    return line.replace(PIPE, "").replace(ARROW, "").replace(DASH, "").rstrip()
