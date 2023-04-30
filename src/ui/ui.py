from ui.alusta_peli_nakyma import AlustaPeliNakyma
from ui.peli_nakyma import PeliNakyma
from ui.tilasto_nakyma import TilastoNakyma


class UI:
    """Luokka, joka vastaa aloitusnäkymästä."""

    def __init__(self) -> None:
        self.__alusta_peli_nakyma = AlustaPeliNakyma()
        self.__peli_nakyma = PeliNakyma()
        self.__tilasto_nakyma = TilastoNakyma()

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
                    print()
                    self.__tilasto_nakyma.kaynnista()

    def __tulosta_ohje(self) -> None:
        print(
            "1: Pelaa",
            "x: Lopeta",
            sep="\n",
        )

    def __aloita_peli(self) -> None:
        self.__alusta_peli_nakyma.kaynnista()
        self.__peli_nakyma.kaynnista()
