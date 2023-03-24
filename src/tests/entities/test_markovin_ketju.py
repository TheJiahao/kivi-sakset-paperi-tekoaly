import unittest
from collections import deque

from entities.markovin_ketju import MarkovinKetju, muodosta_jonot


class TestMarkovKetju(unittest.TestCase):
    def setUp(self):
        self.markov = MarkovinKetju(3, {"a", "b", "c"})

    def tayta_muisti(self):
        self.markov.lisaa("a")
        self.markov.lisaa("b")
        self.markov.lisaa("c")

    def test_muodosta_jonot_yhdella_vaihtoehtolla(self):
        self.assertEqual(muodosta_jonot({1}, 3), {(1, 1, 1)})
        self.assertEqual(muodosta_jonot({"a"}, 4), {("a", "a", "a", "a")})
        self.assertEqual(muodosta_jonot({(1,)}, 2), {((1,), (1,))})
        self.assertEqual(muodosta_jonot({1}, 1), {(1,)})

    def test_muodosta_jonot_usealla_vaihtoehdolla(self):
        self.assertEqual(muodosta_jonot({1}, 3), {(1, 1, 1)})
        self.assertEqual(
            muodosta_jonot({"a", "b"}, 3),
            {
                ("a", "a", "a"),
                ("a", "a", "b"),
                ("a", "b", "a"),
                ("b", "a", "a"),
                ("a", "b", "b"),
                ("b", "a", "b"),
                ("b", "b", "a"),
                ("b", "b", "b"),
            },
        )
        self.assertEqual(
            muodosta_jonot({1, 2, 3}, 2),
            {
                (1, 1),
                (1, 2),
                (1, 3),
                (2, 1),
                (2, 2),
                (2, 3),
                (3, 1),
                (3, 2),
                (3, 3),
            },
        )
        self.assertEqual(muodosta_jonot({"a", "b", "c"}, 1), {("a",), ("b",), ("c",)})

    def test_markovin_ketjun_luominen_onnistuu(self):
        MarkovinKetju(3, {"a", "b", "c"})
        MarkovinKetju(5, {"a", "b", "c"})
        MarkovinKetju(3, {1, 2})
        MarkovinKetju(1, {"a"})
        MarkovinKetju(1, {(1,)})

    def test_muisti_on_alussa_tyhja(self):
        self.assertEqual(self.markov.muisti, tuple())

    def test_alustettu_vaihtoehdot_oikein(self):
        self.assertEqual(self.markov.vaihtoehdot, {"a", "b", "c"})

    def test_alustettu_n_oikein(self):
        self.assertEqual(self.markov.n, 3)

    def test_siirtymamatriisi_alustettu_oikein(self):
        jonot = muodosta_jonot({"a", "b", "c"}, 3)

        for vaihtoehto in self.markov.vaihtoehdot:
            for jono in jonot:
                self.assertEqual(self.markov.siirtymamatriisi[vaihtoehto][jono], 0)

    def test_havainnot_tyhjia_alussa(self):
        self.assertEqual(self.markov.havainnot, {})

    def test_frekvenssit_nollia_alussa(self):
        for vaihtoehto in self.markov.vaihtoehdot:
            for frekvenssi in self.markov.frekvenssit[vaihtoehto].values():
                self.assertEqual(frekvenssi, 0)

    def test_lisaa_aiheuttaa_virheen_kun_syote_ei_kelpaa(self):
        with self.assertRaises(ValueError):
            self.markov.lisaa("x")

        with self.assertRaises(ValueError):
            self.markov.lisaa(1)

        with self.assertRaises(ValueError):
            self.markov.lisaa((2,))

    def test_lisaa_kasvattaa_havaintoja_kun_muisti_on_taynna(self):
        self.tayta_muisti()

        self.markov.lisaa("c")
        self.assertEqual(self.markov.havainnot[("a", "b", "c")], 1)

        self.markov.lisaa("c")
        self.assertEqual(self.markov.havainnot[("b", "c", "c")], 1)

    def test_lisaa_ei_muuta_frekvensseja_kun_muisti_ei_ole_taynna(self):
        self.markov.lisaa("c")
        self.assertEqual(set(self.markov.frekvenssit["c"].values()), {0})

        self.markov.lisaa("b")
        self.assertEqual(set(self.markov.frekvenssit["b"].values()), {0})

        self.markov.lisaa("a")
        self.assertEqual(set(self.markov.frekvenssit["a"].values()), {0})

    def test_lisaa_kasvattaa_frekvensseja_kun_muisti_on_taynna(self):
        self.tayta_muisti()

        self.markov.lisaa("c")
        self.assertEqual(self.markov.frekvenssit["c"][("a", "b", "c")], 1)

        self.markov.lisaa("c")
        self.assertEqual(self.markov.frekvenssit["c"][("b", "c", "c")], 1)

        self.tayta_muisti()
        self.markov.lisaa("c")
        self.assertEqual(self.markov.frekvenssit["c"][("a", "b", "c")], 2)

    def test_lisaa_ei_muuta_havaintoja_kun_muisti_ei_ole_taynna(self):
        self.markov.lisaa("c")
        self.assertEqual(self.markov.havainnot, {})

        self.markov.lisaa("b")
        self.assertEqual(self.markov.havainnot, {})

        self.markov.lisaa("a")
        self.assertEqual(self.markov.havainnot, {})

    def test_lisaa_ei_muuta_siirtymamatriisia_kun_muisti_ei_ole_taynna(self):
        self.markov.lisaa("c")
        for vaihtoehto in self.markov.vaihtoehdot:
            self.assertEqual(
                set(self.markov.siirtymamatriisi[vaihtoehto].values()), {0}
            )

        self.markov.lisaa("b")
        for vaihtoehto in self.markov.vaihtoehdot:
            self.assertEqual(
                set(self.markov.siirtymamatriisi[vaihtoehto].values()), {0}
            )

        self.markov.lisaa("a")
        for vaihtoehto in self.markov.vaihtoehdot:
            self.assertEqual(
                set(self.markov.siirtymamatriisi[vaihtoehto].values()), {0}
            )

    def test_muistista_poistetaan_ylimaarainen_alkio_oikein(self):
        self.tayta_muisti()

        self.markov.lisaa("a")
        self.assertEqual(self.markov.muisti, ("b", "c", "a"))

        self.markov.lisaa("b")
        self.assertEqual(self.markov.muisti, ("c", "a", "b"))

        self.markov.lisaa("a")
        self.assertEqual(self.markov.muisti, ("a", "b", "a"))

    def test_lisaa_paivittaa_todennakoisyyden_oikein(self):
        self.tayta_muisti()
        self.markov.lisaa("a")

        todennakoisyys = self.markov.siirtymamatriisi["a"][("a", "b", "c")]
        self.assertAlmostEqual(todennakoisyys, 1)

        self.markov.lisaa("a")
        todennakoisyys = self.markov.siirtymamatriisi["a"][("b", "c", "a")]
        self.assertAlmostEqual(todennakoisyys, 1)

        self.tayta_muisti()
        self.markov.lisaa("b")

        a_todennakoisyys = self.markov.siirtymamatriisi["b"][("a", "b", "c")]
        b_todennakoisyys = self.markov.siirtymamatriisi["a"][("a", "b", "c")]
        c_todennakoisyys = self.markov.siirtymamatriisi["c"][("a", "b", "c")]

        self.assertAlmostEqual(a_todennakoisyys, 1 / 2)
        self.assertAlmostEqual(b_todennakoisyys, 1 / 2)
        self.assertAlmostEqual(c_todennakoisyys, 0)

    def test_ennusta_valitsee_todennakoisimman_vaihtoehdon_kun_muisti_on_taynna(self):
        self.tayta_muisti()
        self.markov.lisaa("a")

        # a:n todennäköisyys on 1 eli todennäköisin
        self.assertEqual(self.markov.ennusta(), "a")

        # Muisti on nyt (b, c, a)
        self.tayta_muisti()
        # Nyt (a, b, c) jonon jälkeen havaittiin b, frekvenssi 1
        self.markov.lisaa("b")
        self.tayta_muisti()
        # Nyt (a, b, c) jonon jälkeen havaittiin b, frekvenssi 2
        self.markov.lisaa("b")

        # Nyt b:n todennäköisyys on 2/3 eli todennäköisin
        self.assertEqual(self.markov.ennusta(), "b")
