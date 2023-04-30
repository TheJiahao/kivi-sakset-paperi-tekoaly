from abc import ABC, abstractmethod


class Nakyma(ABC):
    @abstractmethod
    def kaynnista(self) -> None:
        pass

    def _kysy_kokonaisluku(self, oletusarvo: int, alaraja: int, selite: str) -> int:
        """Kysyy käyttäjältä kokonaisluvun.

        Args:
            oletusarvo (int): Arvo, joka palautetaan käyttäjän syöttäessä tyhjä merkkijono.
            selite (str): Selite.

        Returns:
            int: Käyttäjän syöttämä kokonaisluku.
        """

        ohje = f"{selite} (oletus {oletusarvo}): "

        while True:
            try:
                if (syote := input(ohje)) == "":
                    return oletusarvo

                luku = int(syote)

                if luku < alaraja:
                    raise ValueError

                return luku

            except ValueError:
                print("Virheellinen syöte.")

    def _kysy_kylla_tai_ei(
        self,
        kylla: str,
        ei: str,
        oletusarvo: bool,
        kysymys: str,
        virheviesti: str = "Virheellinen syöte.",
    ) -> bool:
        """Kysyy käyttäjältä kyllä/ei kysymyksen ja palauttaa vastauksen.

        Args:
            kylla (str): Kyllä-vaihtoehtoa vastaava merkkijono.
            ei (str): Ei-vaihtoehtoa vastaava merkkijono.
            oletusarvo (bool): Arvo, joka palautetaan käyttäjän syöttäessä tyhjä merkkijono.
            kysymys (str): Kysymys.
            virheviesti (str, optional): Virheviesti. Oletukseltaan "Virheellinen syöte.".

        Returns:
            bool: _description_
        """

        kylla = kylla.lower()
        ei = ei.lower()
        vastaukset = {kylla: True, ei: False, "": True}

        if oletusarvo:
            oletusselite = "kyllä"
        else:
            oletusselite = "ei"

        ohje = f"{kysymys} ({kylla}: kyllä, {ei}: ei, oletus {oletusselite}): "

        while True:
            try:
                syote = input(ohje)
                return vastaukset[syote]

            except KeyError:
                print(virheviesti)
