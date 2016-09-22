from crypto.tools import xor_strings, split
from crypto.games.game_cr import GameCR
from crypto.simulator.cr_sim import CRSim
from crypto.abstract.block_cipher import BlockCipher

"""
Let enc: {0,1}^k x {0,1}^n -> {0,1}^n be a block cipher with k,n = INSTRUCSTOR TODO.
Let the family of functions hash_f: {0,1}^n x {0,1}^2n -> {0,1}^n be defined as
follows:
"""

# Block & key size in bytes. INSTRUCTOR TODO.
block = None
key_len = None

def hash_f(k, m):
    """
    INSTRUCTOR TODO: Fill in.
    """
    return None

"""
Show that hash_f is not collision resistant by presenting a practical adversary
(adversary) such that Adv(cr,H, adversary) = 1. Note that the running time of
the birthday attack is too large for it to be considered practical.
"""


def adversary(key):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param key: This is key used as the seed to the provided hash function
    :return: return 2 messages, m1 and m2, that your adversary believes collide.
    """

    return None

"""

Advantage:

Running time:

"""


if __name__ == '__main__':
    g = GameCR(hash_f, key_len)
    s = CRSim(g, adversary)

    print "\nThe advantage of your adversary is ~" + str(s.compute_advantage())
