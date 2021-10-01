import pytest
import aiopoke


@pytest.mark.asyncio
async def test_cache(client: aiopoke.AiopokeClient):
    pokemon = await client.fetch_pokemon(5)
    encounter_condition = await client.fetch_encounter_condition(2)

    cache = client._cache._cache
    assert cache["pokemon_5"] == pokemon
    assert cache["encounter_condition_2"] == encounter_condition

    move = await client.fetch_move(1)
    contest_effect = await move.contest_effect.fetch()

    assert isinstance(contest_effect, aiopoke.ContestEffect)
