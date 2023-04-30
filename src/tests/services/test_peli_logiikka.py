import unittest
from random import choice

from services.peli_logiikka import PeliLogiikka
from entities.tekoalyt.tekoaly import Tekoaly


class FakeTekoaly(Tekoaly):
    """Tekoäly testausta varten. Pelaa vuorotellen k, s, p."""

    def __init__(self) -> None:
        self.laskuri: int = 0
        self.vaihtoehdot: list[str] = ["k", "s", "p"]

    def lisaa(self, syote: str) -> None:
        self.laskuri += 1
        self.laskuri %= 3

    def pelaa(self) -> str:
        return self.vaihtoehdot[self.laskuri]

    def __eq__(self, toinen: object) -> bool:
        return True


class TestPeliLogiikka(unittest.TestCase):
    def setUp(self) -> None:
        self.logiikka = PeliLogiikka()
        self.kelpaavat_syotteet = ["k", "s", "p"]

    def test_pelaa_palauttaa_oikeanlaisen_tulosteen(self):
        for i in range(100):
            syote = choice(self.kelpaavat_syotteet)
            tulos = self.logiikka.pelaa(syote)

            self.assertIn(tulos[0], self.kelpaavat_syotteet)
            self.assertIn(tulos[1], [-1, 0, 1])

    def test_alusta(self):
        self.logiikka.pelaa("s")

        self.logiikka.alusta(10, True, tekoaly=FakeTekoaly())
        self.assertEqual(self.logiikka._PeliLogiikka__tilasto, [])
        self.assertEqual(self.logiikka._PeliLogiikka__tekoaly, FakeTekoaly())

    def test_hae_tilasto_palauttaa_tyhjan_listan_alussa(self):
        self.assertEqual(self.logiikka.hae_tilasto(), [])

    def test_hae_tilasto(self):
        logiikka = PeliLogiikka(FakeTekoaly())

        # Pelaaja häviää
        logiikka.pelaa("s")

        tilasto = logiikka.hae_tilasto()

        self.assertEqual(tilasto[0][0], 0)
        self.assertEqual(tilasto[0][1], 0)
        self.assertEqual(tilasto[0][2], 1)

        # Pelaaja voittaa
        logiikka.pelaa("k")

        tilasto = logiikka.hae_tilasto()

        self.assertEqual(tilasto[1][0], 0.5)
        self.assertEqual(tilasto[1][1], 0)
        self.assertEqual(tilasto[1][2], 0.5)

        # Tasapeli
        logiikka.pelaa("p")

        tilasto = logiikka.hae_tilasto()

        self.assertAlmostEqual(tilasto[2][0], 0.33, 2)
        self.assertAlmostEqual(tilasto[2][1], 0.33, 2)
        self.assertAlmostEqual(tilasto[2][2], 0.33, 2)
