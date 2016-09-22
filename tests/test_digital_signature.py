import unittest

try:
    from ..crypto.abstract.digital_signature import DigitalSignature
except ValueError:
    from crypto.abstract.digital_signature import DigitalSignature



class TestDigitalSignature(unittest.TestCase):
    def test_sign(self):
        m = "ABCDEFGH" * 16
        k = "A" * 128
        m2 = m + m

        ds = DigitalSignature(128, 128)
        c = ds.sign(k, m)

        c2 = ds.sign(k, m)
        self.assertNotEqual(c, m)
        self.assertEquals(c2, c)

        c3 = ds.sign(k, m2)

        self.assertNotEqual(c2, c3)

    def test_verify(self):
        m = "ABCDEFGH" * 16
        k = "A" * 128

        ds = DigitalSignature(128, 128)

        pk, sk = ds.key_gen()

        c = ds.sign(pk, m)

        self.assertTrue(ds.verify(sk, m, c))
        self.assertFalse(ds.verify(pk, m, c))



if __name__ == '__main__':
    unittest.main()