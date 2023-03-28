import unittest

from entities.markovin_ketju import MarkovinKetju


class TestMarkovKetju(unittest.TestCase):
    def setUp(self):
        self.markov = MarkovinKetju(3, {"a", "b", "c"})

    def tayta_muisti(self):
        self.markov.lisaa("a")
        self.markov.lisaa("b")
        self.markov.lisaa("c")

    def test_markovin_ketjun_luominen_onnistuu(self):
        MarkovinKetju(3, {"a", "b", "c"})
        MarkovinKetju(5, {"a", "b", "c"})
        MarkovinKetju(3, {1, 2})
        MarkovinKetju(1, {"a"})
        MarkovinKetju(1, {(1,)})

    def test_muisti_on_alussa_tyhja(self):
        self.assertEqual(self.markov.muisti, tuple())

    def test_vaihtoehdot_alustettu_oikein(self):
        self.assertEqual(self.markov.vaihtoehdot, {"a", "b", "c"})

    def test_n_alustettu_oikein(self):
        self.assertEqual(self.markov.n, 3)

    def test_frekvenssit_alustettu_oikein(self):
        for vaihtoehto in self.markov.vaihtoehdot:
            self.assertEqual(self.markov.frekvenssit[vaihtoehto], {})

    def test_frekvenssia_ei_voi_muuttaa_ulkopuolelta(self):
        self.tayta_muisti()
        self.tayta_muisti()
        self.markov.frekvenssit["a"][("a", "b", "c")] = 10

        self.assertEqual(self.markov.frekvenssit["a"][("a", "b", "c")], 1)

    def test_vaihtoehtoja_ei_voi_muuttaa_ulkopuolelta(self):
        self.markov.vaihtoehdot.add("d")

        self.assertEqual(self.markov.vaihtoehdot, {"a", "b", "c"})

    def test_lisaa_aiheuttaa_virheen_kun_syote_ei_kelpaa(self):
        with self.assertRaises(ValueError):
            self.markov.lisaa("x")

        with self.assertRaises(ValueError):
            self.markov.lisaa(1)

        with self.assertRaises(ValueError):
            self.markov.lisaa((2,))

    def test_lisaa_ei_muuta_frekvensseja_kun_muisti_ei_ole_taynna(self):
        self.markov.lisaa("c")
        self.assertEqual(self.markov.frekvenssit["c"], {})

        self.markov.lisaa("b")
        self.assertEqual(self.markov.frekvenssit["b"], {})

        self.markov.lisaa("a")
        self.assertEqual(self.markov.frekvenssit["a"], {})

    def test_lisaa_kasvattaa_frekvensseja_kun_muisti_on_taynna(self):
        self.tayta_muisti()

        self.markov.lisaa("c")
        self.assertEqual(self.markov.frekvenssit["c"][("a", "b", "c")], 1)

        self.markov.lisaa("c")
        self.assertEqual(self.markov.frekvenssit["c"][("b", "c", "c")], 1)

        self.tayta_muisti()
        self.markov.lisaa("c")
        self.assertEqual(self.markov.frekvenssit["c"][("a", "b", "c")], 2)

    def test_muistista_poistetaan_ylimaarainen_alkio_oikein(self):
        self.tayta_muisti()

        self.markov.lisaa("a")
        self.assertEqual(self.markov.muisti, ("b", "c", "a"))

        self.markov.lisaa("b")
        self.assertEqual(self.markov.muisti, ("c", "a", "b"))

        self.markov.lisaa("a")
        self.assertEqual(self.markov.muisti, ("a", "b", "a"))

    def test_todennakoisyydet_paivittyvat_oikein(self):
        self.tayta_muisti()
        self.markov.lisaa("a")
        self.tayta_muisti()

        self.assertAlmostEqual(self.markov.hae_todennakoisyydet()["a"], 1)
        self.assertAlmostEqual(self.markov.hae_todennakoisyydet()["b"], 0)
        self.assertAlmostEqual(self.markov.hae_todennakoisyydet()["c"], 0)

        self.markov.lisaa("b")
        self.tayta_muisti()

        self.assertAlmostEqual(self.markov.hae_todennakoisyydet()["a"], 0.5)
        self.assertAlmostEqual(self.markov.hae_todennakoisyydet()["b"], 0.5)
        self.assertAlmostEqual(self.markov.hae_todennakoisyydet()["c"], 0)

        self.markov.lisaa("c")
        self.tayta_muisti()

        self.assertAlmostEqual(self.markov.hae_todennakoisyydet()["a"], 0.33, places=2)
        self.assertAlmostEqual(self.markov.hae_todennakoisyydet()["b"], 0.33, places=2)
        self.assertAlmostEqual(self.markov.hae_todennakoisyydet()["c"], 0.33, places=2)

    def test_ennusta_valitsee_todennakoisimman_vaihtoehdon_kun_muisti_on_taynna(self):
        self.tayta_muisti()
        self.markov.lisaa("a")
        self.tayta_muisti()

        # a:n todennäköisyys on 1 eli todennäköisin
        self.assertEqual(self.markov.ennusta(), "a")

        self.tayta_muisti()
        self.markov.lisaa("b")
        self.tayta_muisti()
        self.markov.lisaa("b")
        self.tayta_muisti()
        self.markov.lisaa("b")
        self.tayta_muisti()

        # Nyt b:n todennäköisyys on 3/5 eli todennäköisin
        self.assertEqual(self.markov.ennusta(), "b")

    def test_hae_frekvenssi_aiheuttaa_virheen_kun_syote_ei_kelpaa(self):
        with self.assertRaises(ValueError):
            self.markov.hae_frekvenssi("x")

        with self.assertRaises(ValueError):
            self.markov.hae_frekvenssi(1)

        with self.assertRaises(ValueError):
            self.markov.hae_frekvenssi((2,))

    def test_hae_frekvenssi_palauttaa_nolla_kun_muisti_ei_ole_taynna(self):
        self.markov.lisaa("a")
        self.assertEqual(self.markov.hae_frekvenssi("a"), 0)
        self.assertEqual(self.markov.hae_frekvenssi("b"), 0)
        self.assertEqual(self.markov.hae_frekvenssi("c"), 0)

        self.markov.lisaa("c")
        self.assertEqual(self.markov.hae_frekvenssi("a"), 0)
        self.assertEqual(self.markov.hae_frekvenssi("b"), 0)
        self.assertEqual(self.markov.hae_frekvenssi("c"), 0)

        self.markov.lisaa("b")
        self.assertEqual(self.markov.hae_frekvenssi("a"), 0)
        self.assertEqual(self.markov.hae_frekvenssi("b"), 0)
        self.assertEqual(self.markov.hae_frekvenssi("c"), 0)

    def test_hae_todennakoisyys_on_symmetrinen_kun_muisti_ei_ole_taynna(self):
        self.markov.lisaa("a")
        self.assertAlmostEqual(self.markov.hae_todennakoisyys("a"), 1 / 3, places=2)
        self.assertAlmostEqual(self.markov.hae_todennakoisyys("b"), 1 / 3, places=2)
        self.assertAlmostEqual(self.markov.hae_todennakoisyys("c"), 1 / 3, places=2)

        self.markov.lisaa("c")
        self.assertAlmostEqual(self.markov.hae_todennakoisyys("a"), 1 / 3, places=2)
        self.assertAlmostEqual(self.markov.hae_todennakoisyys("b"), 1 / 3, places=2)
        self.assertAlmostEqual(self.markov.hae_todennakoisyys("c"), 1 / 3, places=2)

        self.markov.lisaa("b")
        self.assertAlmostEqual(self.markov.hae_todennakoisyys("a"), 1 / 3, places=2)
        self.assertAlmostEqual(self.markov.hae_todennakoisyys("b"), 1 / 3, places=2)
        self.assertAlmostEqual(self.markov.hae_todennakoisyys("c"), 1 / 3, places=2)
