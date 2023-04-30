from services import peli_logiikka


class PeliNakyma:
    """Luokka, joka vastaa varsinaisesta pelinäkymästä."""

    def __init__(self) -> None:
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
                    return

                for merkki in syote:
                    pelitulos = peli_logiikka.pelaa(merkki)

                    print(
                        f'(Sinä) "{merkki}" VS "{pelitulos[0]}" (Tekoäly)',
                        self.__selitykset[pelitulos[1]],
                    )

                print()

            except ValueError:
                print("Syöte ei kelpaa, kokeile uudestaan.")
