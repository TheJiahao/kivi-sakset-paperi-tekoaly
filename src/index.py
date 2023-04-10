from ui.ui import UI
from services.peli_logiikka import PeliLogiikka

if __name__ == "__main__":
    logiikka = PeliLogiikka()
    kayttoliittyma = UI(logiikka)
    kayttoliittyma.kaynnista()
