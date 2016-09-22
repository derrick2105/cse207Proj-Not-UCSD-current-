from crypto.primitives import AES, AES_I
from crypto.tools import split

"""
The family of functions F: {0, 1}^n x {0, 1}^k --> {0, 1}^n is defined by:
"""

# Block & key size in bytes. INSTRUCTOR TODO.
block = None
key_len = None

def F(k, x):
    """
    INSTRUCTOR TODO: Fill in.INSTRUCTOR TODO: Fill in.
    """
    return None

"""
Show that F is not a secure PRF by presenting a practical adversary A such
that Adv(prf, F, A) is close to one. Fill in the code for adversary A,
verify it's advantage by running your code and describe
the running time.
"""


def A(fn):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param fn: This is the oracle supplied by GamePRF, you can call this
    oracle to get an "encryption" of the data you pass into it.
    :return: return 1 to indicate your adversary believes it is the real world
    and return 0 to indicate that your adversary believes it is in the random
    world.
    """
    return None

from crypto.games.game_prf import GamePRF
from crypto.simulator.world_sim import WorldSim

if __name__ == '__main__':
    g = GamePRF(F, key_len, block)
    s = WorldSim(g, A)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())