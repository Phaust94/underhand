"""
Models an event card
"""

from __future__ import annotations

import os.path
import typing
from dataclasses import dataclass, field

from underhand.cards.resource import Resource

__all__ = [
    "EventCard",
    "CardOption",
    "ResourceList",
    "ResourceAmount",
]


@dataclass
class ResourceAmount:
    resource_type: Resource
    amount: int


@dataclass
class ResourceList:
    resources: typing.List[ResourceAmount] = field(default_factory=list)

    def __post_init__(self):
        res_types = [x.resource_type for x in self.resources]
        assert len(set(res_types)) == len(res_types), "Duplicate resource types"

    @classmethod
    def from_resources(cls, *resources: ResourceAmount) -> ResourceList:
        return cls(list(resources))


@dataclass
class CardOption:
    name: str = None
    resources_required: typing.Union[
        ResourceList,
        typing.Callable[[ResourceList], ResourceList],
    ] = field(default_factory=ResourceList)
    resources_received: ResourceList = field(default_factory=ResourceList)

    shuffle_card_ids: typing.List[int] = field(default=None)
    foresight: bool = False

    is_available: typing.Union[
        bool,
        typing.Callable[[ResourceList], bool],
    ] = True


DUMMY_OPTION = CardOption(is_available=False)


@dataclass
class EventCard:
    _id: int
    options: typing.List[CardOption] = field(default_factory=list)
    dupe_limit: int = 999

    def __post_init__(self):
        if len(self.options) > 3:
            raise ValueError("Too many options")
        self.options = self.options + [DUMMY_OPTION for _ in range(3 - len(self.options))]

        for option in self.options:
            if option.shuffle_card_ids is None:
                option.shuffle_card_ids = [self._id]

        return None

    @property
    def picture_path(self) -> str:
        path = os.path.abspath(
            os.path.join(
                __file__,
                "..", "..",
                "assets", "cards",
                f"Card{self._id}.png",
            )
        )
        return path
