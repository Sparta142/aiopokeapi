from typing import TYPE_CHECKING, List, Optional

from aiopoke.objects.utility.common_models import Name, NamedResource
from aiopoke.utils.minimal_resources import MinimalResource
from aiopoke.utils.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import BerryFlavor, MoveBatteStyle
    from aiopoke.objects.resources.pokemon import PokeathlonStat


class Nature(NamedResource):
    decreased_stat: Optional[MinimalResource["PokeathlonStat"]]
    hates_flavor: Optional[MinimalResource["BerryFlavor"]]
    increased_stat: Optional[MinimalResource["PokeathlonStat"]]
    likes_flavor: Optional[MinimalResource["BerryFlavor"]]
    move_battle_style_preferences: List["MoveBattleStylePreference"]
    names: List["Name"]
    pokeathlon_stat_changes: List["NatureStatChange"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.decreased_stat = (
            MinimalResource(data["decreased_stat"])
            if data["decreased_stat"] is not None
            else None
        )
        self.hates_flavor = (
            MinimalResource(data["hates_flavor"])
            if data["hates_flavor"] is not None
            else None
        )
        self.increased_stat = (
            MinimalResource(data["increased_stat"])
            if data["increased_stat"] is not None
            else None
        )
        self.likes_flavor = (
            MinimalResource(data["likes_flavor"])
            if data["likes_flavor"] is not None
            else None
        )
        self.move_battle_style_preferences = [
            MoveBattleStylePreference(move_battle_style_preference_data)
            for move_battle_style_preference_data in data[
                "move_battle_style_preferences"
            ]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.pokeathlon_stat_changes = [
            NatureStatChange(pokeathlon_stat_change_data)
            for pokeathlon_stat_change_data in data["pokeathlon_stat_changes"]
        ]


class NatureStatChange(Resource):
    max_change: int
    pokeathlon_stat: MinimalResource["PokeathlonStat"]

    def __init__(self, data) -> None:
        self.max_change = data["max_change"]
        self.pokeathlon_stat = MinimalResource(data["pokeathlon_stat"])


class MoveBattleStylePreference(Resource):
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: MinimalResource["MoveBatteStyle"]

    def __init__(self, data) -> None:
        self.low_hp_preference = data["low_hp_preference"]
        self.high_hp_preference = data["high_hp_preference"]
        self.move_battle_style = MinimalResource(data["move_battle_style"])
