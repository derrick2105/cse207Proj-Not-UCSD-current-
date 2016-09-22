from crypto.tools import *
from crypto.abstract.block_cipher import BlockCipher

"""
Let enc: {0, 1}^k x {0, 1)^n -> {0, 1)^n be a block cipher with k, n = INSTRUCTOR TODO
Let D = { M (= {0, 1}* : 0 < |M| < n * 2^n and |M| mod n = 0}.
Let tag: {0, 1}^k x D -> {0, 1}^n be defined as follows:
"""

# key length in bytes INSTRUCTOR TODO
key_len = None

def T(k, m):
    """
    INSTRUCTOR TODO: Fill in.
    """
    return None

def V(k, m, t):
    if T(k, m) == t:
        return 1
    else:
        return 0

"""
Show that T is an insecure MAC by presenting a practical adversary (adversary)
such that Adv(adversary) = 1.

Oracle queries: 2
Running time: constant

"""

def adversary(tag, verify):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for. You must make a valid call to verify in order to win.

    :param tag: This is an oracle supplied by GameUFCMA, you can call this
    oracle to get a "tag" for the data you pass into it.
    :param verify: This is an oracle supplied by GameUFCMA, you can call this
    oracle to verify a tag for a specific message.
    """
    pass

from crypto.games.game_ufcma import GameUFCMA
from crypto.simulator.ufcma_sim import UFCMASim

if __name__ == '__main__':
    g = GameUFCMA(T, V, key_len)
    s = UFCMASim(g, adversary)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())
