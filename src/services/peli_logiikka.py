from entities.peli import Peli
from entities.tekoalyt.tekoaly import Tekoaly
from entities.tekoalyt.yhdistelma_tekoaly import YhdistelmaTekoaly


class PeliLogiikka:
    """Luokka, joka vastaa sovelluksen logiikasta."""

    def __init__(
        self, tekoaly: Tekoaly | None = None, n: int = 5, peli: Peli | None = None
    ) -> None:
        """Luokan konstruktori.

        Args:
            tekoaly (Tekoaly | None, optional): Tekoälyä kuvaava olio. Oletukseltaan None.
            n (int, optional): Yhdistelmätekoälyn muistin pituus. Oletukseltaan 5.
            peli (Peli, optional): Pelituloksista vastaava olio. Oletuksteltaan None.
        """

        self.__peli: Peli = peli or Peli()
        self.__tekoaly: Tekoaly = tekoaly or YhdistelmaTekoaly(n, self.__peli)
        self.__tilasto: list[int] = []

    def alusta(self, n: int, tila: bool) -> None:
        """Luo uuden tekoälyn ja nollaa tilaston.

        Args:
            n (int): Uuden tekoälyn muistin pituus.
            tila (bool): YhdistelmaTekoaly-olion tila.
        """

        self.__tekoaly = YhdistelmaTekoaly(n, self.__peli, vaihto_kierroksittain=tila)
        self.__tilasto = []

    def pelaa(self, syote: str) -> tuple[str, int]:
        """Pelaa kierroksen ja palauttaa tekoälyn siirron sekä pelituloksen
        (-1: häviö, 0: tasapeli, 1: voitto).

        Args:
            syote (str): Pelaajan syöte.

        Returns:
            tuple[str, int]: Tuple, joka on muotoa (tekoälyn siirto, pelitulos).
        """

        tekoalyn_siirto = self.__tekoaly.pelaa()

        pelitulos = self.__peli.paata_voittaja(syote, tekoalyn_siirto)

        self.__tekoaly.lisaa(syote)
        self.__tilasto.append(pelitulos)

        return (tekoalyn_siirto, pelitulos)

    def hae_tilasto(self) -> list[tuple[float, float, float]]:
        """Palauttaa tilaston.

        Returns:
            list[tuple[float, float, float]]:
                Kumulatiivinen tilasto voitto-, tasapeli- ja häviöprosenteista.
        """

        tilasto = []
        laskurit = {-1: 0, 0: 0, 1: 0}

        for i, pelitulos in enumerate(self.__tilasto):
            laskurit[pelitulos] += 1

            voitto_osuus = laskurit[1] / (i + 1)
            tasapeli_osuus = laskurit[0] / (i + 1)
            havio_osuus = laskurit[-1] / (i + 1)

            tilasto.append((voitto_osuus, tasapeli_osuus, havio_osuus))

        return tilasto
