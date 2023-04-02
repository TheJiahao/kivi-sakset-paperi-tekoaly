import copy
from collections import deque
from typing import Hashable


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
                Matriisi, joka sisältää jokaisen syötteen frekvenssin jonkin jonon perässä.
                Oletusarvoltaan None.
        """
        self.__muisti: deque[Hashable] = deque(maxlen=n)
        self.__n: int = n
        self.__vaihtoehdot: set[Hashable] = vaihtoehdot
        self.__frekvenssit: dict[Hashable, dict[tuple, int]] = frekvenssit or {
            vaihtoehto: {} for vaihtoehto in vaihtoehdot
        }

    def __eq__(self, toinen: "MarkovinKetju") -> bool:
        return (
            self.muisti == toinen.muisti
            and self.n == toinen.n
            and self.vaihtoehdot == toinen.vaihtoehdot
            and self.frekvenssit == toinen.frekvenssit
        )

    def __hash__(self) -> int:
        return hash(self.n + hash(tuple(self.vaihtoehdot)))

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

    def ennusta(self) -> Hashable:
        """Palauttaa todennäköisimmän seuraavan vaihtoehdon.
        Alussa kaikkien vaihtoehtojen frekvenssi on nolla,
        jolloin palautetaan satunnaisesti jokin vaihtoehto.

        Returns:
            Hashable: Todennäköisin seuraava vaihtoehto.
        """

        return max(
            self.__vaihtoehdot,
            key=self.hae_frekvenssi,
        )

    def hae_frekvenssi(self, syote: Hashable) -> int:
        """Palauttaa syotteen frekvenssin, kun edeltävä jono on muistissa oleva jono.
        Palauttaa nollan myös, kun muisti ei ole täynnä, mikä helpottaa todennäköisyyksien laskua.

        Args:
            syote (Hashable): Syote, jonka frekvenssiä haetaan.

        Returns:
            int: Haettavan syotteen frekvenssi.

        Raises:
            ValueError: Syote ei kelpaa.
        """

        if syote not in self.__vaihtoehdot:
            raise ValueError(f"Syote '{syote}' ei kelpaa.")

        return self.frekvenssit[syote].get(self.muisti, 0)

    def __hae_jonon_frekvenssi(self) -> int:
        """Palauttaa kuinka monta kertaa muistissa oleva jono on havaittu edeltävänä jonona.

        Returns:
            int: Muistissa olevan jonon frekvenssi.
        """

        return sum(self.hae_frekvenssi(vaihtoehto) for vaihtoehto in self.vaihtoehdot)

    def hae_todennakoisyys(self, syote: Hashable) -> float:
        """Palauttaa todennäköisyyden, että annettu syote on seuraava ennuste.

        Args:
            syote (Hashable): Syote, jonka todennäköisyyttä haetaan.

        Returns:
            float: Todennäköisyys, että annettu syote on seuraava ennuste.
        """

        if self.__hae_jonon_frekvenssi() == 0:
            return 1 / len(self.vaihtoehdot)

        return self.hae_frekvenssi(syote) / self.__hae_jonon_frekvenssi()

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
