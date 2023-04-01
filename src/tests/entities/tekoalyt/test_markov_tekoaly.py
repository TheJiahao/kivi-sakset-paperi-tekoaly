import unittest

from entities.tekoalyt.markov_tekoaly import MarkovTekoaly


class TestMarkovTekoaly(unittest.TestCase):
    def test_pelaa(self):
        voittavat_vaihtoehdot = {"k": "p", "s": "k", "p": "s"}

        markov1 = MarkovTekoaly(1, voittavat_vaihtoehdot)

        markov1.pelaa("k")

        self.assertEqual(markov1.pelaa("k"), "p")

        markov1.pelaa("s")
        markov1.pelaa("k")
        markov1.pelaa("s")

        self.assertEqual(markov1.pelaa("k"), "k")

        markov3 = MarkovTekoaly(3, voittavat_vaihtoehdot)

        markov3.pelaa("k")
        markov3.pelaa("s")
        markov3.pelaa("p")
        markov3.pelaa("k")
        markov3.pelaa("s")

        self.assertEqual(markov3.pelaa("p"), "p")
