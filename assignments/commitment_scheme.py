import math

from crypto.primitives import *
from crypto.tools import *
from crypto.abstract.hash_function import HashFunction

"""
Let K be a RSA generator with associated security parameter k = 1024. Let
CS = (p, c, v) be the commitment scheme whose constituent algorithms are as
follows:
"""

h = None

def p():
    key = rsa_keygen(128)
    global h
    _h = HashFunction(long(math.log(key['n'], 2) / 8)).hash
    h = lambda x: string_to_int(_h(x))
    return key['n']

def c(n, m):
    k = random.randrange(n)
    _c = (k * h(m)) % n
    return _c, k

def v(n, _c, m, k):
    if k > n or k < 0 or _c > n or _c < 0:
        return 0

    if _c == (k * h(m)) % n:
        return 1
    else:
        return 0


"""
Give a BIND adversary that shows that this scheme is not binding:
"""

def adversary(pi):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param pi: This is the public parameter returned by GameBIND initialization.
    :return: return (c,m0,m1,k1,k2) where c is the target commitment, m0 and
    m1 are messages, and k0 and k1 are keys.
    """

    return None, None, None, None, None


from crypto.games.game_bind import GameBIND
from crypto.simulator.bind_sim import BINDSim

if __name__ == '__main__':
    g = GameBIND(p, v)
    s = BINDSim(g, adversary)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())
