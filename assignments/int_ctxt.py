from crypto.primitives import AES, AES_I, random_string
from crypto.tools import xor_strings, split, join

"""
Let E denote AES. Let K be the key generation algorithm that returns a
random 128-but AES key K and let SE = (K, encrypt, decrypt) be the
symmetric encryption scheme whose encryption and decryption algorithms are
as follows:
"""

block_size = 64

def encrypt(k, m):
    if len(m) != block_size:
        return None

    m = [None] + split(m, block_size/4)
    ce = [random_string(16)]
    cm = ["\x00" * 16]

    for i in range(1, 5):
        ce += [AES(k, xor_strings(ce[i-1], m[i]))]
        cm += [AES(k, xor_strings(cm[i-1], m[i]))]

    return join(ce), cm[4]

def decrypt(k, (ce, t)):
    if len(ce) != block_size + 16:
        return None

    ce = split(ce, block_size/4)
    cm = ["\x00" * 16]
    m = [None]

    for i in range(1, 5):
        m += [xor_strings(AES_I(k, ce[i]), ce[i - 1])]
        cm += [AES(k, xor_strings(cm[i - 1], m[i]))]

    if cm[4] != t:
        return None
    else:
        return join(m[1:])


"""
Give an INT-CTXT adversary that shows that this sceme is not secure:
"""

def adversary(enc, dec):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param enc: This is an oracle supplied by GameINTCTXT, you can call this
    oracle to get an encryption of the data you pass into it.
    :param dec: This is an oracle supplied by GameINTCTXT, you can call this
    oracle to get a decryption of the data you pass into it.
    """
    pass



from crypto.games.game_int_ctxt import GameINTCTXT
from crypto.simulator.ctxt_sim import CTXTSim

if __name__ == '__main__':
    g = GameINTCTXT(encrypt, decrypt, 16)
    s = CTXTSim(g, adversary)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())
