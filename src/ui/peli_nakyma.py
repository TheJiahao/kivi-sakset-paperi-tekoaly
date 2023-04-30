from services.peli_logiikka import PeliLogiikka


class PeliNakyma:
    """Luokka, joka vastaa varsinaisesta pelinäkymästä."""

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
                    self.__tulosta_tilasto()
                    return

                for merkki in syote:
                    pelitulos = self.__logiikka.pelaa(merkki)

                    print(
                        f'(Sinä) "{merkki}" VS "{pelitulos[0]}" (Tekoäly)',
                        self.__selitykset[pelitulos[1]],
                    )

                print()

            except ValueError:
                print("Syöte ei kelpaa, kokeile uudestaan.")

    def __tulosta_tilasto(self) -> None:
        tilasto = self.__logiikka.hae_tilasto()

        print(
            "Tilasto",
            f"Voitot: {100*tilasto[0]:.0f} %",
            f"Tasapelit: {100*tilasto[1]:.0f} %",
            f"Häviöt: {100*tilasto[2]:.0f} %",
            sep="\n",
        )
        print()
