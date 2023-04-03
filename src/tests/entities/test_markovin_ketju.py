import unittest

from entities.markovin_ketju import MarkovinKetju


class TestMarkovKetju(unittest.TestCase):
    def setUp(self):
        self.ketju = MarkovinKetju(3, {"a", "b", "c"})

    def tayta_muisti(self):
        self.ketju.lisaa("a")
        self.ketju.lisaa("b")
        self.ketju.lisaa("c")

    def test_markovin_ketjun_luominen_onnistuu(self):
        MarkovinKetju(3, {"a", "b", "c"})
        MarkovinKetju(5, {"a", "b", "c"})
        MarkovinKetju(3, {1, 2})
        MarkovinKetju(1, {"a"})
        MarkovinKetju(1, {(1,)})

    def test_muisti_on_alussa_tyhja(self):
        self.assertEqual(self.ketju.muisti, tuple())

    def test_vaihtoehdot_alustettu_oikein(self):
        self.assertEqual(self.ketju.vaihtoehdot, {"a", "b", "c"})

    def test_n_alustettu_oikein(self):
        self.assertEqual(self.ketju.n, 3)

    def test_frekvenssit_alustettu_oikein(self):
        for vaihtoehto in self.ketju.vaihtoehdot:
            self.assertEqual(self.ketju.frekvenssit[vaihtoehto], {})

    def test_ketju_on_sama_itsensa_kanssa(self):
        ketju1 = MarkovinKetju(2, {1, 2, 3}, {1: {(1, 2): 1}})
        ketju2 = MarkovinKetju(2, {1, 2, 3, 4})

        self.assertEqual(ketju1, ketju1)
        self.assertEqual(ketju2, ketju2)

    def test_ketjut_samoilla_parametreilla_ovat_samat(self):
        ketju1 = MarkovinKetju(2, {1, 2, 3}, {1: {(1, 2): 1}})
        ketju2 = MarkovinKetju(2, {1, 2, 3}, {1: {(1, 2): 1}})

        self.assertEqual(ketju1, ketju1)
        self.assertEqual(ketju1, ketju2)

    def test_ketjut_ovat_samat_samojen_muutoksien_jalkeen(self):
        ketju1 = MarkovinKetju(2, {1, 2, 3})
        ketju2 = MarkovinKetju(2, {1, 2, 3})

        ketju1.lisaa(1)
        ketju1.lisaa(2)
        ketju1.lisaa(3)

        ketju2.lisaa(1)
        ketju2.lisaa(2)
        ketju2.lisaa(3)

        self.assertEqual(ketju1, ketju2)

    def test_ketjut_eri_parametreilla_ovat_eri(self):
        ketju1 = MarkovinKetju(2, {1, 2, 3})
        ketju2 = MarkovinKetju(10, {1, 2})
        ketju3 = MarkovinKetju(2, {1, 2})
        ketju4 = MarkovinKetju(2, {1, 2}, {1: {(2, 1): 20}})

        self.assertNotEqual(ketju1, ketju2)
        self.assertNotEqual(ketju2, ketju3)
        self.assertNotEqual(ketju3, ketju4)

    def test_samat_ketjut_ovat_eri_muutoksien_jalkeen_eri(self):
        ketju1 = MarkovinKetju(2, {1, 2, 3})
        ketju2 = MarkovinKetju(2, {1, 2, 3})

        ketju1.lisaa(2)
        ketju1.lisaa(2)

        ketju2.lisaa(1)
        ketju2.lisaa(3)

        self.assertNotEqual(ketju1, ketju2)

    def test_samoilla_ketjuilla_on_samat_hajautusarvot(self):
        ketju1 = MarkovinKetju(2, {2, 4, 6})
        ketju2 = MarkovinKetju(2, {2, 4, 6})

        self.assertEqual(ketju1, ketju2)

    def test_frekvenssia_ei_voi_muuttaa_ulkopuolelta(self):
        self.tayta_muisti()
        self.tayta_muisti()
        self.ketju.frekvenssit["a"][("a", "b", "c")] = 10

        self.assertEqual(self.ketju.frekvenssit["a"][("a", "b", "c")], 1)

    def test_vaihtoehtoja_ei_voi_muuttaa_ulkopuolelta(self):
        self.ketju.vaihtoehdot.add("d")

        self.assertEqual(self.ketju.vaihtoehdot, {"a", "b", "c"})

    def test_lisaa_aiheuttaa_virheen_kun_syote_ei_kelpaa(self):
        with self.assertRaises(ValueError):
            self.ketju.lisaa("x")

        with self.assertRaises(ValueError):
            self.ketju.lisaa(1)

        with self.assertRaises(ValueError):
            self.ketju.lisaa((2,))

    def test_lisaa_ei_muuta_frekvensseja_kun_muisti_ei_ole_taynna(self):
        self.ketju.lisaa("c")
        self.assertEqual(self.ketju.frekvenssit["c"], {})

        self.ketju.lisaa("b")
        self.assertEqual(self.ketju.frekvenssit["b"], {})

        self.ketju.lisaa("a")
        self.assertEqual(self.ketju.frekvenssit["a"], {})

    def test_lisaa_kasvattaa_frekvensseja_kun_muisti_on_taynna(self):
        self.tayta_muisti()

        self.ketju.lisaa("c")
        self.assertEqual(self.ketju.frekvenssit["c"][("a", "b", "c")], 1)

        self.ketju.lisaa("c")
        self.assertEqual(self.ketju.frekvenssit["c"][("b", "c", "c")], 1)

        self.tayta_muisti()
        self.ketju.lisaa("c")
        self.assertEqual(self.ketju.frekvenssit["c"][("a", "b", "c")], 2)

    def test_muistista_poistetaan_ylimaarainen_alkio_oikein(self):
        self.tayta_muisti()

        self.ketju.lisaa("a")
        self.assertEqual(self.ketju.muisti, ("b", "c", "a"))

        self.ketju.lisaa("b")
        self.assertEqual(self.ketju.muisti, ("c", "a", "b"))

        self.ketju.lisaa("a")
        self.assertEqual(self.ketju.muisti, ("a", "b", "a"))

    def test_todennakoisyydet_paivittyvat_oikein(self):
        self.tayta_muisti()
        self.ketju.lisaa("a")
        self.tayta_muisti()

        self.assertAlmostEqual(self.ketju.hae_todennakoisyydet()["a"], 1)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyydet()["b"], 0)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyydet()["c"], 0)

        self.ketju.lisaa("b")
        self.tayta_muisti()

        self.assertAlmostEqual(self.ketju.hae_todennakoisyydet()["a"], 0.5)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyydet()["b"], 0.5)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyydet()["c"], 0)

        self.ketju.lisaa("c")
        self.tayta_muisti()

        self.assertAlmostEqual(self.ketju.hae_todennakoisyydet()["a"], 0.33, places=2)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyydet()["b"], 0.33, places=2)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyydet()["c"], 0.33, places=2)

    def test_ennusta_valitsee_todennakoisimman_vaihtoehdon_kun_muisti_on_taynna(self):
        self.tayta_muisti()
        self.ketju.lisaa("a")
        self.tayta_muisti()

        # a:n todennäköisyys on 1 eli todennäköisin
        self.assertEqual(self.ketju.ennusta(), "a")

        self.tayta_muisti()
        self.ketju.lisaa("b")
        self.tayta_muisti()
        self.ketju.lisaa("b")
        self.tayta_muisti()
        self.ketju.lisaa("b")
        self.tayta_muisti()

        # Nyt b:n todennäköisyys on 3/5 eli todennäköisin
        self.assertEqual(self.ketju.ennusta(), "b")

    def test_hae_frekvenssi_aiheuttaa_virheen_kun_syote_ei_kelpaa(self):
        with self.assertRaises(ValueError):
            self.ketju.hae_frekvenssi("x")

        with self.assertRaises(ValueError):
            self.ketju.hae_frekvenssi(1)

        with self.assertRaises(ValueError):
            self.ketju.hae_frekvenssi((2,))

    def test_hae_frekvenssi_palauttaa_nolla_kun_muisti_ei_ole_taynna(self):
        self.ketju.lisaa("a")
        self.assertEqual(self.ketju.hae_frekvenssi("a"), 0)
        self.assertEqual(self.ketju.hae_frekvenssi("b"), 0)
        self.assertEqual(self.ketju.hae_frekvenssi("c"), 0)

        self.ketju.lisaa("c")
        self.assertEqual(self.ketju.hae_frekvenssi("a"), 0)
        self.assertEqual(self.ketju.hae_frekvenssi("b"), 0)
        self.assertEqual(self.ketju.hae_frekvenssi("c"), 0)

        self.ketju.lisaa("b")
        self.assertEqual(self.ketju.hae_frekvenssi("a"), 0)
        self.assertEqual(self.ketju.hae_frekvenssi("b"), 0)
        self.assertEqual(self.ketju.hae_frekvenssi("c"), 0)

    def test_hae_todennakoisyys_on_symmetrinen_kun_muisti_ei_ole_taynna(self):
        self.ketju.lisaa("a")
        self.assertAlmostEqual(self.ketju.hae_todennakoisyys("a"), 1 / 3, places=2)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyys("b"), 1 / 3, places=2)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyys("c"), 1 / 3, places=2)

        self.ketju.lisaa("c")
        self.assertAlmostEqual(self.ketju.hae_todennakoisyys("a"), 1 / 3, places=2)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyys("b"), 1 / 3, places=2)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyys("c"), 1 / 3, places=2)

        self.ketju.lisaa("b")
        self.assertAlmostEqual(self.ketju.hae_todennakoisyys("a"), 1 / 3, places=2)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyys("b"), 1 / 3, places=2)
        self.assertAlmostEqual(self.ketju.hae_todennakoisyys("c"), 1 / 3, places=2)
