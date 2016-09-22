from crypto.tools import xor_strings, split
from crypto.games.game_cr import GameCR 
from crypto.simulator.cr_sim import CRSim
from crypto.abstract.block_cipher import BlockCipher

"""
Let enc: {0,1}^k x {0,1}^n -> {0,1}^n be a block cipher with k,n = 128.
Let the family of functions hash_f: {0,1}^n x {0,1}^2n -> {0,1}^n be defined as
follows:
"""

n = 128
block = n/8
cipher = BlockCipher(block, block) 
enc = cipher.encrypt
enc_i = cipher.decrypt


"""
Show that hash_f is not collision resistant by presenting a practical adversary
(adversary) such that Adv(cr,H, adversary) = 1. Note that the running time of
the birthday attack is too large for it to be considered practical.
"""

def hash_f(k, m):
    if len(m) != 2 * block:
        return None
    l, m = k, split(m)

    for i in range(2):
        x = enc(l, m[i])
        l = xor_strings(x, m[i])
    return x


def adversary(key):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param key: This is key used as the seed to the provided hash function
    :return: return 2 messages, m1 and m2, that your adversary believes collide.
    """
    return None, None

"""

Advantage: 1

Running time: constant

"""


if __name__ == '__main__':
    g = GameCR(hash_f, 16)
    s = CRSim(g, adversary)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())
