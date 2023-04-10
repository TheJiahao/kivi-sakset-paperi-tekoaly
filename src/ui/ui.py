from services.peli_logiikka import PeliLogiikka


class UI:
    def __init__(self) -> None:
        self.__logiikka: PeliLogiikka = PeliLogiikka()

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
        while True:
            try:
                syote = input("Syötä muistin pituus (oletus 5): ")

                if syote == "":
                    self.__logiikka = PeliLogiikka()
                else:
                    muistin_pituus = int(syote)
                    self.__logiikka = PeliLogiikka(n=muistin_pituus)
                break

            except ValueError:
                print("Virheellinen syöte, syötä kokonaisluku.")

        print('"k" = kivi, "s" = sakset, "p" = paperi')

        while True:
            syote = input("Pelaa (x lopettaa): ").lower()

            if syote == "x":
                self.__tulosta_tilasto()
                return

            if syote not in {"k", "s", "p"}:
                print("Syöte ei kelpaa, kokeile uudestaan.")
                continue

            pelitulos = self.__logiikka.pelaa(syote)

            print(f"Tekoäly pelasi {pelitulos[0]}")

            match pelitulos[1]:
                case -1:
                    print("Hävisit.")
                case 0:
                    print("Tasapeli.")
                case 1:
                    print("Voitit!")

    def __tulosta_tilasto(self) -> None:
        tilasto = self.__logiikka.hae_tilasto()

        print("Tilastosi")
        print(f"Voitot: {100*tilasto[0]:.0f} %")
        print(f"Tasapelit: {100*tilasto[1]:.0f} %")
        print(f"Häviöt: {100*tilasto[2]:.0f} %")
