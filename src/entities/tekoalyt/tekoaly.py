from abc import ABC, abstractmethod
from typing import Hashable


class Tekoaly(ABC, Hashable):
    @abstractmethod
    def pelaa(self) -> str:
        """Pelaa yhden kierroksen. Ei muuta luokan sisäistä tilaa.

        Returns:
            str: Tekoälyn pelaama siirto.
        """

    @abstractmethod
    def lisaa(self, syote: str) -> str:
        """Lisää pelaajan syötteen.

        Args:
            syote (str): Pelaajan syöte.
        """
