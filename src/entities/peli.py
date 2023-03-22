class Peli:
    """Luokka, joka kuvaa kivi-sakset-paperi-peliä."""

    def __init__(self, syotteet: dict[str, int] | None = None) -> None:
        """Luokan konstruktori.

        Args:
            syotteet (dict[str, int] | None, optional):
                Vapaaehtoinen, oletusarvoltaan None.
                Kuvaa merkkijonosyötteitä vastaavia lukuja.
        """
        self.__syotteet: dict[str, int] = syotteet or {"k": 0, "s": -1, "p": 1}

    def paata_voittaja(self, pelaaja1: str, pelaaja2: str) -> int:
        """Päättää kivi-sakset-paperi-pelin voittajan.

        Args:
            pelaaja1 (str): Pelaajan 1 syöte.
            pelaaja2 (str): Pelaajan 2 syöte.

        Returns:
            int: Palauttaa -1, 0 tai 1; mitkä vastaavat pelaajan 1 häviötä, tasapelia tai voittoa.
        """
        tulos = 0

        if pelaaja1 != pelaaja2:
            p1 = self.__muunna_luvuiksi(pelaaja1)
            p2 = self.__muunna_luvuiksi(pelaaja2)

            match p1:
                case -1:
                    if p1 * p2 == -1:
                        tulos = 1
                    else:
                        tulos = -1
                case 0:
                    if p1 > p2:
                        tulos = 1
                    else:
                        tulos = -1
                case 1:
                    if p1 * p2 != -1:
                        tulos = 1
                    else:
                        tulos = -1

        return tulos

    def __muunna_luvuiksi(self, merkki: str) -> int:
        """Muuttaa merkin vastaavaksi luvuksi

        Args:
            merkki (str): Merkkijono, joka kuvaa pelaajan syötettä.

        Raises:
            ValueError: Merkkijono ei kelpaa.

        Returns:
            int: Syötettä vastaava luku.
        """

        if merkki not in self.__syotteet:
            raise ValueError(f"Virheellinen merkki '{merkki}'.")

        return self.__syotteet[merkki]
