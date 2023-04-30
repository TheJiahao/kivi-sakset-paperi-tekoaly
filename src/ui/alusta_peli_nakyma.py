from services import peli_logiikka


class AlustaPeliNakyma:
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

        while True:
            try:
                syote = input("Syötä muistin pituus (oletus 5): ")

                if syote == "":
                    n = 5
                else:
                    n = int(syote)

                return n

            except ValueError:
                print("Virheellinen syöte.")

    def __lue_tekoalyn_tila(self) -> bool:
        """Kysyy käyttäjältä vaihdetaanko tekoäly kierroksittain.

        Returns:
            bool: Jos True, niin vaihdetaan tekoäly kierroksittain.
        """

        while True:
            try:
                syote = input(
                    "Nopeammin sopeutuva tekoäly? (k: kyllä, e: ei, oletus kyllä): "
                )

                match syote.lower():
                    case "" | "k":
                        return True
                    case "e":
                        return False

            except ValueError:
                print("Virheellinen syöte.")
