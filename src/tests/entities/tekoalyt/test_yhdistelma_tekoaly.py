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
        for pistejono in self.tekoaly.pisteet.values():
            self.assertEqual(tuple(pistejono), tuple())

    def test_tekoalyjen_pisteet_nollia_alussa(self):
        for ai in self.tekoaly.hae_tekoalyt():
            self.assertEqual(self.tekoaly.hae_pisteet(ai), 0)

    def test_hae_pisteet_aiheuttaa_virheen_jos_tekoalya_ei_ole(self):
        with self.assertRaises(ValueError):
            self.tekoaly.hae_pisteet(YhdistelmaTekoaly(4))

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
