import copy
from collections import deque
from typing import Any, Hashable


def muodosta_jonot(
    vaihtoehdot: set, n: int, osajonot: set[tuple] | None = None, k: int = 1
) -> set[tuple]:
    """Muodostaa annetuista vaihtoehdoista kaikki n-pituiset jonot O(m^n) ajassa,
    missä m on osajonon alkioiden vaihtoehtojen määrä.

    Args:
        vaihtoehdot (set): Osajonon alkioiden vaihtoehtojen joukko.
        n (int): Haluttu osajonojen pituus.
        osajonot (set[tuple] | None, optional): k-pituisten osajonojen joukko. Oletukseltaan None.
        k (int, optional): osajonot-joukon pituus. Oletukseltaan 1.

    Returns:
        set[tuple]: n-pituisten jonojen joukko.
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

    def __init__(
        self,
        n: int,
        vaihtoehdot: set[Hashable],
        frekvenssit: dict[Hashable, dict[tuple, int]] | None = None,
    ) -> None:
        """Luokan konstruktori. Luo Markovin ketjun.

        Args:
            n (int):
                Muistin maksimipituus.
            vaihtoehdot (set[Hashable]):
                Joukko, joka sisältää sallitut syötteet.
            frekvenssit (dict[Hashable, dict[tuple, int]] | None, optional):
                Matriisi, joka sisältää jokaisen syötteen vastaavalla jonolla.
                Esimerkiksi __frekvenssit["a"][("a", "b", "c")] kuvaa,
                montako kertaa "a" on havaittu suoraan jonon ("a", "b", "c") jälkeen.
                Oletusarvoltaan None.
        """
        self.__muisti: deque[Hashable] = deque(maxlen=n)
        self.__n: int = n
        self.__vaihtoehdot: set[Hashable] = vaihtoehdot
        self.__frekvenssit: dict[Hashable, dict[tuple, int]] = frekvenssit or {}

        self.__alusta_laskurit()

    def __alusta_laskurit(self) -> None:
        """Alustaa frekvenssit nolliksi O(m^n) ajassa,
        missä m on muistin vaihtoehtojen määrä ja n muistin pituus."""

        for vaihtoehto in self.__vaihtoehdot:
            jonot = muodosta_jonot(self.__vaihtoehdot, self.__n)
            self.__frekvenssit[vaihtoehto] = {jono: 0 for jono in jonot}

    @property
    def muisti(self) -> tuple:
        """Palauttaa muistin tuplena, mikä helpottaa käsittelyä.

        Returns:
            tuple: Muisti tuplena.
        """

        return tuple(self.__muisti)

    @property
    def n(self) -> int:
        return self.__n

    @property
    def vaihtoehdot(self) -> set[Hashable]:
        return copy.deepcopy(self.__vaihtoehdot)

    @property
    def frekvenssit(self) -> dict[Hashable, dict[tuple, int]]:
        return copy.deepcopy(self.__frekvenssit)

    def lisaa(self, syote: Hashable) -> None:
        """Lisää Markovin ketjuun alkion ja päivittää todennäköisyyden.

        Args:
            syote (Hashable): Lisättävä alkio.

        Raises:
            ValueError: Syote ei kelpaa.
        """

        if syote not in self.__vaihtoehdot:
            raise ValueError(f"Syote '{syote}' ei kelpaa.")

        if len(self.muisti) == self.n:
            self.__frekvenssit[syote][self.muisti] = self.hae_frekvenssi(syote) + 1

        self.__muisti.append(syote)

    def ennusta(self) -> Any:
        """Palauttaa todennäköisimmän seuraavan vaihtoehdon.
        Alussa kaikkien vaihtoehtojen frekvenssi on nolla,
        jolloin palautetaan satunnaisesti jokin vaihtoehto.

        Returns:
            Any: Todennäköisin seuraava vaihtoehto.
        """

        return max(
            self.__vaihtoehdot,
            key=self.hae_frekvenssi,
        )

    def hae_frekvenssi(self, syote: Hashable) -> int:
        """Palauttaa syotteen frekvenssin, kun edeltävä jono on muistissa oleva jono.

        Args:
            syote (Hashable): Syote, jonka frekvenssiä haetaan.

        Returns:
            int: Haettavan syotteen frekvenssi.

        Raises:
            ValueError: Syote ei kelpaa.
        """

        if syote not in self.__vaihtoehdot:
            raise ValueError(f"Syote '{syote}' ei kelpaa.")

        if len(self.muisti) < self.n:
            return 0

        return self.frekvenssit[syote][self.muisti]

    def __hae_jonon_frekvenssi(self) -> int:
        """Palauttaa kuinka monta kertaa muistissa oleva jono on havaittu edeltävänä jonona.

        Returns:
            int: Muistissa olevan jonon frekvenssi.
        """

        return sum(self.hae_frekvenssi(vaihtoehto) for vaihtoehto in self.__vaihtoehdot)

    def hae_todennakoisyys(self, syote: Hashable) -> float:
        """Palauttaa todennäköisyyden, että annettu syote on seuraava ennuste.
        Jos muisti ei ole täynnä tai tämänhetkinen jono on ensimmäistä kertaa havaittu,
        niin palauttaa 0.

        Args:
            syote (Hashable): Syote, jonka todennäköisyyttä haetaan.

        Returns:
            float: Todennäköisyys, että annettu syote on seuraava ennuste.

        Raises:
            ValueError: Syote ei kelpaa.
        """

        if syote not in self.__vaihtoehdot:
            raise ValueError(f"Syote '{syote}' ei kelpaa.")

        if len(self.muisti) < self.n or self.__hae_jonon_frekvenssi() == 0:
            return 0

        return self.frekvenssit[syote][self.muisti] / self.__hae_jonon_frekvenssi()

    def hae_todennakoisyydet(self) -> dict[Hashable, float]:
        """Palauttaa tilastolliset todennäköisyydet seuraavalle ennusteelle.

        Returns:
            dict[Hashable, float]:
                Sanakirja, joka sisältää jokaista vaihtoehtoa vastaavan todennäköisyyden.
        """

        return {
            vaihtoehto: self.hae_todennakoisyys(vaihtoehto)
            for vaihtoehto in self.__vaihtoehdot
        }
