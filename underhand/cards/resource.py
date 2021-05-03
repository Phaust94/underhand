"""
Models a resource
"""

import enum

__all__ = [
    "Resource",
]


class Resource(enum.Flag):
    Relic = enum.auto()
    Money = enum.auto()
    Cultist = enum.auto()
    Food = enum.auto()
    Prisoner = enum.auto()
    Suspicion = enum.auto()


starting_resources = [0, 2, 2, 2, 2, 0]

Player_Resources = {
    "Relic": f"{starting_resources[0]}",
    "Money": f"{starting_resources[1]}",
    "Cultist": f"{starting_resources[2]}",
    "Food": f"{starting_resources[3]}",
    "Prisoner": f"{starting_resources[4]}",
    "Suspicion": f"{starting_resources[5]}"
}
