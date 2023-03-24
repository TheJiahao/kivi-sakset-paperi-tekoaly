import unittest
from entities.markovin_ketju import MarkovinKetju, muodosta_osajonot


class TestMarkovKetju(unittest.TestCase):
    def setUp(self):
        pass

    def test_muodosta_osajonot_yhdella_vaihtoehtolla(self):
        self.assertEqual(muodosta_osajonot({1}, 3), {(1, 1, 1)})
        self.assertEqual(muodosta_osajonot({"a"}, 4), {("a", "a", "a", "a")})
        self.assertEqual(muodosta_osajonot({(1,)}, 2), {((1,), (1,))})
        self.assertEqual(muodosta_osajonot({1}, 1), {(1,)})

    def test_muodosta_osajonot_usealla_vaihtoehdolla(self):
        self.assertEqual(muodosta_osajonot({1}, 3), {(1, 1, 1)})
        self.assertEqual(
            muodosta_osajonot({"a", "b"}, 3),
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
            muodosta_osajonot({1, 2, 3}, 2),
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
        self.assertEqual(
            muodosta_osajonot({"a", "b", "c"}, 1), {("a",), ("b",), ("c",)}
        )
