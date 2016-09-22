import unittest
try:
    from ..crypto.abstract.message_authentication_code import MAC
except ValueError:
    from crypto.abstract.message_authentication_code import MAC


class TestMAC(unittest.TestCase):
    def test_tag(self):
       m = "ABCDEFGH" * 16
       k = "A" * 128
       m2 = m + m

       mac = MAC(128, 128)
       c = mac.tag(k, m)

       c2 = mac.tag(k, m)
       self.assertNotEqual(c, m)
       self.assertEquals(c2, c)

       c3 = mac.tag(k, m2)

       self.assertNotEqual(c2, c3)

    def test_verify(self):
        m = "ABCDEFGH" * 16
        k = "A" * 128

        mac = MAC(128, 128)

        c = mac.tag(k, m)

        self.assertTrue(mac.verify(k, m, c))

if __name__ == '__main__':
    unittest.main()