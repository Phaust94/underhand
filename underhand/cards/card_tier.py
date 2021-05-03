"""
Card tier
"""

import enum

__all__ = [
    "CardTier",
]


class CardTier(enum.Enum):
    Regular = enum.auto()
    Special = enum.auto()
    Blessing = enum.auto()
