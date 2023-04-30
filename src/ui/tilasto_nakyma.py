from math import ceil

from services import peli_logiikka
from ui.nakyma import Nakyma


class TilastoNakyma(Nakyma):
    def __init__(self) -> None:
        self.__tilasto: list[tuple[float, float, float]] = []
        self.__asteikko: int = 10
        self.__riveja: int = 10

    def kaynnista(self) -> None:
        self.__tilasto = peli_logiikka.hae_tilasto()

        if self.__tilasto:
            print("Tilasto")
            self.__asteikko = self._kysy_kokonaisluku(10, 1, "Kuvaajan asteikko")
            self.__riveja = self._kysy_kokonaisluku(10, 1, "Kuvaajan rivimäärä")
            print()

            self.__tulosta_tilasto()

    def __tulosta_tilasto(self) -> None:
        self.__tulosta_kuvaaja()
        print()
        self.__tulosta_yhteenveto()

    def __tulosta_yhteenveto(self) -> None:
        voitto_osuus = 100 * self.__tilasto[-1][0]
        tasapeli_osuus = 100 * self.__tilasto[-1][1]
        havio_osuus = 100 * self.__tilasto[-1][2]

        print("Yhteenveto")
        print(
            f"Kierroksia: {len(self.__tilasto)}",
            f"Voitot: {voitto_osuus:.0f} %",
            f"Tasapelit: {tasapeli_osuus:.0f} %",
            f"Häviöt: {havio_osuus:.0f} %",
            sep="\n",
        )
        print()

    def __muodosta_rivi(
        self,
        i: int | str,
        sarakkeet: list[str],
        indeksin_leveys: int,
        sarake_leveys: int,
    ) -> str:
        sisalto = [f"{sarake:<{sarake_leveys}}" for sarake in sarakkeet]
        rivi = "|".join(sisalto)

        return f"|{i:<{indeksin_leveys}}|{rivi}|"

    def __tulosta_kuvaaja(self) -> None:
        kierroksia = len(self.__tilasto)
        indeksin_leveys = max(len(str(kierroksia)), 2)

        sarakkeiden_otsikot = self.__muodosta_rivi(
            "i",
            ["Voitot", "Tasapelit", "Häviöt"],
            indeksin_leveys,
            self.__asteikko,
        )
        erotin = self.__muodosta_rivi(
            "-" * indeksin_leveys,
            ["-" * self.__asteikko] * 3,
            indeksin_leveys,
            self.__asteikko,
        )

        print("Kuvaaja")
        print(sarakkeiden_otsikot)
        print(erotin)

        for i in range(
            0, max(kierroksia, self.__riveja), max(kierroksia // self.__riveja, 1)
        ):
            if i >= kierroksia:
                break

            voitot = ceil(self.__tilasto[i][0] * self.__asteikko)
            tasapelit = ceil(self.__tilasto[i][1] * self.__asteikko)
            haviot = ceil(self.__tilasto[i][2] * self.__asteikko)

            rivi = self.__muodosta_rivi(
                i + 1,
                ["#" * voitot, "#" * tasapelit, "#" * haviot],
                indeksin_leveys,
                self.__asteikko,
            )

            print(rivi)

        print(f"# = {100//self.__asteikko} %")
