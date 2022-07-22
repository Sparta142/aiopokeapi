__title__ = "aiopoke"
__author__ = "beastmatser"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present beastmatser"
__version__ = "0.1.4"

from typing import NamedTuple

from aiopoke.aiopoke_client import AiopokeClient
from aiopoke.objects import (
    Ability,
    Berry,
    BerryFirmness,
    BerryFlavor,
    Characteristic,
    ContestEffect,
    ContestType,
    Description,
    Effect,
    EggGroup,
    Encounter,
    EncounterCondition,
    EncounterConditionValue,
    EncounterMethod,
    EvolutionChain,
    EvolutionTrigger,
    FlavorText,
    Gender,
    Generation,
    GenerationGameIndex,
    GrowthRate,
    Item,
    ItemAttribute,
    ItemCategory,
    ItemFlingEffect,
    ItemPocket,
    Language,
    Location,
    LocationArea,
    Machine,
    MachineVersionDetail,
    Move,
    MoveAilment,
    MoveBatteStyle,
    MoveCategory,
    MoveDamageClass,
    MoveLearnMethod,
    MoveTarget,
    Name,
    NamedResource,
    NaturalGiftType,
    Nature,
    PalParkArea,
    PokeathlonStat,
    Pokedex,
    Pokemon,
    PokemonColor,
    PokemonForm,
    PokemonHabitat,
    PokemonShape,
    PokemonSpecies,
    Region,
    Sprite,
    Sprites,
    Stat,
    SuperContestEffect,
    VerboseEffect,
    Version,
    VersionEncounterDetail,
    VersionGameIndex,
    VersionGroup,
    VersionGroupFlavorText,
)


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str  # must be one of the following: alpha, beta, candidate, or final

    def __repr__(self) -> str:
        return f"{self.major}.{self.minor}.{self.micro}-{self.releaselevel}"


version_info: VersionInfo = VersionInfo(0, 1, 3, "final")


__all__ = (
    "Language",
    "Description",
    "Effect",
    "Encounter",
    "FlavorText",
    "GenerationGameIndex",
    "MachineVersionDetail",
    "Name",
    "NamedResource",
    "Sprite",
    "Sprites",
    "VerboseEffect",
    "VersionEncounterDetail",
    "VersionGameIndex",
    "VersionGroupFlavorText",
    "Berry",
    "BerryFirmness",
    "BerryFlavor",
    "ContestEffect",
    "ContestType",
    "SuperContestEffect",
    "EncounterCondition",
    "EncounterConditionValue",
    "EncounterMethod",
    "EvolutionChain",
    "EvolutionTrigger",
    "Generation",
    "Pokedex",
    "VersionGroup",
    "Version",
    "ItemAttribute",
    "ItemCategory",
    "ItemFlingEffect",
    "ItemPocket",
    "Item",
    "LocationArea",
    "Location",
    "PalParkArea",
    "Region",
    "Machine",
    "MoveAilment",
    "MoveBatteStyle",
    "MoveCategory",
    "MoveDamageClass",
    "MoveLearnMethod",
    "MoveTarget",
    "Move",
    "Ability",
    "Characteristic",
    "EggGroup",
    "Gender",
    "GrowthRate",
    "NaturalGiftType",
    "Nature",
    "PokeathlonStat",
    "PokemonColor",
    "PokemonForm",
    "PokemonHabitat",
    "PokemonShape",
    "PokemonSpecies",
    "Pokemon",
    "Stat",
    "AiopokeClient",
    "version_info",
    "__title__",
    "__author__",
    "__license__",
    "__copyright__",
    "__version__",
)
