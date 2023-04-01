from collections import deque

from entities.tekoalyt.markov_tekoaly import MarkovTekoaly
from entities.tekoalyt.tekoaly import Tekoaly
from entities.peli import Peli


class YhdistelmaTekoaly(Tekoaly):
    def __init__(self, fokus_pituus: int, peli: Peli) -> None:
        self.__fokus_pituus: int = fokus_pituus
        self.__tekoalyt: list[Tekoaly] = []
        self.__peli = peli
        self.__voittavat_siirrot: dict[str, str] = peli.voittavat_siirrot

        self.__alusta_tekoalyt()

        self.__pisteet: dict[Tekoaly, deque[int]] = {
            tekoaly: deque(maxlen=fokus_pituus) for tekoaly in self.__tekoalyt
        }

        self.__pelaava_tekoaly = self.__tekoalyt[0]
        self.__siirtoja_jaljella = fokus_pituus

    def __alusta_tekoalyt(self) -> None:
        for i in range(1, self.__fokus_pituus + 1):
            self.__tekoalyt.append(MarkovTekoaly(i, self.__voittavat_siirrot))

    def __vaihda_tekoaly(self) -> None:
        self.__pelaava_tekoaly = max(
            self.__tekoalyt, key=lambda x: sum(self.__pisteet[x])
        )

        self.__siirtoja_jaljella = self.__fokus_pituus

    def pelaa(self, syote: str) -> str:
        siirto = self.__pelaava_tekoaly.pelaa(syote)

        for tekoaly in self.__tekoalyt:
            pelattu = None

            if tekoaly == self.__pelaava_tekoaly:
                pelattu = siirto
            else:
                pelattu = tekoaly.pelaa(syote)

            tulos = self.__peli.paata_voittaja(pelattu, syote)

            self.__pisteet[tekoaly].append(tulos)

        if self.__siirtoja_jaljella == 0:
            self.__vaihda_tekoaly()

        return siirto

    def pisteyta(self) -> None:
        pass
