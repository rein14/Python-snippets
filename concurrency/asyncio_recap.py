import asyncio
from random import randint
from time import perf_counter
from typing import Any, AsyncIterable, Awaitable

from req_http import http_get, http_get_sync

# The highest Pokemon id
MAX_POKEMON = 898


def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])


async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])

async def next_pokemons(total: int) -> AsyncIterable:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name

async def main() -> None:
    time_before = perf_counter()
    names = [name async for name in next_pokemons(20)]
    # async for name in next_pokemons(20):
    print(names)
    print(f"total time (asynchronous): {perf_counter() - time_before}.")
    # # synchronous call
    #  for _ in range(20):
    #     print(get_random_pokemon_name_sync())
    # asynchronous call
    # time_before = perf_counter()
    # pok = await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])
    # print(pok)
    # print(f"Total time (asynchronous): {perf_counter() - time_before}")

asyncio.run(main())