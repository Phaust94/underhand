"""
Models a resource
"""

import enum

__all__ = [
    "Resource",
]


class Resource(enum.Flag):
    Suspicion = enum.auto()
    Relic = enum.auto()
    Food = enum.auto()
    Cultist = enum.auto()
    Prisoner = enum.auto()
    Money = enum.auto()
    Win = enum.auto()
    Lose = enum.auto()
