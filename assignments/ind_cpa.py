import random

from crypto.primitives import AES, AES_I, random_string
from crypto.tools import xor_strings, add_int_to_string

"""
Let key K be a random 128-bit string. Let encrypt be the following encryption
algorithm, based on the block cipher AES.
"""
block_size = 16


def encrypt(k, x):
    r = random_string(block_size)
    c = r
    for i in range(1, len(x) / block_size + 1, 1):
        w_i = add_int_to_string(r, i, block_size * 8)
        x_i = x[((i - 1) * block_size): (i * block_size)]
        c += AES(k, xor_strings(x_i, w_i))
    return c

"""
Specify a decryption algorithm decrypt such that  SE =(K,E,D) is a symmetric
encryption scheme
"""


def decrypt(k, c):
    """
    You must fill in this method. This is the decryption algorithm that the
    problem is asking for.

    :param k: The key used to encrypt/decrypt the message
    :param c: The cipher text to be decrypted
    :return: return the decryption on the cipher text c
    """

    return None

"""
Show that this scheme is insecure by presenting a practical adversary such
that the Adv(ind-cpa, SE, A) is high.
"""


def adversary(lr):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param lr: This is the oracle supplied by GameLR, you can call this
    oracle to get an encryption of the data you pass into it.
    :return: return 1 to indicate your adversary believes it is the left world
    and return 0 to indicate that your adversary believes it is in the right
    world.
    """

    return None

"""
State the probability achieved by your adversary and the number of oracle calls
it makes.

probability:

queries:
"""

from crypto.games.game_lr import GameLR
from crypto.simulator.lr_sim import LRSim

if __name__ == '__main__':
    g = GameLR(encrypt, 16, 16)
    s = LRSim(g, adversary)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())

    key = random_string(block_size)

    for j in range(100):
        blocks = random.randrange(100)
        message = random_string(blocks*16)
        cypher = encrypt(key, message)
        bad = False
        if message != decrypt(key, cypher):
            bad = True
    if bad:
        print "Your Decryption function is incorrect"
    else:
        print "Your Decryption function is correct"
