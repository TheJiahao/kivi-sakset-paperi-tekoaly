from services import peli_logiikka
from ui.nakyma import Nakyma


class AlustaPeliNakyma(Nakyma):
    """Luokka, joka vastaa pelin alustamisnäkymästä."""

    def kaynnista(self) -> None:
        n = self.__lue_muistin_pituus()
        tila = self.__lue_tekoalyn_tila()

        peli_logiikka.alusta(n, tila=tila)

    def __lue_muistin_pituus(self) -> int:
        """Kysyy käyttäjältä muistin pituuden.

        Returns:
            int: Muistin pituus.
        """
        return self._kysy_kokonaisluku(5, 1, "Syötä muistin pituus")

    def __lue_tekoalyn_tila(self) -> bool:
        """Kysyy käyttäjältä vaihdetaanko tekoäly kierroksittain.

        Returns:
            bool: Jos True, niin vaihdetaan tekoäly kierroksittain.
        """

        return self._kysy_kylla_tai_ei("k", "e", True, "Nopeammin sopeutuva tekoäly?")
