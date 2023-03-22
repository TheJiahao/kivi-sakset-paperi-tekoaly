from collections import deque
import random


class MarkovKetju:
    def __init__(self, pituus: int, vaihtoehdot: list[str]) -> None:
        self.__muisti: deque[str] = deque(maxlen=pituus)
        self.__max_pituus: int = pituus
        self.__todennakoisyydet: dict[tuple, float] = {}
        self.__vaihtoehtot: list[str] = vaihtoehdot
        self.__havaintoja: int = 0
        self.__frekvenssit: dict[tuple, int] = {}

    def lisaa(self, syote: str) -> None:
        self.__muisti.append(syote)
        self.__havaintoja += 1

        if len(self.__muisti) < self.__max_pituus:
            return

        jono = tuple(self.__muisti)
        self.__frekvenssit[jono] = self.__frekvenssit[jono] + 1 or 1
        self.__todennakoisyydet[jono] = self.__frekvenssit[jono] / self.__havaintoja

    def ennusta(self) -> str:
        seuraava_jono: tuple = tuple(random.sample(self.__vaihtoehtot, self.__max_pituus))

        if len(self.__todennakoisyydet) > 0:
            for jono, todennakoisyys in self.__todennakoisyydet:
                oletus_todennakoisyys = 1 / (
                    len(self.__vaihtoehtot) ** self.__max_pituus
                )

                if (
                    todennakoisyys > self.__todennakoisyydet[seuraava_jono]
                    or oletus_todennakoisyys
                ):
                    seuraava_jono = jono

        return seuraava_jono[-1]
