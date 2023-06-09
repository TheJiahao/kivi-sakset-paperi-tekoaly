from copy import copy


class Peli:
    """Luokka, joka kuvaa kivi-sakset-paperi-peliä."""

    def __init__(
        self,
        voittavat_siirrot: dict[str, str] | None = None,
    ) -> None:
        """Luokan konstruktori.

        Args:
            voittavat_siirrot (dict[str, str] | None, optional):
                Syötteitä vastaavat voittavat siirrot.
                Esimerkiksi syötettä "k" (kiveä) vastaa syöte "p" (paperi).
                Oletusarvoltaan None.
        """

        self.__voittavat_siirrot: dict[str, str] = voittavat_siirrot or {
            "k": "p",
            "s": "k",
            "p": "s",
        }
        self.__syotteet: set[str] = set(self.__voittavat_siirrot.keys())

    @property
    def voittavat_siirrot(self) -> dict[str, str]:
        return copy(self.__voittavat_siirrot)

    def paata_voittaja(self, pelaaja1: str, pelaaja2: str) -> int:
        """Päättää kivi-sakset-paperi-pelin voittajan.

        Args:
            pelaaja1 (str): Pelaajan 1 syöte.
            pelaaja2 (str): Pelaajan 2 syöte.

        Raises:
            ValueError: Merkkijono ei kelpaa.

        Returns:
            int: Palauttaa -1, 0 tai 1; mitkä vastaavat pelaajan 1 häviötä, tasapelia tai voittoa.
        """

        if pelaaja1 not in self.__syotteet or pelaaja2 not in self.__syotteet:
            raise ValueError("Virheellinen syöte.")

        tulos = 0

        if pelaaja1 != pelaaja2:
            tulos = -1

            if self.__voittavat_siirrot[pelaaja2] == pelaaja1:
                tulos = 1

        return tulos
