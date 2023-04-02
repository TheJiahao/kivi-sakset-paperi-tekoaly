from abc import ABC, abstractmethod


class Tekoaly(ABC):
    @abstractmethod
    def pelaa(self) -> str:
        """Pelaa yhden kierroksen.

        Returns:
            str: Tekoälyn pelaama siirto.
        """

    @abstractmethod
    def lisaa(self, syote: str) -> str:
        """Lisää pelaajan syötteen.

        Args:
            syote (str): Pelaajan syöte.
        """
