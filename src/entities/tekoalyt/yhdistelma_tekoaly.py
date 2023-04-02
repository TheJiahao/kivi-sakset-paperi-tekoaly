from collections import deque
from copy import deepcopy

from entities.peli import Peli
from entities.tekoalyt.markov_tekoaly import MarkovTekoaly
from entities.tekoalyt.tekoaly import Tekoaly


class YhdistelmaTekoaly(Tekoaly):
    """Luokka, joka kuvaa usean tekoälyn yhdistelmätekoälyä."""

    def __init__(self, fokus_pituus: int, peli: Peli | None = None) -> None:
        """Luokan konstruktori.

        Args:
            fokus_pituus (int):
                Kuvaa monenko viimeisimmän kierroksen tuloksen perusteella tekoälyt pisteytetään.
            peli (Peli | None, optional):
                Pelin tuloksista vastaava olio. Oletukseltaan None.

        Raises:
            ValueError: Ei-positiivinen fokus_pituus.
        """
        if fokus_pituus <= 0:
            raise ValueError("Ei-positiivinen fokus_pituus ei kelpaa.")

        self.__fokus_pituus: int = fokus_pituus
        self.__peli: Peli = peli or Peli()
        self.__pisteet: dict[Tekoaly, deque[int]] = {}

        self.__alusta_pisteet()

        self.__pelaava_tekoaly: Tekoaly = self.hae_paras_tekoaly()
        self.__siirtoja_jaljella: int = fokus_pituus

    def __hash__(self) -> int:
        return (
            (sum(hash(tekoaly) for tekoaly in self.hae_tekoalyt()))
            + self.__fokus_pituus
            + hash(self.__peli)
        )

    def __alusta_pisteet(self) -> None:
        for i in range(1, self.__fokus_pituus + 1):
            tekoaly = MarkovTekoaly(i, self.__peli.voittavat_siirrot)
            self.__pisteet[tekoaly] = deque(maxlen=self.__fokus_pituus)

    @property
    def pelaava_tekoaly(self) -> Tekoaly:
        return deepcopy(self.__pelaava_tekoaly)

    @property
    def siirtoja_jaljella(self) -> int:
        return self.__siirtoja_jaljella

    @property
    def pisteet(self) -> dict[Tekoaly, deque[int]]:
        return deepcopy(self.__pisteet)

    def __paivita_pisteet(self, syote: str) -> None:
        """Päivittää tekoälyjen pisteet.

        Args:
            syote (str): Pelaajan syöte viime kierroksella.
        """

        for tekoaly in self.hae_tekoalyt():
            tulos = self.__peli.paata_voittaja(tekoaly.pelaa(), syote)
            self.__pisteet[tekoaly].append(tulos)

    def hae_tekoalyt(self) -> list[Tekoaly]:
        """Palauttaa kaikki tekoälyt.

        Returns:
            list[Tekoaly]: Lista, joka sisältää kaikki tekoälyt.
        """

        return deepcopy(list(self.pisteet.keys()))

    def hae_paras_tekoaly(self) -> Tekoaly:
        """Palauttaa parhaiten pelanneen tekoälyn.

        Returns:
            Tekoaly: Tekoäly, jolla on korkein pistemäärä.
        """

        return max(self.hae_tekoalyt(), key=self.hae_pisteet)

    def hae_pisteet(self, tekoaly: Tekoaly) -> int:
        """Hakee annetun tekoälyn pistemäärän.

        Args:
            tekoaly (Tekoaly): Haettava tekoäly.

        Raises:
            ValueError: Tekoäly ei kuulu joukkoon.

        Returns:
            int: Tekoälyn pistemäärä.
        """

        if tekoaly not in self.hae_tekoalyt():
            raise ValueError("Tekoäly ei kuulu joukkoon.")

        return sum(self.__pisteet[tekoaly])

    def pelaa(self) -> str:
        """Pelaa kierroksen. Ei muuta luokan sisäistä tilaa.

        Returns:
            str: Tällä hetkellä pelaavan tekoälyn pelaama siirto.
        """

        return self.__pelaava_tekoaly.pelaa()

    def lisaa(self, syote: str) -> None:
        """Lisää pelaajan syötteen ja päivittää tekoälyjen pisteytystä.

        Args:
            syote (str): Pelaajan syöte.
        """

        if self.__siirtoja_jaljella == 0:
            self.__pelaava_tekoaly = self.hae_paras_tekoaly()
            self.__siirtoja_jaljella = self.__fokus_pituus

        self.__siirtoja_jaljella -= 1

        self.__paivita_pisteet(syote)

        for tekoaly in self.hae_tekoalyt():
            tekoaly.lisaa(syote)
