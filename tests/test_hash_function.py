import unittest
try:
    from ..crypto.abstract.hash_function import HashFunction
except ValueError:
    from crypto.abstract.hash_function import HashFunction


class TestHashFunction(unittest.TestCase):

    def test_hash(self):
        m = "ABCDEFGH" * 16
        m2 = m + m

        h = HashFunction(128)
        c = h.hash(m)

        c2 = h.hash(m)

        self.assertNotEqual(c, m)
        self.assertEquals(c2, c)

        c3 = h.hash(m2)

        self.assertNotEqual(c2, c3)


if __name__ == '__main__':
    unittest.main()