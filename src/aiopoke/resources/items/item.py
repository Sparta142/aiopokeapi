from typing import List, Optional
from ...minimal_resources import (
    EvolutionChainUrl,
    MinimalItemAttribute,
    MinimalItemCategory,
    MinimalItemFlingEffect,
    MinimalPokemon,
    MinimalVersion,
)
from ...utility import Sprite
from ...utility import (
    Name,
    MachineVersionDetail,
    GenerationGameIndex,
    NamedResource,
    VerboseEffect,
    FlavorText,
)


class Item(NamedResource):
    attributes: List["MinimalItemAttribute"]
    baby_trigger_form: Optional["EvolutionChainUrl"]
    cost: int
    effect_entry: "VerboseEffect"
    effect_entries: List["VerboseEffect"]
    flavor_text_entry: "FlavorText"
    flavor_text_entries: List["FlavorText"]
    fling_effect: Optional["MinimalItemFlingEffect"]
    fling_power: Optional[int]
    game_indices: List["GenerationGameIndex"]
    held_by_pokemon: List["ItemHolderPokemon"]
    machines: List["MachineVersionDetail"]
    names: List["Name"]
    sprite: Optional["Sprite"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.attributes = [
            MinimalItemAttribute(attribute_data)
            for attribute_data in data["attributes"]
        ]
        self.baby_trigger_for = (
            EvolutionChainUrl(data["baby_trigger_for"]["url"])
            if data["baby_trigger_for"] is not None
            else None
        )
        self.category = MinimalItemCategory(data["category"])
        self.cost = data["cost"]
        self.effect_entry = [
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
            if effect_entry_data["language"]["name"] == "en"
        ][0]
        self.effect_entries = [
            VerboseEffect(effect_entry_data)
            for effect_entry_data in data["effect_entries"]
        ]
        self.flavor_text_entry = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
            if flavor_text_entry_data["language"]["name"] == "en"
        ][0]
        self.flavor_text_entries = [
            FlavorText(flavor_text_entry_data)
            for flavor_text_entry_data in data["flavor_text_entries"]
        ]
        self.fling_effect = (
            MinimalItemFlingEffect(data["fling_effect"])
            if data["fling_effect"] is not None
            else None
        )
        self.fling_power = data["fling_power"]
        self.game_indices = [
            GenerationGameIndex(game_indice_data)
            for game_indice_data in data["game_indices"]
        ]
        self.held_by_pokemon = [
            ItemHolderPokemon(pokemon_data) for pokemon_data in data["held_by_pokemon"]
        ]
        self.machines = [
            MachineVersionDetail(machine_data) for machine_data in data["machines"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]
        self.sprite = Sprite(data["sprites"]["default"])

    def __repr__(self) -> str:
        return (
            f"<Item attributes={self.attributes} baby_trigger_form={self.baby_trigger_form} cost={self.cost} effect_entry={self.effect_entry} "
            f"effect_entries={self.effect_entries} flavor_text_entry={self.flavor_text_entry} flavor_text_entries={self.flavor_text_entries} "
            f"fling_effect={self.fling_effect} fling_power={self.fling_power} game_indices={self.game_indices} held_by_pokemon={self.held_by_pokemon} "
            f"id_={self.id_} machines={self.machines} name='{self.name}' names={self.name} sprite={self.sprite}>"
        )


class ItemSprites:
    default: Optional["Sprite"]

    def __init__(self, data) -> None:
        self.default = Sprite.from_url(data["default"])

    def __repr__(self) -> str:
        return f"<ItemSprites default={self.default}>"


class ItemHolderPokemon:
    pokemon: "MinimalPokemon"
    version_details: List["ItemHolderPokemonVersionDetail"]

    def __init__(self, data) -> None:
        self.pokemon = MinimalPokemon(data["pokemon"])
        self.version_details = [
            ItemHolderPokemonVersionDetail(version_detail_data)
            for version_detail_data in data["version_details"]
        ]

    def __repr__(self) -> str:
        return f"<ItemHolderPokemon pokemon={self.pokemon} version_details={self.version_details}>"


class ItemHolderPokemonVersionDetail:
    def __init__(self, data) -> None:
        self.rarity = data["rarity"]
        self.version = MinimalVersion(data["version"])

    def __repr__(self) -> str:
        return f"<ItemHolderPokemonVersionDetail rarity={self.rarity} version={self.version}>"
