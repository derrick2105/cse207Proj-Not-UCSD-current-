from crypto.tools import *
from crypto.abstract.block_cipher import BlockCipher

"""
Let enc: {0, 1}^k x {0, 1)^n -> {0, 1)^n be a block cipher with k, n = 128 bits
Let D = { M (= {0, 1}* : 0 < |M| < n * 2^n and |M| mod n = 0}.
Let tag: {0, 1}^k x D -> {0, 1}^n be defined as follows:
"""

# Use n in bytes in code.
n = 128 / 8
enc = BlockCipher(n, n).encrypt

def T(k, m):
    if len(m) < 0 or len(m) * 8 > 128 * (2**128) or len(m) % n != 0:
        return None

    m = split(m, n)
    length_m = len(m)

    m = [None] + m + [int_to_string(length_m, n)]
    c = ["\xFF" * n]

    for i in xrange(1, length_m + 2):
        c += [enc(k, xor_strings(c[i - 1], m[i]))]

    return c[length_m + 1]

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
    asking for.

    :param tag: This is an oracle supplied by GameUFCMA, you can call this
    oracle to get a "tag" for the data you pass into it.
    :param verify: This is an oracle supplied by GameUFCMA, you can call this
    oracle to verify a tag for a specific message.
    """
    pass

from crypto.games.game_ufcma import GameUFCMA
from crypto.simulator.ufcma_sim import UFCMASim

if __name__ == '__main__':
    g = GameUFCMA(T, V, 16)
    s = UFCMASim(g, adversary)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())
