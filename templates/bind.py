import math

from crypto.primitives import *
from crypto.tools import *

"""
Let CS = (p, c, v) be the commitment scheme whose constituent algorithms are as
follows:
"""

h = None

def p():
    """
    INSTRUCTOR TODO: Fill in.
    This function should return the public parameter.
    """
    return None

def c(n, m):
    """
    INSTRUCTOR TODO: Fill in.
    This function should return a (c, k) tuple as defined for commitment schemes.
    """
    k = None
    _c = None
    return _c, k

def v(n, _c, m, k):
    """
    INSTRUCTOR TODO: Fill in.
    This function should return 1 for a valid commitment and 0 otherwise.
    """

    return None


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
    return (None, None, None, None, None)


from crypto.games.game_bind import GameBIND
from crypto.simulator.bind_sim import BINDSim

if __name__ == '__main__':
    g = GameBIND(p, v)
    s = BINDSim(g, adversary)

    print "\nThe advantage of your adversary is ~" + str(s.compute_advantage())
