"""
Foresight options
"""

import enum

__all__ = [
    "ForesightOption",
]


class ForesightOption(enum.Enum):
    NoForesight = enum.auto()
    Foresight = enum.auto()
    ForesightWithDiscard = enum.auto()
