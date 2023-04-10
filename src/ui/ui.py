from services.peli_logiikka import PeliLogiikka
from entities.tekoalyt.yhdistelma_tekoaly import YhdistelmaTekoaly


class UI:
    def __init__(self, logiikka: PeliLogiikka) -> None:
        self.__logiikka: PeliLogiikka = logiikka
        self.__selitykset: dict[int, str] = {
            -1: "Hävisit.",
            0: "Tasapeli.",
            1: "Voitit!",
        }

    def kaynnista(self) -> None:
        print("Kivi-sakset-paperi-peli")

        while True:
            self.__tulosta_ohje()
            syote = input("Anna syöte: ").lower()

            match syote:
                case "x":
                    return

                case "1":
                    self.__aloita_kivi_sakset_paperi_peli()

    def __tulosta_ohje(self) -> None:
        print(
            """
1: Aloita peli
x: Lopeta
"""
        )

    def __aloita_kivi_sakset_paperi_peli(self) -> None:
        self.__alusta_kivi_sakset_paperi_peli()

        print('"k" = kivi, "s" = sakset, "p" = paperi')

        while True:
            try:
                syote = input("Pelaa (x lopettaa): ").lower()

                if syote == "x":
                    self.__tulosta_tilasto()
                    return

                pelitulos = self.__logiikka.pelaa(syote)

                print(f"Tekoäly pelasi {pelitulos[0]}")
                print(self.__selitykset[pelitulos[1]])

            except ValueError:
                print("Syöte ei kelpaa, kokeile uudestaan.")

    def __alusta_kivi_sakset_paperi_peli(self) -> None:
        while True:
            try:
                syote = input("Syötä muistin pituus (oletus 5): ")

                if syote == "":
                    self.__logiikka = PeliLogiikka()
                    return

                muistin_pituus = int(syote)
                self.__logiikka = PeliLogiikka(n=muistin_pituus)

            except ValueError:
                print("Virheellinen syöte, syötä kokonaisluku.")

            else:
                return

    def __tulosta_tilasto(self) -> None:
        tilasto = self.__logiikka.hae_tilasto()

        print("Tilasto")
        print(f"Voitot: {100*tilasto[0]:.0f} %")
        print(f"Tasapelit: {100*tilasto[1]:.0f} %")
        print(f"Häviöt: {100*tilasto[2]:.0f} %")
