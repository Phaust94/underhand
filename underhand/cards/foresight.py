"""
Foresight options
"""

import enum

__all__ = [
    "Foresight",
]


class Foresight(enum.Enum):
    NoForesight = enum.auto()
    Foresight = enum.auto()
    ForesightWithDiscard = enum.auto()
