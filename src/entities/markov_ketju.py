from collections import deque
from copy import deepcopy
from typing import Hashable


class MarkovKetju:
    """Luokka, joka kuvaa Markovin ketjua."""

    def __init__(self, n: int, vaihtoehdot: set[Hashable]) -> None:
        """Luokan konstruktori.

        Args:
            n (int): Muistin maksimipituus.
            vaihtoehdot (set[Hashable]): Sallitut vaihtoehdot.
        """
        self.__muisti: deque[Hashable] = deque(maxlen=n)
        self.__vaihtoehdot: dict[Hashable, int] = {
            vaihtoehto: i for i, vaihtoehto in enumerate(vaihtoehdot)
        }
        self.__frekvenssit: dict[Hashable, dict[int, int]] = {
            vaihtoehto: {} for vaihtoehto in vaihtoehdot
        }

        self.__n: int = n
        self.__k: int = len(vaihtoehdot)
        self.__hajautusarvo: int = 0
        self.__k_potenssiin_n: int = self.__k**n

    def __eq__(self, toinen: object) -> bool:
        if isinstance(toinen, MarkovKetju):
            return (
                self.muisti == toinen.muisti
                and self.n == toinen.n
                and self.vaihtoehdot == toinen.vaihtoehdot
                and self.frekvenssit == toinen.frekvenssit
            )

        return False

    def __repr__(self) -> str:
        vaihtoehdot = set(self.__vaihtoehdot.keys())

        return f"MarkovKetju({self.__n}, {vaihtoehdot})"

    @property
    def muisti(self) -> deque:
        return deepcopy(self.__muisti)

    @property
    def n(self) -> int:
        return self.__n

    @property
    def k(self) -> int:
        return self.__k

    @property
    def vaihtoehdot(self) -> dict[Hashable, int]:
        return deepcopy(self.__vaihtoehdot)

    @property
    def frekvenssit(self) -> dict[Hashable, dict[int, int]]:
        return deepcopy(self.__frekvenssit)

    def lisaa(self, syote: Hashable) -> None:
        """Lisää Markovin ketjuun alkion ja päivittää frekvenssin.

        Args:
            syote (Hashable): Lisättävä alkio.

        Raises:
            ValueError: Syöte ei kelpaa.
        """

        if syote not in self.__vaihtoehdot:
            raise ValueError(f"Syote '{syote}' ei kelpaa.")

        oikea_numero = self.__vaihtoehdot[syote]
        vasen_numero = 0

        if len(self.__muisti) == self.__n:
            self.__frekvenssit[syote][self.__hajautusarvo] = (
                self.hae_frekvenssi(syote) + 1
            )

            vasen_numero = self.__vaihtoehdot[self.__muisti[0]]

        self.__muisti.append(syote)
        self.paivita_hajautusarvo(vasen_numero, oikea_numero)

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
        Palauttaa nollan, kun muisti ei ole täynnä.

        Args:
            syote (Hashable): Syöte, jonka frekvenssiä haetaan.

        Returns:
            int: Haettavan syötteen frekvenssi.

        Raises:
            ValueError: Syöte ei kelpaa.
        """

        if syote not in self.__vaihtoehdot:
            raise ValueError(f"Syote '{syote}' ei kelpaa.")

        return self.__frekvenssit[syote].get(self.__hajautusarvo, 0)

    def paivita_hajautusarvo(self, vasen: int, oikea: int) -> None:
        uusi = self.__hajautusarvo
        uusi *= self.__k
        uusi += oikea
        uusi -= vasen * self.__k_potenssiin_n

        self.__hajautusarvo = uusi
