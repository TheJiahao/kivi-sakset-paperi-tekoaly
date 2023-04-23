import unittest

from entities.peli import Peli
from entities.tekoalyt.markov_tekoaly import MarkovTekoaly
from entities.tekoalyt.tekoaly import Tekoaly
from entities.tekoalyt.yhdistelma_tekoaly import YhdistelmaTekoaly


class FakeTekoaly(Tekoaly):
    def __init__(self) -> None:
        pass

    def pelaa(self) -> str:
        return "test"

    def lisaa(self, syote: str) -> None:
        pass

    def __repr__(self) -> str:
        return "Tekoaly"


class TestYhdistelmaTekoaly(unittest.TestCase):
    def setUp(self) -> None:
        self.tekoaly = YhdistelmaTekoaly(3, Peli())

    def hae_tekoalyn_pisteet(self, haettava: Tekoaly) -> int:
        for tekoaly, pisteet in self.tekoaly.hae_tekoalyt_ja_pisteet():
            if tekoaly == haettava:
                return pisteet

        return 0

    def pelaa_useampi_kierros(self, tekoaly: YhdistelmaTekoaly, syotteet: str) -> str:
        tuloste = ""

        for syote in syotteet:
            tuloste += tekoaly.pelaa()
            tekoaly.lisaa(syote)

        return tuloste

    def test_ei_positiivinen_fokus_pituus_aiheuttaa_virheen(self):
        with self.assertRaises(ValueError):
            YhdistelmaTekoaly(-10, Peli())

        with self.assertRaises(ValueError):
            YhdistelmaTekoaly(0, Peli())

    def test_siirtoja_jaljella_alustettu_oikein(self):
        self.assertEqual(self.tekoaly.siirtoja_jaljella, 3)

    def test_pisteet_nollia_alussa(self):
        for pari in self.tekoaly.hae_tekoalyt_ja_pisteet():
            self.assertEqual(pari[1], 0)

    def test_repr(self):
        self.assertEqual(
            repr(YhdistelmaTekoaly(5, Peli(), True, [FakeTekoaly()])),
            "YhdistelmaTekoaly(5, True, [Tekoaly])",
        )

    def test_hae_paras_tekoaly_antaa_parhaimman_tekoalyn(self):
        paras = self.tekoaly.hae_paras_tekoaly()
        pisteet = self.hae_tekoalyn_pisteet(paras)
        pistetilanne = map(lambda pari: pari[1], self.tekoaly.hae_tekoalyt_ja_pisteet())

        self.assertEqual(pisteet, max(pistetilanne))

        self.tekoaly.lisaa("k")
        self.tekoaly.lisaa("s")
        self.tekoaly.lisaa("p")

        paras = self.tekoaly.hae_paras_tekoaly()
        pisteet = self.hae_tekoalyn_pisteet(paras)
        pistetilanne = map(lambda pari: pari[1], self.tekoaly.hae_tekoalyt_ja_pisteet())

        self.assertEqual(pisteet, max(pistetilanne))

    def test_lisaa_pienentaa_jaljella_olevia_siirtoja_yhdella(self):
        self.tekoaly.lisaa("k")

        self.assertEqual(self.tekoaly.siirtoja_jaljella, 2)

    def test_lisaa_vaihtaa_parhaiten_pelanneen_tekoalyn_kun_ei_ole_siirtoja_jaljella(
        self,
    ):
        self.tekoaly.lisaa("k")
        self.tekoaly.lisaa("k")
        self.tekoaly.lisaa("k")

        self.assertEqual(
            self.hae_tekoalyn_pisteet(self.tekoaly.pelaava_tekoaly),
            self.hae_tekoalyn_pisteet(self.tekoaly.hae_paras_tekoaly()),
        )

    def test_pelaa_saannollisella_syotteella_kun_vaihto_fokus_pituuden_valein(
        self,
    ):
        # Voittojärjestys: a <- b <- c <- a eli esim. b voittaa a:n.
        peli = Peli({"a": "b", "b": "c", "c": "a"})

        tekoaly1 = YhdistelmaTekoaly(3, peli)
        tekoaly2 = YhdistelmaTekoaly(3, peli)

        self.pelaa_useampi_kierros(tekoaly1, "aaaaaaaaa")
        self.pelaa_useampi_kierros(tekoaly2, "abcabcabc")

        self.assertEqual(self.pelaa_useampi_kierros(tekoaly1, "aaaaaa"), "bbbbbb")
        self.assertEqual(self.pelaa_useampi_kierros(tekoaly2, "abcabc"), "bcabca")

    def test_pelaa_saannollisella_syotteella_kun_vaihto_kierroksittain(self):
        peli = Peli({"a": "b", "b": "c", "c": "a"})

        tekoaly1 = YhdistelmaTekoaly(
            10,
            peli,
            True,
        )
        tekoaly2 = YhdistelmaTekoaly(
            6,
            peli,
            True,
        )

        self.pelaa_useampi_kierros(tekoaly1, "aaaaaaaaaaaaaaaaaaaa")
        self.pelaa_useampi_kierros(tekoaly2, "abcabcabcabcabcabcabc")

        self.assertEqual(self.pelaa_useampi_kierros(tekoaly1, "aaaaa"), "bbbbb")
        self.assertEqual(self.pelaa_useampi_kierros(tekoaly2, "abcabc"), "bcabca")

    def test_pelaa_pidemmalla_syotteella_kun_vaihto_fokus_pituuden_valein(
        self,
    ):
        peli = Peli({"a": "b", "b": "c", "c": "a"})
        tekoaly = YhdistelmaTekoaly(3, peli)

        self.pelaa_useampi_kierros(tekoaly, "abcbabcabcbabbababcaabbabcabbcabbcab")

        self.assertEqual(self.pelaa_useampi_kierros(tekoaly, "cba"), "aba")

    def test_pelaa_pidemmalla_syotteella_kun_vaihto_kierroksittain(self):
        peli = Peli({"a": "b", "b": "c", "c": "a"})
        tekoaly = YhdistelmaTekoaly(
            5,
            peli,
            True,
            [MarkovTekoaly(i, peli.voittavat_siirrot) for i in range(1, 4)],
        )

        self.pelaa_useampi_kierros(
            tekoaly,
            "babbacbabcabbabcabcbabcbabcbabcbabcbabcbabcabbabcbabcbabcbabcabcbacbcbacbacacbacbacbabbabcbabcabcbabcabcbacbbcbcbcabcbabcbbcabcbbabbcacbacabcab",
        )
        self.pelaa_useampi_kierros(tekoaly, "cbabc")

        self.assertEqual(self.pelaa_useampi_kierros(tekoaly, "bab"), "cbc")
