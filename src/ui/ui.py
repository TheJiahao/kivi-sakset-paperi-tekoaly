from services.peli_logiikka import PeliLogiikka
from ui.alusta_peli_nakyma import AlustaPeliNakyma
from ui.peli_nakyma import PeliNakyma


class UI:
    def __init__(self, logiikka: PeliLogiikka) -> None:
        self.__alusta_peli_nakyma = AlustaPeliNakyma(logiikka)
        self.__peli_nakyma = PeliNakyma(logiikka)

    def kaynnista(self) -> None:
        print("Kivi-sakset-paperi-peli")

        while True:
            self.__tulosta_ohje()
            syote = input("Anna syöte: ").lower()

            match syote:
                case "x":
                    return

                case "1":
                    self.__aloita_peli()

    def __tulosta_ohje(self) -> None:
        print(
            "1: Pelaa",
            "x: Lopeta",
            sep="\n",
        )

    def __aloita_peli(self) -> None:
        self.__alusta_peli_nakyma.kaynnista()
        self.__peli_nakyma.kaynnista()
