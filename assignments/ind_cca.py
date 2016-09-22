from crypto.primitives import random_string_bits
from crypto.tools import xor_strings, split
from crypto.games.game_cca import GameCCA
from crypto.simulator.cca_sim import CCASim
from crypto.abstract.block_cipher import BlockCipher

"""
Let enc: {0,1}^k x {0,1}^n -> {0,1}^n be a block cipher with k,n = 128.
Let encrypt, decrypt be the following encryption algorithm and decryption
algorithms, respectively:
"""
n = 128
block = n/8
cipher = BlockCipher(block, block)
enc = cipher.encrypt
enc_i = cipher.decrypt

def encrypt(k, input_m):
    if len(input_m) != 2*block:
        return None
    m = ['', '']
    m[0], m[1] = split(input_m)
    r = random_string_bits(n)
    c = enc(k, r)
    for j in range(2):
        r = enc(k, xor_strings(r, m[j]))
        c += enc(k, r)
    return c


def decrypt(k, cipher):
    if len(cipher) != 3*block:
        return None
    r, cipher = enc_i(k, cipher[:block]), cipher[block:]
    c, m = ['', ''], ''
    c[0], c[1] = split(cipher)
    for j in range(2):
        r_j = enc_i(k, c[j])
        m, r = m + xor_strings(enc_i(k, r_j), r), r_j
    return m

"""
Present  a  practical  adversary A making one LR query and one Dec query and
achieving dv(ind-cca, SE, A) = 1
"""


def adversary(lr, dec):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param lr: This is an oracle supplied by GameCCA, you can call this
    oracle to get an encryption of the data you pass into it.
    :param dec: This is an oracle supplied by GameCCA, you can call this
    oracle to get decrypt data.
    :return: return 1 to indicate your adversary believes it is the left world
    and return 0 to indicate that your adversary believes it is in the right
    world.
    """
    return None

"""
State the advantage achieved by your adversary: 1

"""


if __name__ == '__main__':
    g = GameCCA(encrypt, decrypt, block, block)
    s = CCASim(g, adversary)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())

