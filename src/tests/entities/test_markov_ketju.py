import unittest
from collections import deque

from entities.markov_ketju import MarkovKetju


class TestMarkovKetju(unittest.TestCase):
    def setUp(self):
        self.ketju = MarkovKetju(3, {"a", "b", "c"})

    def tayta_muisti(self) -> None:
        self.ketju.lisaa("a")
        self.ketju.lisaa("b")
        self.ketju.lisaa("c")

    def laske_jonon_hajautusarvo(self, jono: tuple) -> int:
        tulos = 0

        for jasen in jono:
            tulos *= self.ketju.k
            tulos += self.ketju.vaihtoehdot[jasen]

        return tulos

    def test_markovin_ketjun_luominen_onnistuu(self):
        MarkovKetju(3, {"a", "b", "c"})
        MarkovKetju(5, {"a", "b", "c"})
        MarkovKetju(3, {1, 2})
        MarkovKetju(1, {"a"})
        MarkovKetju(1, {(1,)})

    def test_muisti_on_alussa_tyhja(self):
        self.assertEqual(len(self.ketju.muisti), 0)

    def test_n_alustettu_oikein(self):
        self.assertEqual(self.ketju.n, 3)

    def test_frekvenssit_alustettu_oikein(self):
        for vaihtoehto in self.ketju.vaihtoehdot:
            self.assertEqual(self.ketju.frekvenssit[vaihtoehto], {})

    def test_ketju_on_sama_itsensa_kanssa(self):
        ketju1 = MarkovKetju(2, {1, 2, 3})
        ketju2 = MarkovKetju(2, {1, 2, 3, 4})

        self.assertEqual(ketju1, ketju1)
        self.assertEqual(ketju2, ketju2)

    def test_ketjut_samoilla_parametreilla_ovat_samat(self):
        ketju1 = MarkovKetju(2, {1, 2, 3})
        ketju2 = MarkovKetju(2, {1, 2, 3})

        self.assertEqual(ketju1, ketju1)
        self.assertEqual(ketju1, ketju2)

    def test_ketjut_ovat_samat_samojen_muutoksien_jalkeen(self):
        ketju1 = MarkovKetju(2, {1, 2, 3})
        ketju2 = MarkovKetju(2, {1, 2, 3})

        ketju1.lisaa(1)
        ketju1.lisaa(2)
        ketju1.lisaa(3)

        ketju2.lisaa(1)
        ketju2.lisaa(2)
        ketju2.lisaa(3)

        self.assertEqual(ketju1, ketju2)

    def test_ketjut_eri_parametreilla_ovat_eri(self):
        ketju1 = MarkovKetju(2, {1, 2, 3})
        ketju2 = MarkovKetju(10, {1, 2})
        ketju3 = MarkovKetju(2, {1, 2})

        self.assertNotEqual(ketju1, ketju2)
        self.assertNotEqual(ketju1, ketju3)
        self.assertNotEqual(ketju2, ketju3)

    def test_samat_ketjut_ovat_eri_muutoksien_jalkeen_eri(self):
        ketju1 = MarkovKetju(2, {1, 2, 3})
        ketju2 = MarkovKetju(2, {1, 2, 3})

        ketju1.lisaa(2)
        ketju1.lisaa(2)

        ketju2.lisaa(1)
        ketju2.lisaa(3)

        self.assertNotEqual(ketju1, ketju2)

    def test_ketju_ei_ole_sama_toisen_tyyppisen_olion_kanssa(self):
        self.assertNotEqual(self.ketju, 1)
        self.assertNotEqual(self.ketju, "x")
        self.assertNotEqual(self.ketju, [])

    def test_repr(self):
        self.assertEqual(repr(MarkovKetju(10, {1})), "MarkovKetju(10, {1})")
        self.assertEqual(repr(MarkovKetju(4, {2})), "MarkovKetju(4, {2})")

    def test_frekvenssia_ei_voi_muuttaa_ulkopuolelta(self):
        self.tayta_muisti()
        self.tayta_muisti()
        self.ketju.frekvenssit["a"] = {1: 100}

        self.assertNotEqual(self.ketju.frekvenssit["a"].get(1, 0), 100)

    def test_vaihtoehtoja_ei_voi_muuttaa_ulkopuolelta(self):
        self.ketju.vaihtoehdot["d"] = 2

        self.assertNotIn("d", self.ketju.vaihtoehdot)

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

        self.assertEqual(
            self.ketju.frekvenssit["c"][self.laske_jonon_hajautusarvo(("a", "b", "c"))],
            1,
        )

        self.ketju.lisaa("c")

        self.assertEqual(
            self.ketju.frekvenssit["c"][self.laske_jonon_hajautusarvo(("b", "c", "c"))],
            1,
        )

        self.tayta_muisti()
        self.ketju.lisaa("c")

        self.assertEqual(
            self.ketju.frekvenssit["c"][self.laske_jonon_hajautusarvo(("a", "b", "c"))],
            2,
        )

    def test_muistista_poistetaan_ylimaarainen_alkio_oikein(self):
        self.tayta_muisti()

        self.ketju.lisaa("a")
        self.assertEqual(self.ketju.muisti, deque(["b", "c", "a"]))

        self.ketju.lisaa("b")
        self.assertEqual(self.ketju.muisti, deque(["c", "a", "b"]))

        self.ketju.lisaa("a")
        self.assertEqual(self.ketju.muisti, deque(["a", "b", "a"]))

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
