from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.objects.utility import Name
from aiopoke.objects.utility import NamedResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources.berries import Berry


class BerryFlavor(NamedResource):
    berries: Tuple["FlavorBerryMap", ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berries = tuple(
            FlavorBerryMap(berry_data) for berry_data in data["berries"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])


class FlavorBerryMap(Resource):
    potency: int
    berry: MinimalResource["Berry"]

    def __init__(self, data) -> None:
        self.potency = data["potency"]
        self.berry = MinimalResource(data["berry"])
