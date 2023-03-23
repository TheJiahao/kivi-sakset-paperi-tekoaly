import unittest
from entities.markovin_ketju import MarkovinKetju, muodosta_osajonot


class TestMarkovKetju(unittest.TestCase):
    def setUp(self):
        pass

    def test_muodosta_osajonot(self):
        vaihtoehdot1 = {"a", "b"}
        vaihtoehdot2 = {"a", "b", "c"}
        vaihtoehdot3 = {"a"}

        self.assertEqual(
            muodosta_osajonot(vaihtoehdot1, vaihtoehdot1, 3),
            {"aaa", "aab", "aba", "baa", "abb", "bab", "bba", "bbb"},
        )
        self.assertEqual(
            muodosta_osajonot(vaihtoehdot2, vaihtoehdot2, 2),
            {"aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"},
        )
        self.assertEqual(
            muodosta_osajonot(vaihtoehdot3, vaihtoehdot3, 4),
            {"aaaa"},
        )
