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
        self.__tilasto: dict[int, int] = {-1: 0, 0: 0, 1: 0}

    def alusta(self, n: int, tila: bool) -> None:
        """Luo uuden tekoälyn ja nollaa tilaston.

        Args:
            n (int): Uuden tekoälyn muistin pituus.
            tila (bool): YhdistelmaTekoaly-olion tila.
        """

        self.__tekoaly = YhdistelmaTekoaly(n, self.__peli, vaihto_kierroksittain=tila)
        self.__tilasto = {-1: 0, 0: 0, 1: 0}

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

        self.__tilasto[pelitulos] = self.__tilasto[pelitulos] + 1
        self.__tekoaly.lisaa(syote)

        return (tekoalyn_siirto, pelitulos)

    def hae_tilasto(self) -> tuple[float, float, float]:
        """Palauttaa pelin tilaston eli voittojen, tasapelien ja häviöiden osuuden.

        Returns:
            tuple[float, float, float]:
                Tuple, joka on muotoa (voittojen osuus, tasapelien osuus, häviöiden osuus)
        """

        kierroksia = self.__tilasto[-1] + self.__tilasto[0] + self.__tilasto[1]

        if kierroksia == 0:
            return (0, 0, 0)

        voittojen_osuus = self.__tilasto[1] / kierroksia
        tasapelien_osuus = self.__tilasto[0] / kierroksia
        havioiden_osuus = self.__tilasto[-1] / kierroksia

        return (voittojen_osuus, tasapelien_osuus, havioiden_osuus)
