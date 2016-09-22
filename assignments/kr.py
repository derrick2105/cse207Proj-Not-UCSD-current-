from crypto.primitives import AES, AES_I
from crypto.tools import xor_strings, split

"""
The family of functions F: {0, 1}^256 x {0, 1}^256 --> {0, 1}^256 is defined by:
"""


def F(k, x):
    k1, k2 = split(k)
    x1, x2 = split(x)

    y1 = AES(x1, k1)
    y2 = AES(k1, xor_strings(x2, k2))

    return y1 + y2

"""
for all 256-bit strings k, x. Present a practical KR adversary that successfully
attacks F. Say how many input-output examples q and how much time t your attack
takes.
"""


def A(fn):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param fn: This is the oracle supplied by GameKR, you can call this
    oracle to get an "encryption" of the data you pass into it.
    :return: return the a string that represents a key guess.
    """

    return None


from crypto.games.game_kr import GameKR
from crypto.simulator.kr_sim import KRSim

if __name__ == '__main__':
    g = GameKR(F, 32, 32)
    s = KRSim(g, A)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())