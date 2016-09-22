from crypto.primitives import random_string_bits
from crypto.tools import xor_strings, split
from crypto.games.game_cca import GameCCA
from crypto.simulator.cca_sim import CCASim
from crypto.abstract.block_cipher import BlockCipher

"""
Let enc: {0,1}^k x {0,1}^n -> {0,1}^n be a block cipher with k,n = INSTRUCTOR TODO.
Let encrypt, decrypt be the following encryption algorithm and decryption
algorithms, respectively:
"""

# Block and key size in bytes. INSTRUCTOR TODO.
block = None
key_len = None

def encrypt(k, input_m):
    """
    INSTRUCTOR TODO: Fill in.
    """
    return None


def decrypt(k, cipher):
    """
    INSTRUCTOR TODO: Fill in.
    """
    return None

"""
Present  a  practical  adversary A.
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
    return (None, None)

"""
State the advantage achieved by your adversary:

"""

if __name__ == '__main__':
    g = GameCCA(encrypt, decrypt, key_len, block)
    s = CCASim(g, adversary)

    print "\nThe advantage of your adversary is ~" + str(s.compute_advantage())
