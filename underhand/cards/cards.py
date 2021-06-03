"""
Actual card instances
"""

from underhand.cards.card import CardOption, EventCard, ResourceList, ResourceAmount
from underhand.cards.card_tier import CardTier
from underhand.cards.foresight import Foresight
from underhand.cards.resource import Resource

__all__ = [
    "CARDS",
]

TRAVELLING_SALESPERSON = EventCard(
    1,
    1,
    CardTier.Regular,
    [
        CardOption(
            "Buy Supplies",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Money, 2),
            ),
            resources_received=ResourceList.from_resources(
                ResourceAmount(Resource.Food, 1),
            )
        ),
        CardOption(
            "Sell Supplies",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Food, 2),
            ),
            resources_received=ResourceList.from_resources(
                ResourceAmount(Resource.Money, 1),
            )
        ),
        CardOption("Decline to Trade"),
    ]
)

GODS_DEMAND_SACRIFICE = EventCard(
    4,
    1,
    CardTier.Regular,
    [
        CardOption(
            "Sacrifice Prisoners",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Prisoner, 2),
            )
        ),
        CardOption(
            "Sacrifice a Cultist",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Cultist, 1),
            )
        ),
        CardOption(
            "We don't have anyone to spare",
            shuffle_card_ids=[5]
        )
    ]
)

WRATH_OF_THE_GODS = EventCard(
    5,
    999,
    CardTier.Special,
    [
        CardOption(
            "Appease them with a large sacrifice",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Cultist, 5)
            )
        ),
        CardOption(
            "Appease them with a sacred offering",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Relic, 1)
            )
        ),
        CardOption(
            "The end has come",
            lose_game=True
        )
    ],
    unique_event=True
)

PERFORM_HARUSPICY = EventCard(
    21,
    1,
    CardTier.Blessing,
    [
        CardOption(
            "Make a sacrifice",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Food, 1),
            ),
            foresight=Foresight.Foresight,
        ),
        CardOption("We need the food"),
    ]
)

ORGAN_HARVEST = EventCard(
    23,
    1,
    CardTier.Blessing,
    [
        CardOption(
            "We need the cash",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Cultist | Resource.Prisoner, 1),
            ),
            resources_received=ResourceList.from_resources(
                ResourceAmount(Resource.Money, 2),
                ResourceAmount(Resource.Prisoner, 1)
            )
        ),
        CardOption(
            "We've got the meats",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Cultist | Resource.Prisoner, 1),
            ),
            resources_received=ResourceList.from_resources(
                ResourceAmount(Resource.Food, 2),
                ResourceAmount(Resource.Prisoner, 1)
            )
        ),
        CardOption("Save the slaughter for another day"),
    ]
)

CARDS = [
    TRAVELLING_SALESPERSON, PERFORM_HARUSPICY, ORGAN_HARVEST,
]
