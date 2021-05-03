"""
Models an event card
"""

from __future__ import annotations

import os.path
import typing
from dataclasses import dataclass, field

from underhand.cards.resource import Resource
from underhand.cards.foresight import ForesightOption
from underhand.cards.card_tier import CardTier

__all__ = [
    "EventCard",
    "CardOption",
    "ResourceList",
    "ResourceAmount",
]


ASSET_PATH = os.path.abspath(os.path.join(
    __file__,
    "..", "..",
    "assets",
))


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

    def resource_amount(self, resource_type: Resource) -> int:
        for res in self.resources:
            if res.resource_type is resource_type:
                return res.amount
        return 0



@dataclass
class CardOption:
    name: str = None
    resources_required: typing.Union[
        ResourceList,
        typing.Callable[[ResourceList], ResourceList],
    ] = field(default_factory=ResourceList)
    resources_received: ResourceList = field(default_factory=ResourceList)
    win_game: bool = False
    lose_game: bool = False

    shuffle_card_ids: typing.List[int] = field(default=None)
    foresight: ForesightOption = ForesightOption.NoForesight

    is_available: typing.Union[
        bool,
        typing.Callable[[ResourceList], bool],
    ] = True

    @property
    def picture_path(self) -> str:
        fn = f"OptionActive.png" if self.is_available else f"OptionDormant.png"
        path = os.path.join(ASSET_PATH, "options", fn)
        return path


DUMMY_OPTION = CardOption(is_available=False)


@dataclass
class EventCard:
    _id: int
    dupe_limit: int = 999
    tier: CardTier = CardTier.Regular
    options: typing.List[CardOption] = field(default_factory=list)
    unique_event: bool = False

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
        path = os.path.join(
                ASSET_PATH, "cards",
                f"Card{self._id}.png",
        )
        return path
