from abc import ABC, abstractmethod


class Tekoaly(ABC):
    """Luokka, joka kuvaa tekoälyä."""

    @abstractmethod
    def pelaa(self) -> str:
        """Pelaa yhden kierroksen. Ei muuta luokan sisäistä tilaa.

        Returns:
            str: Tekoälyn pelaama siirto.
        """

    @abstractmethod
    def lisaa(self, syote: str) -> None:
        """Lisää pelaajan syötteen.

        Args:
            syote (str): Pelaajan syöte.
        """
