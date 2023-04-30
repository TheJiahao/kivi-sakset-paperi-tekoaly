from collections import deque
from copy import deepcopy

from entities.peli import Peli
from entities.tekoalyt.markov_tekoaly import MarkovTekoaly
from entities.tekoalyt.tekoaly import Tekoaly


class YhdistelmaTekoaly(Tekoaly):
    """Luokka, joka kuvaa usean tekoälyn muodostamaa yhdistelmätekoälyä."""

    def __init__(
        self,
        fokus_pituus: int,
        peli: Peli,
        vaihto_kierroksittain: bool = False,
        tekoalyt: list[Tekoaly] | None = None,
    ) -> None:
        """Luokan konstruktori.

        Args:
            fokus_pituus (int):
                Kuvaa monenko viimeisimmän kierroksen tuloksen perusteella tekoälyt pisteytetään.
            peli (Peli):
                Pelin tuloksista vastaava olio.
            vaihto_kierroksittain (bool):
                Jos True, niin tekoäly vaihdetaan kierroksittain.
            tekoalyt (list[Tekoaly] | None, optional):
                Tekoälyt, joita YhdistelmäTekoaly käyttää sisäisesti. Oletukseltaan None.

        Raises:
            ValueError: Ei-positiivinen fokus_pituus.
        """

        if fokus_pituus <= 0:
            raise ValueError("Ei-positiivinen fokus_pituus ei kelpaa.")

        self.__fokus_pituus: int = fokus_pituus
        self.__peli: Peli = peli
        self.__tekoalyt: list[Tekoaly] = tekoalyt or [
            MarkovTekoaly(i, self.__peli.voittavat_siirrot)
            for i in range(1, fokus_pituus + 1)
        ]
        self.__pisteet: list[int] = [0] * len(self.__tekoalyt)
        self.__pistejono: list[deque[int]] = [
            deque([0] * fokus_pituus, maxlen=fokus_pituus) for i in range(fokus_pituus)
        ]

        self.__vaihto_kierroksittain: bool = vaihto_kierroksittain
        self.__pelaava_tekoaly: Tekoaly = self.hae_paras_tekoaly()
        self.__siirtoja_jaljella: int = fokus_pituus

    def __repr__(self) -> str:
        return (
            f"YhdistelmaTekoaly({self.__fokus_pituus}, "
            + f"{self.__vaihto_kierroksittain}, "
            + f"{self.__tekoalyt}"
            + ")"
        )

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

            self.__pisteet[i] -= self.__pistejono[i][0]
            self.__pisteet[i] += tulos

            self.__pistejono[i].append(tulos)

    def hae_tekoalyt_ja_pisteet(self) -> list[tuple[Tekoaly, int]]:
        """Palauttaa tekoälyt ja vastaavat pisteet.

        Returns:
            list[tuple[Tekoaly, int]]:
                Lista, joka sisältää tekoälyt ja vastaavat pisteet tuplena.
        """

        return [
            (tekoaly, self.__pisteet[i]) for i, tekoaly in enumerate(self.__tekoalyt)
        ]

    def hae_paras_tekoaly(self) -> Tekoaly:
        """Palauttaa parhaiten pelanneen tekoälyn.

        Returns:
            Tekoaly: Tekoäly, jolla on korkein pistemäärä.
        """
        paras_indeksi = max(
            range(len(self.__tekoalyt)), key=lambda i: self.__pisteet[i]
        )

        return self.__tekoalyt[paras_indeksi]

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

        self.__paivita_pisteet(syote)
        self.__siirtoja_jaljella -= 1

        if self.__siirtoja_jaljella == 0 or self.__vaihto_kierroksittain:
            self.__pelaava_tekoaly = self.hae_paras_tekoaly()
            self.__siirtoja_jaljella = self.__fokus_pituus

        for tekoaly in self.__tekoalyt:
            tekoaly.lisaa(syote)
