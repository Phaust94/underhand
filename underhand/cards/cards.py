"""
Actual card instances
"""

from underhand.cards.card import CardOption, EventCard, ResourceList, ResourceAmount
from underhand.cards.resource import Resource

__all__ = [
    "CARDS",
]

TRAVELLING_SALESPERSON = EventCard(
    1,
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

PERFORM_HARUSPICY = EventCard(
    21,
    [
        CardOption(
            "Make a sacrifice",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Food, 1),
            ),
            foresight=True,
        ),
        CardOption("We need the food"),
    ]
)

ORGAN_HARVEST = EventCard(
    23,
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
            "We've got the meals",
            resources_required=ResourceList.from_resources(
                ResourceAmount(Resource.Cultist | Resource.Prisoner, 1),
            ),
            resources_received=ResourceList.from_resources(
                ResourceAmount(Resource.Food, 2),
                ResourceAmount(Resource.Prisoner, 1)
            )
        ),
        CardOption("Save the salughter for another day"),
    ]
)

CARDS = [
    TRAVELLING_SALESPERSON, PERFORM_HARUSPICY, ORGAN_HARVEST,
]

