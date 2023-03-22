import unittest
from entities.peli import Peli


class TestPeli(unittest.TestCase):
    def setUp(self) -> None:
        self.peli = Peli()

    def test_voittotapaukset_oikein(self):
        self.assertEqual(self.peli.paata_voittaja("k", "s"), 1)
        self.assertEqual(self.peli.paata_voittaja("s", "p"), 1)
        self.assertEqual(self.peli.paata_voittaja("p", "k"), 1)

    def test_tasapelit_oikein(self):
        self.assertEqual(self.peli.paata_voittaja("k", "k"), 0)
        self.assertEqual(self.peli.paata_voittaja("s", "s"), 0)
        self.assertEqual(self.peli.paata_voittaja("p", "p"), 0)

    def test_haviot_oikein(self):
        self.assertEqual(self.peli.paata_voittaja("k", "p"), -1)
        self.assertEqual(self.peli.paata_voittaja("s", "k"), -1)
        self.assertEqual(self.peli.paata_voittaja("p", "s"), -1)

    def test_virheellinen_merkki(self):
        with self.assertRaises(ValueError):
            self.peli.paata_voittaja("a", "p")
            self.peli.paata_voittaja("a", "b")
            self.peli.paata_voittaja("k", "b")
