from math import ceil

from services import peli_logiikka


class TilastoNakyma:
    def __init__(self) -> None:
        self.__tilasto: list[tuple[float, float, float]] = []

    def tulosta_tilasto(self) -> None:
        self.__tilasto = peli_logiikka.hae_tilasto()

        if self.__tilasto:
            self.__tulosta_kuvaaja()
            print()

            self.__tulosta_yhteenveto()

    def __tulosta_yhteenveto(self) -> None:
        voitto_osuus = 100 * self.__tilasto[-1][0]
        tasapeli_osuus = 100 * self.__tilasto[-1][1]
        havio_osuus = 100 * self.__tilasto[-1][2]

        print("Yhteenveto")
        print(
            f"Voitot: {voitto_osuus:.0f} %",
            f"Tasapelit: {tasapeli_osuus:.0f} %",
            f"Häviöt: {havio_osuus:.0f} %",
            sep="\n",
        )
        print()

    def __tulosta_kuvaaja(self) -> None:
        kierroksia = len(self.__tilasto)
        indeksin_leveys = max(len(str(kierroksia)), 2)
        asteikko = 20

        print(
            f'{" ":{indeksin_leveys}}',
            f'{"Voitot":<{asteikko}}',
            f'{"Tasapelit":<{asteikko}}',
            f'{"Häviöt":<{asteikko}}',
            sep="|",
            end="|\n",
        )
        print(
            f'{" ":{indeksin_leveys}}',
            f'{"-"*asteikko}',
            f'{"-"*asteikko}',
            f'{"-"*asteikko}',
            sep="|",
            end="|\n",
        )

        for i in range(0, max(kierroksia, 10), max(kierroksia // 10, 1)):
            voitot = 0
            tasapelit = 0
            haviot = 0

            if i < kierroksia:
                voitot = ceil(self.__tilasto[i][0] * asteikko)
                tasapelit = ceil(self.__tilasto[i][1] * asteikko)
                haviot = ceil(self.__tilasto[i][2] * asteikko)

            print(
                f"{i+1:<{indeksin_leveys}}",
                f'{"#"*voitot:{asteikko}}',
                f'{"#"*tasapelit:{asteikko}}',
                f'{"#"*haviot:{asteikko}}',
                sep="|",
                end="|\n",
            )

        print(f"# = {100//asteikko} %")
