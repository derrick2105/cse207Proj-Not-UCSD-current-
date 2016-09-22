import unittest

try:
    from ..crypto.abstract.block_cipher import BlockCipher
except ValueError:
    from crypto.abstract.block_cipher import BlockCipher


class TestBlockCipher(unittest.TestCase):
    def test_encrypt(self):
        m = "ABCDEFGH" * 16
        k = "A" * 128

        b = BlockCipher(128, 128)
        c = b.encrypt(k, m)

        self.assertNotEqual(c, m)

        self.assertEquals(m, b.decrypt(k, c))


    def test_decrypt(self):
        c = "ABCDEFGH" * 16
        k = "A" * 128

        b = BlockCipher(128, 128)
        m = b.decrypt(k, c)

        self.assertNotEqual(m, c)

        self.assertEquals(c, b.encrypt(k, m))

if __name__ == '__main__':
    unittest.main()