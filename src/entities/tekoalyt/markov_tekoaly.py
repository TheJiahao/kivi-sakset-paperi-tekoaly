from entities.markovin_ketju import MarkovinKetju
from entities.tekoalyt.tekoaly import Tekoaly


class MarkovTekoaly(Tekoaly):
    """Luokka, joka kuvaa Markovin ketjuun perustuva tekoälyä."""

    def __init__(self, n: int, voittavat_siirrot: dict[str, str]) -> None:
        """Luokan konstruktori.

        Args:
            n (int): Markovin ketjun pituus.
            voittavat_siirrot (dict[str, str]): Syötteitä vastaavat voittavat siirrot.
        """

        self.__markovin_ketju: MarkovinKetju = MarkovinKetju(
            n, set(voittavat_siirrot.keys())
        )
        self.voittavat_siirrot: dict[str, str] = voittavat_siirrot

    def pelaa(self) -> str:
        """Pelaa yhden kierroksen. Ei muuta luokan sisäistä tilaa.

        Returns:
            str: Tekoälyn pelaama siirto.
        """

        ennuste = str(self.__markovin_ketju.ennusta())
        return self.voittavat_siirrot[ennuste]

    def lisaa(self, syote: str) -> None:
        """Lisää pelaajan syötteen.

        Args:
            syote (str): Pelaajan syöte.
        """

        self.__markovin_ketju.lisaa(syote)
