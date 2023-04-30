from math import ceil

from services import peli_logiikka


class TilastoNakyma:
    def __init__(self) -> None:
        self.__tilasto: list[tuple[float, float, float]] = []
        self.__asteikko: int = 10
        self.__riveja: int = 10

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
            f"Kierroksia: {len(self.__tilasto)}",
            f"Voitot: {voitto_osuus:.0f} %",
            f"Tasapelit: {tasapeli_osuus:.0f} %",
            f"Häviöt: {havio_osuus:.0f} %",
            sep="\n",
        )
        print()

    def __tulosta_kuvaaja(self) -> None:
        kierroksia = len(self.__tilasto)
        indeksin_leveys = max(len(str(kierroksia)), 2)

        sarakkeiden_otsikot = "|".join(
            [
                f'{"i":<{indeksin_leveys}}',
                f'{"Voitot":<{self.__asteikko}}',
                f'{"Tasapelit":<{self.__asteikko}}',
                f'{"Häviöt":<{self.__asteikko}}',
            ]
        )
        erotin = "|".join(
            [
                f'{"-"*indeksin_leveys:>{indeksin_leveys}}',
                f'{"-"*self.__asteikko}',
                f'{"-"*self.__asteikko}',
                f'{"-"*self.__asteikko}',
            ]
        )

        print(f"|{sarakkeiden_otsikot}|")
        print(f"|{erotin}|")

        for i in range(
            0, max(kierroksia, self.__riveja), max(kierroksia // self.__riveja, 1)
        ):
            if i >= kierroksia:
                break

            voitot = ceil(self.__tilasto[i][0] * self.__asteikko)
            tasapelit = ceil(self.__tilasto[i][1] * self.__asteikko)
            haviot = ceil(self.__tilasto[i][2] * self.__asteikko)

            rivi = "|".join(
                [
                    f"{i+1:<{indeksin_leveys}}",
                    f'{"#"*voitot:{self.__asteikko}}',
                    f'{"#"*tasapelit:{self.__asteikko}}',
                    f'{"#"*haviot:{self.__asteikko}}',
                ]
            )

            print(f"|{rivi}|")

        print(f"# = {100//self.__asteikko} %")
