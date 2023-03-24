from collections import deque


def muodosta_osajonot(
    vaihtoehdot: set, n: int, osajonot: set[tuple] | None = None, k: int = 1
) -> set[tuple]:
    """Muodostaa vaihtoehdoista kaikki n-pituiset osajonot O(m^n) ajassa,
    missä m on osajonon alkioiden vaihtoehtojen määrä.

    Args:
        vaihtoehdot (set): Osajonon alkioiden vaihtoehtojen joukko.
        n (int): Haluttu osajonojen pituus.
        osajonot (set[tuple] | None, optional): k-pituisten osajonojen joukko. Oletukseltaan None.
        k (int, optional): osajonot-joukon pituus. Oletukseltaan 1.

    Returns:
        set[tuple]: n-pituisten osajonojen joukko.
    """

    if osajonot is None:
        osajonot = {(vaihtoehto,) for vaihtoehto in vaihtoehdot}

    if k == n:
        return osajonot

    uudet_osajonot = set()

    for jono in osajonot:
        for vaihtoehto in vaihtoehdot:
            uusi_jono = jono + (vaihtoehto,)
            uudet_osajonot.add(uusi_jono)

    return muodosta_osajonot(vaihtoehdot, n, uudet_osajonot, k + 1)


class MarkovinKetju:
    """Luokka, joka kuvaa Markovin ketjua."""

    def __init__(self, n: int, vaihtoehdot: list[str]) -> None:
        self.__muisti: deque[str] = deque(maxlen=n)
        self.__n: int = n
        self.__vaihtoehtot: list[str] = vaihtoehdot
        self.__havaintoja: int = 0
        self.__frekvenssit: dict[str, int] = {}
        self.__siirtymamatriisi: dict[str, dict[str, float]] = {}

        self.__alusta_siirtymamatriisi()

    def __alusta_siirtymamatriisi(self) -> None:
        """Alustaa siirtymämatriisin."""
        for vaihtoehto in self.__vaihtoehtot:
            for jono in muodosta_osajonot(
                set(self.__vaihtoehtot), set(self.__vaihtoehtot), self.__n
            ):
                self.__siirtymamatriisi[vaihtoehto][jono] = 1 / (
                    len(self.__vaihtoehtot) ** self.__n
                )

    def lisaa(self, syote: str) -> None:
        """Lisää Markovin ketjuun alkion ja päivittää todennäköisyyden.

        Args:
            syote (str): Lisättävä alkio.
        """

        if len(self.__muisti) < self.__n:
            self.__muisti.append(syote)
            self.__havaintoja += 1
            return

        jono = str(self.__muisti)

        self.__frekvenssit[jono] = self.__frekvenssit[jono] + 1 or 1
        self.__siirtymamatriisi[syote][jono] = (
            self.__frekvenssit[jono] / self.__havaintoja
        )

        self.__muisti.append(syote)

    def ennusta(self) -> str:
        """Palauttaa todennäköisimmän vaihtoehdon.

        Returns:
            str: Todennäköisin vaihtoehto.
        """
        return max(
            self.__vaihtoehtot,
            key=lambda x: self.__siirtymamatriisi[x][str(self.__muisti)],
        )
