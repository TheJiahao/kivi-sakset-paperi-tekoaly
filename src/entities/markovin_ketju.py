import copy
from collections import deque
from typing import Any, Hashable


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

        return self.frekvenssit[syote].get(self.muisti, 0)

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
        """

        if len(self.muisti) < self.n or self.__hae_jonon_frekvenssi() == 0:
            return 0

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
