class Peli:
    """Luokka, joka kuvaa kivi-sakset-paperi-peliä.

    Attributes:
        __syotteet (set[str]): Joukko, joka sisältää kaikki sallitut syötteet.
    """

    def __init__(self, syotteet: set[str] | None = None) -> None:
        """Luokan konstruktori.

        Args:
            syotteet (set[str] | None, optional):
                Vapaaehtoinen, oletusarvoltaan None.
                Kuvaa merkkijonosyötteitä vastaavia lukuja.
        """
        self.__syotteet: set[str] = syotteet or {"k", "s", "p"}

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
            voittotapaukset = {"ks", "sp", "pk"}

            if pelaaja1 + pelaaja2 in voittotapaukset:
                tulos = 1

        return tulos
