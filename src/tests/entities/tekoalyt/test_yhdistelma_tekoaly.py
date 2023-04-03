import unittest

from entities.peli import Peli
from entities.tekoalyt.yhdistelma_tekoaly import YhdistelmaTekoaly


class TestYhdistelmaTekoaly(unittest.TestCase):
    def setUp(self) -> None:
        self.tekoaly = YhdistelmaTekoaly(3, Peli())

    def test_ei_positiivinen_fokus_pituus_aiheuttaa_virheen(self):
        with self.assertRaises(ValueError):
            YhdistelmaTekoaly(-10, Peli())

        with self.assertRaises(ValueError):
            YhdistelmaTekoaly(0, Peli())

    def test_siirtoja_jaljella_alustettu_oikein(self):
        self.assertEqual(self.tekoaly.siirtoja_jaljella, 3)

    def test_pisteet_tyhjia_alussa(self):
        for pari in self.tekoaly.hae_tekoalyt_ja_pisteet():
            self.assertEqual(pari[1], tuple())

    def test_lisaa_pienentaa_jaljella_olevia_siirtoja_yhdella(self):
        self.tekoaly.lisaa("k")

        self.assertEqual(self.tekoaly.siirtoja_jaljella, 2)

    def test_lisaa_vaihtaa_parhaiten_pelanneen_tekoalyn_kun_ei_ole_siirtoja_jaljella(
        self,
    ):
        self.tekoaly.lisaa("k")
        self.tekoaly.lisaa("k")
        self.tekoaly.lisaa("k")

        self.assertEqual(self.tekoaly.pelaava_tekoaly, self.tekoaly.hae_paras_tekoaly())
