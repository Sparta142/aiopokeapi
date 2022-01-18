from typing import TYPE_CHECKING

from aiopoke.minimal_resources import MinimalResource
from aiopoke.resource import Resource

if TYPE_CHECKING:
    from aiopoke.objects.utility import Language


class Description(Resource):
    description: str
    language: MinimalResource["Language"]

    def __init__(self, data) -> None:
        self.description = data["description"]
        self.language = MinimalResource(data["language"])
