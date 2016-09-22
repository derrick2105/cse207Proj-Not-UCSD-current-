from crypto.primitives import AES, AES_I
from crypto.tools import xor_strings, split

"""
The family of functions F: {0, 1}^n x {0, 1}^n --> {0, 1}^n is defined by:
"""

# Block & key size in bytes. INSTRUCTOR TODO.
block = None
key_len = None

def F(k, x):
    """
    INSTRUCTOR TODO: Fill in.
    """

    return None

"""
for all n-bit strings k, x. Present a practical KR adversary that successfully
attacks F. Say how many input-output examples q and how much time t your attack
takes.
"""


def A(fn):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param fn: This is the oracle supplied by GameKR, you can call this
    oracle to get an "encryption" of the data you pass into it.
    :return: return 1 to indicate your adversary believes it is the real world
    and return 0 to indicate that your adversary believes it is in the random
    world.
    """
    return None


from crypto.games.game_kr import GameKR
from crypto.simulator.kr_sim import KRSim

if __name__ == '__main__':
    g = GameKR(F, key_len, block)
    s = KRSim(g, A)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())