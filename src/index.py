from services.peli_logiikka import PeliLogiikka
from ui.ui import UI

if __name__ == "__main__":
    logiikka = PeliLogiikka()
    kayttoliittyma = UI(logiikka)
    kayttoliittyma.kaynnista()
