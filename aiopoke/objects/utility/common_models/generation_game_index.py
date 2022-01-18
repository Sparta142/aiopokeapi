from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.resources import Generation


class GenerationGameIndex(Resource):
    game_index: int
    generation: MinimalResource["Generation"]

    def __init__(self, data) -> None:
        self.game_index = data["game_index"]
        self.generation = MinimalResource(data["generation"])
