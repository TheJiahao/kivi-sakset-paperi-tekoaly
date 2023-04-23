from services.peli_logiikka import PeliLogiikka


class PeliNakyma:
    def __init__(self, logiikka: PeliLogiikka) -> None:
        self.__logiikka = logiikka
        self.__selitykset: dict[int, str] = {
            -1: "Hävisit.",
            0: "Tasapeli.",
            1: "Voitit!",
        }

    def kaynnista(self) -> None:
        print("k: kivi, s: sakset, p: paperi")

        while True:
            try:
                syote = input("Pelaa (x lopettaa): ").lower()

                if syote == "x":
                    self.tulosta_tilasto()
                    return

                pelitulos = self.__logiikka.pelaa(syote)

                print(f"Tekoäly pelasi {pelitulos[0]}")
                print(self.__selitykset[pelitulos[1]])

            except ValueError:
                print("Syöte ei kelpaa, kokeile uudestaan.")

    def tulosta_tilasto(self) -> None:
        tilasto = self.__logiikka.hae_tilasto()

        print("Tilasto")
        print(f"Voitot: {100*tilasto[0]:.0f} %")
        print(f"Tasapelit: {100*tilasto[1]:.0f} %")
        print(f"Häviöt: {100*tilasto[2]:.0f} %")
