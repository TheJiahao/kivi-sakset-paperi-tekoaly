import unittest
from random import choice

from services.peli_logiikka import PeliLogiikka


class TestPeliLogiikka(unittest.TestCase):
    def setUp(self) -> None:
        self.__logiikka = PeliLogiikka()
        self.__kelpaavat_syotteet = ["k", "s", "p"]

    def test_pelaa_palauttaa_oikeanlaisen_tulosteen(self):
        for i in range(100):
            syote = choice(self.__kelpaavat_syotteet)
            tulos = self.__logiikka.pelaa(syote)

            self.assertIn(tulos[0], self.__kelpaavat_syotteet)
            self.assertIn(tulos[1], [-1, 0, 1])

    def test_hae_tilasto_palauttaa_nollia_alussa(self):
        self.assertEqual(self.__logiikka.hae_tilasto(), (0, 0, 0))

    def test_hae_tilasto_palauttaa_arvoja_nollan_ja_yhden_valilta(self):
        for i in range(100):
            syote = choice(self.__kelpaavat_syotteet)
            self.__logiikka.pelaa(syote)
            tilasto = self.__logiikka.hae_tilasto()

            self.assertTrue(0 <= tilasto[0] <= 1)
            self.assertTrue(0 <= tilasto[1] <= 1)
            self.assertTrue(0 <= tilasto[2] <= 1)
