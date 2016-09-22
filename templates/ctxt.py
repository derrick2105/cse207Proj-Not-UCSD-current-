from crypto.primitives import AES, AES_I, random_string
from crypto.tools import xor_strings, split, join

"""
Let E denote AES. Let K be the key generation algorithm that returns a
random 128-bit AES key K and let SE = (K, encrypt, decrypt) be the
symmetric encryption scheme whose encryption and decryption algorithms are
as follows:
"""

block_size = None
key_len = None

def encrypt(k, m):
    """
    INSTRUCTOR TODO: Fill in.
    return cipher text and tag tuple
    """
    cipher_text = None
    tag = None

    return cipher_text, tag

def decrypt(k, (ce, t)):
    """
    INSTRUCTOR TODO: Fill in.
    Return message if valid, None otherwise.
    """

    return None


"""
Give an INT-CTXT adversary that shows that this sceme is not secure:
"""

def adversary(enc, dec):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for. You must call dec on a valid candidate to win the game.

    :param enc: This is an oracle supplied by GameINTCTXT, you can call this
    oracle to get an encryption of the data you pass into it.
    :param dec: This is an oracle supplied by GameINTCTXT, you can call this
    oracle to get a decryption of the data you pass into it.
    """
    pass



from crypto.games.game_int_ctxt import GameINTCTXT
from crypto.simulator.ctxt_sim import CTXTSim

if __name__ == '__main__':
    g = GameINTCTXT(encrypt, decrypt, key_len)
    s = CTXTSim(g, adversary)

    print "\nThe advantage of your adversary is ~" + str(s.compute_advantage())
