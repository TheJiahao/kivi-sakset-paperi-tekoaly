import unittest

from entities.tekoalyt.markov_tekoaly import MarkovTekoaly


class TestMarkovTekoaly(unittest.TestCase):
    def setUp(self) -> None:
        self.voittavat_vaihtoehdot = {"k": "p", "s": "k", "p": "s"}

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

    def tayta(self, markov: MarkovTekoaly) -> None:
        markov.lisaa("k")
        markov.lisaa("s")
        markov.lisaa("p")
