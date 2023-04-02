from collections import deque
from copy import deepcopy

from entities.peli import Peli
from entities.tekoalyt.markov_tekoaly import MarkovTekoaly
from entities.tekoalyt.tekoaly import Tekoaly


class YhdistelmaTekoaly(Tekoaly):
    def __init__(self, fokus_pituus: int, peli: Peli) -> None:
        self.__fokus_pituus: int = fokus_pituus
        self.__tekoalyt: list[Tekoaly] = []
        self.__peli: Peli = peli

        self.__alusta_tekoalyt()

        self.__pisteet: dict[Tekoaly, deque[int]] = {
            tekoaly: deque(maxlen=fokus_pituus) for tekoaly in self.__tekoalyt
        }

        self.__pelaava_tekoaly = self.__tekoalyt[0]
        self.__siirtoja_jaljella = fokus_pituus

    @property
    def pelaava_tekoaly(self) -> Tekoaly:
        return deepcopy(self.__pelaava_tekoaly)

    @property
    def siirtoja_jaljella(self) -> int:
        return self.__siirtoja_jaljella

    @property
    def pisteet(self) -> dict[Tekoaly, deque[int]]:
        return deepcopy(self.__pisteet)

    def __alusta_tekoalyt(self) -> None:
        for i in range(1, self.__fokus_pituus + 1):
            self.__tekoalyt.append(MarkovTekoaly(i, self.__peli.voittavat_siirrot))

    def __vaihda_tekoaly(self) -> None:
        self.__pelaava_tekoaly = max(self.__tekoalyt, key=self.hae_pisteet)

        self.__siirtoja_jaljella = self.__fokus_pituus

    def __lisaa_pelitulos(self, syote: str) -> None:
        for tekoaly in self.__tekoalyt:
            tulos = self.__peli.paata_voittaja(tekoaly.pelaa(), syote)
            self.__pisteet[tekoaly].append(tulos)

    def hae_pisteet(self, tekoaly: Tekoaly) -> int:
        """Hakee annetun tekoälyn pistemäärän.

        Args:
            tekoaly (Tekoaly): Haettava tekoäly.

        Raises:
            ValueError: Tekoäly ei kuulu joukkoon.

        Returns:
            int: Tekoälyn pistemäärä.
        """
        if tekoaly not in self.__tekoalyt:
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

        self.__siirtoja_jaljella -= 1

        if self.__siirtoja_jaljella == 0:
            self.__vaihda_tekoaly()

        self.__lisaa_pelitulos(syote)

        for tekoaly in self.__tekoalyt:
            tekoaly.lisaa(syote)
