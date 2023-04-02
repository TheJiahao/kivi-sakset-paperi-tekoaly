import unittest
from copy import deepcopy

from entities.tekoalyt.markov_tekoaly import MarkovTekoaly


class TestMarkovTekoaly(unittest.TestCase):
    def setUp(self) -> None:
        self.voittavat_vaihtoehdot = {"k": "p", "s": "k", "p": "s"}
        self.markov = MarkovTekoaly(3, self.voittavat_vaihtoehdot)

    def tayta(self, markov: MarkovTekoaly) -> None:
        markov.lisaa("k")
        markov.lisaa("s")
        markov.lisaa("p")

    def test_tekoalyt_samoilla_parametreilla_ovat_samat(self):
        markov1 = MarkovTekoaly(2, {"a": "b", "x": "y"})
        markov2 = MarkovTekoaly(2, {"a": "b", "x": "y"})

        self.assertEqual(markov1, markov2)

    def test_tekoalyt_samojen_syotteiden_jalkeen_samat(self):
        markov1 = MarkovTekoaly(2, {"a": "b", "x": "y"})
        markov2 = MarkovTekoaly(2, {"a": "b", "x": "y"})

        markov1.lisaa("a")
        markov1.lisaa("x")

        markov2.lisaa("a")
        markov2.lisaa("x")

        self.assertEqual(markov1, markov2)

    def test_tekoalyt_eri_parametreilla_eri(self):
        markov1 = MarkovTekoaly(2, {"a": "b", "x": "y"})
        markov2 = MarkovTekoaly(2, {"a": "c", "x": "y"})
        markov3 = MarkovTekoaly(4, {"a": "b"})
        markov4 = MarkovTekoaly(3, {"a": "b"})

        self.assertNotEqual(markov1, markov2)
        self.assertNotEqual(markov2, markov3)
        self.assertNotEqual(markov3, markov4)

    def test_tekoalyt_eri_syotteiden_jalkeen_eri(self):
        markov1 = MarkovTekoaly(2, {"a": "b", "x": "y"})
        markov2 = MarkovTekoaly(2, {"a": "b", "x": "y"})

        markov1.lisaa("x")
        markov1.lisaa("a")

        self.assertNotEqual(markov1, markov2)

    def test_samoilla_tekoalyilla_on_samat_hajautusarvot(self):
        markov1 = MarkovTekoaly(2, {"a": "b", "x": "y"})
        markov2 = MarkovTekoaly(2, {"a": "b", "x": "y"})

        self.assertEqual(hash(markov1), hash(markov2))

    def test_pelaa_lyhyella_ketjulla(self):
        markov = MarkovTekoaly(1, self.voittavat_vaihtoehdot)

        markov.lisaa("k")
        markov.lisaa("k")

        self.assertEqual(markov.pelaa(), "p")

        markov.lisaa("s")
        markov.lisaa("k")
        markov.lisaa("s")
        markov.lisaa("k")

        self.assertEqual(markov.pelaa(), "k")

    def test_pelaa_pidemmalla_ketjulla(self):
        markov = MarkovTekoaly(3, self.voittavat_vaihtoehdot)

        self.tayta(markov)
        self.tayta(markov)

        self.assertEqual(markov.pelaa(), "p")

        markov.lisaa("p")
        self.tayta(markov)
        markov.lisaa("p")
        self.tayta(markov)

        self.assertEqual(markov.pelaa(), "s")

    def test_pelaa_ei_aiheuta_muutosta(self):
        markov1 = MarkovTekoaly(2, {"a": "b", "x": "y"})
        markov2 = MarkovTekoaly(2, {"a": "b", "x": "y"})

        markov1.pelaa()

        self.assertEqual(markov1, markov2)

    def test_markovin_ketjua_ei_voi_muuttaa_ulkopuolelta(self):
        ketju = deepcopy(self.markov.markovin_ketju)

        self.markov.markovin_ketju.lisaa("k")

        self.assertEqual(self.markov.markovin_ketju, ketju)

    def test_voittavia_siirtoja_ei_voi_muuttaa_ulkopuolelta(self):
        self.markov.voittavat_siirrot["d"] = "e"

        self.assertEqual(self.markov.voittavat_siirrot, {"k": "p", "s": "k", "p": "s"})

    def test_lisaa_ei_muuta_hajautusarvoa(self):
        hajautusarvo_alussa = hash(self.markov)

        self.markov.lisaa("k")

        self.assertEqual(hash(self.markov), hajautusarvo_alussa)

        self.markov.lisaa("p")

        self.assertEqual(hash(self.markov), hajautusarvo_alussa)
