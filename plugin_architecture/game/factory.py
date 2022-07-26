"""factory for creating a game character"""
from typing import Any, Callable

from .character import GameCharacter

character_creation_funcs: dict[str, Callable[..., GameCharacter]] = {}

def register(character_type: str, creator_fn: Callable[..., GameCharacter]) -> None:
    """Register a character with the given character"""
    character_creation_funcs[character_type] = creator_fn

def unregister(character_type: str) -> None:
    """Unregister a character with the given character"""
    character_creation_funcs.pop(character_type, None)

def create(arguments: dict[str, Any]) -> GameCharacter:
    """Create a game character of a specific type, given JSON data"""
    args_copy = arguments.copy()
    character_type = args_copy.pop("type")
    try:
        creator_func = character_creation_funcs[character_type]
    except KeyError:
        raise ValueError(f"unknown character type{character_type!r}") from None
    return creator_func(**args_copy)
