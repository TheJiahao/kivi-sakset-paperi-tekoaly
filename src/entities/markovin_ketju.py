from collections import deque


def muodosta_osajonot(
    osajonot: set[str], vaihtoehdot: set[str], n: int, k: int = 1
) -> set[str]:
    """Muodostaa kaikki n-pituiset osajonot O(m^n) ajassa,
    missä m on jonon jäsenen vaihtoehtojen määrä.

    Args:
        osajonot (set[str]): Joukko, joka sisältää kaikki k-pituiset osajonot.
        vaihtoehdot (set[str]): Joukko, joka sisältää kaikki jonon jäsenten vaihtoehdot.
        k (int): Vapaaehtoinen, oletukseltaan 1. Kuvaa osajonojen pituutta.
        n (int): Kuvaa osajonojen suurinta pituutta.

    Returns:
        set[str]: Joukko, joka sisätää osajonot merkkijonoina.
    """

    if k == n:
        return osajonot

    uudet_osajonot = set()

    for jono in osajonot:
        for vaihtoehto in vaihtoehdot:
            uudet_osajonot.add(jono + vaihtoehto)

    return muodosta_osajonot(uudet_osajonot, vaihtoehdot, n, k + 1)


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
