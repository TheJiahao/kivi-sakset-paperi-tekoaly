from collections import deque
from copy import deepcopy

from entities.peli import Peli
from entities.tekoalyt.markov_tekoaly import MarkovTekoaly
from entities.tekoalyt.tekoaly import Tekoaly


class YhdistelmaTekoaly(Tekoaly):
    """Luokka, joka kuvaa usean tekoälyn yhdistelmätekoälyä."""

    def __init__(
        self,
        fokus_pituus: int,
        peli: Peli | None = None,
        tekoalyt: list[Tekoaly] | None = None,
    ) -> None:
        """Luokan konstruktori.

        Args:
            fokus_pituus (int):
                Kuvaa monenko viimeisimmän kierroksen tuloksen perusteella tekoälyt pisteytetään.
            peli (Peli | None, optional):
                Pelin tuloksista vastaava olio. Oletukseltaan None.
            tekoalyt (list[Tekoaly] | None, optional):
                Tekoälyt, joita YhdistelmäTekoaly käyttää sisäisesti. Oletukseltaan None.

        Raises:
            ValueError: Ei-positiivinen fokus_pituus.
        """
        if fokus_pituus <= 0:
            raise ValueError("Ei-positiivinen fokus_pituus ei kelpaa.")

        self.__fokus_pituus: int = fokus_pituus
        self.__peli: Peli = peli or Peli()
        self.__tekoalyt: list[Tekoaly] = tekoalyt or [
            MarkovTekoaly(i, self.__peli.voittavat_siirrot)
            for i in range(1, fokus_pituus + 1)
        ]
        self.__pisteet: list[deque[int]] = [
            deque(maxlen=self.__fokus_pituus) for i in range(fokus_pituus)
        ]

        self.__pelaava_tekoaly: Tekoaly = self.hae_paras_tekoaly()
        self.__siirtoja_jaljella: int = fokus_pituus

    @property
    def pelaava_tekoaly(self) -> Tekoaly:
        return deepcopy(self.__pelaava_tekoaly)

    @property
    def siirtoja_jaljella(self) -> int:
        return self.__siirtoja_jaljella

    def __paivita_pisteet(self, syote: str) -> None:
        """Päivittää tekoälyjen pisteet.

        Args:
            syote (str): Pelaajan syöte viime kierroksella.
        """

        for i, tekoaly in enumerate(self.__tekoalyt):
            tulos = self.__peli.paata_voittaja(tekoaly.pelaa(), syote)
            self.__pisteet[i].append(tulos)

    def hae_tekoalyt_ja_pisteet(self) -> list[tuple[Tekoaly, tuple[int]]]:
        """Palauttaa tekoälyt ja vastaavat pistetilanteet.

        Returns:
            list[tuple[Tekoaly, tuple[int]]]:
                Lista, joka sisältää tekoälyt ja niiden pistetilanteen tuplena.
        """

        return [
            (tekoaly, tuple(self.__pisteet[i]))
            for i, tekoaly in enumerate(self.__tekoalyt)
        ]

    def hae_paras_tekoaly(self) -> Tekoaly:
        """Palauttaa parhaiten pelanneen tekoälyn.

        Returns:
            Tekoaly: Tekoäly, jolla on korkein pistemäärä.
        """

        paras_tekoaly = self.__tekoalyt[0]
        paras_pisteet = self.__pisteet[0]

        for i, tekoaly in enumerate(self.__tekoalyt):
            if self.__pisteet[i] > paras_pisteet:
                paras_tekoaly = tekoaly

        return paras_tekoaly

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
            self.__pelaava_tekoaly = self.hae_paras_tekoaly()
            self.__siirtoja_jaljella = self.__fokus_pituus

        self.__paivita_pisteet(syote)

        for tekoaly in self.__tekoalyt:
            tekoaly.lisaa(syote)
