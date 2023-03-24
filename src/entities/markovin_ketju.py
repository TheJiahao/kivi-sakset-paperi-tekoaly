from collections import deque
from typing import Any, Hashable


def muodosta_jonot(
    vaihtoehdot: set, n: int, osajonot: set[tuple] | None = None, k: int = 1
) -> set[tuple]:
    """Muodostaa vaihtoehdoista kaikki n-pituiset osajonot O(m^n) ajassa,
    missä m on osajonon alkioiden vaihtoehtojen määrä.

    Args:
        vaihtoehdot (set): Osajonon alkioiden vaihtoehtojen joukko.
        n (int): Haluttu osajonojen pituus.
        osajonot (set[tuple] | None, optional): k-pituisten osajonojen joukko. Oletukseltaan None.
        k (int, optional): osajonot-joukon pituus. Oletukseltaan 1.

    Returns:
        set[tuple]: n-pituisten osajonojen joukko.
    """

    if osajonot is None:
        osajonot = {(vaihtoehto,) for vaihtoehto in vaihtoehdot}

    if k == n:
        return osajonot

    uudet_osajonot = set()

    for jono in osajonot:
        for vaihtoehto in vaihtoehdot:
            uusi_jono = jono + (vaihtoehto,)
            uudet_osajonot.add(uusi_jono)

    return muodosta_jonot(vaihtoehdot, n, uudet_osajonot, k + 1)


class MarkovinKetju:
    """Luokka, joka kuvaa Markovin ketjua."""

    def __init__(self, n: int, vaihtoehdot: set[Hashable]) -> None:
        self.__muisti: deque[Hashable] = deque(maxlen=n)
        self.__n: int = n
        self.__vaihtoehdot: set[Hashable] = vaihtoehdot
        self.__havainnot: dict[tuple, int] = {}
        self.__frekvenssit: dict[Hashable, dict[tuple, int]] = {}
        self.__siirtymamatriisi: dict[Hashable, dict[tuple, float]] = {}

        self.__alusta_siirtymamatriisi_ja_laskurit()

    def __alusta_siirtymamatriisi_ja_laskurit(self) -> None:
        """Alustaa siirtymämatriisin."""
        for vaihtoehto in self.__vaihtoehdot:
            self.__siirtymamatriisi[vaihtoehto] = {}
            self.__frekvenssit[vaihtoehto] = {}

            for jono in muodosta_jonot(self.__vaihtoehdot, self.__n):
                self.__siirtymamatriisi[vaihtoehto][jono] = 0
                self.__frekvenssit[vaihtoehto][jono] = 0

    def lisaa(self, syote: Hashable) -> None:
        """Lisää Markovin ketjuun alkion ja päivittää todennäköisyyden.

        Args:
            syote (Hashable): Lisättävä alkio.

        Raises:
            ValueError: Syote ei kelpaa.
        """

        if syote not in self.__vaihtoehdot:
            raise ValueError(f"Syote '{syote}' ei kelpaa.")

        if len(self.__muisti) == self.__n:
            jono = tuple(self.__muisti)
            self.__frekvenssit[syote][jono] = self.__frekvenssit[syote].get(jono, 0) + 1
            self.__havainnot[jono] = self.__havainnot.get(jono, 0) + 1

            self.__paivita_todennaikoisyydet(jono)

        self.__muisti.append(syote)

    def __paivita_todennaikoisyydet(self, jono) -> None:
        for vaihtoehto in self.vaihtoehdot:
            self.__siirtymamatriisi[vaihtoehto][jono] = (
                self.__frekvenssit[vaihtoehto][jono] / self.__havainnot[jono]
            )

    def ennusta(self) -> Any:
        """Palauttaa todennäköisimmän seuraavan vaihtoehdon.
        Alussa kaikkien vaihtoehtojen todennäköisyys on nolla,
        jolloin palautetaan satunnaisesti jokin vaihtoehto.

        Returns:
            Any: Todennäköisin seuraava vaihtoehto.
        """
        return max(
            self.__vaihtoehdot,
            key=lambda x: self.__siirtymamatriisi[x][self.muisti],
        )

    @property
    def muisti(self) -> tuple:
        """Palauttaa muistin tuplena.
        Tuple helpottaa käsittelyä.

        Returns:
            tuple: Muisti tuplena.
        """
        return tuple(self.__muisti)

    @property
    def n(self) -> int:
        return self.__n

    @property
    def vaihtoehdot(self) -> set[Hashable]:
        return self.__vaihtoehdot

    @property
    def havainnot(self) -> dict[tuple, int]:
        return self.__havainnot

    @property
    def frekvenssit(self) -> dict[Hashable, dict[tuple, int]]:
        return self.__frekvenssit

    @property
    def siirtymamatriisi(self) -> dict[Hashable, dict[tuple, float]]:
        return self.__siirtymamatriisi
