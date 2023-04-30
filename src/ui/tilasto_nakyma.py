from services import peli_logiikka


class TilastoNakyma:
    def tulosta_tilasto(self) -> None:
        tilasto = peli_logiikka.hae_tilasto()

        print(
            "Tilasto",
            f"Voitot: {100*tilasto[0]:.0f} %",
            f"Tasapelit: {100*tilasto[1]:.0f} %",
            f"Häviöt: {100*tilasto[2]:.0f} %",
            sep="\n",
        )
        print()
