
from typing import Protocol

class GameCharacter(Protocol):

    """Basic representation of a character"""
    def make_a_noise(self) -> None:   
        """let the charater make a noise"""
     
