How To Create Assignments
*************************
Now that you know how to create a :doc:`blank assignment</quick_start>`, we
are going to walk through filling in an assignment. For this
example we will fill in a CCA assignment template::

    from crypto.primitives import random_string_bits
    from crypto.tools import xor_strings, split
    from crypto.games.game_cca import GameCCA
    from crypto.simulator.cca_sim import CCASim
    from crypto.abstract.block_cipher import BlockCipher
    """
    Let enc: {0,1}^k x {0,1}^n -> {0,1}^n be a block cipher with k,n = INSTRUCTOR TODO.
    Let encrypt, decrypt be the following encryption algorithm and decryption
    algorithms, respectively:
    """
    block = None
    key_len = None

    def encrypt(k, input_m):
        return None
    def decrypt(k, cipher):
        return None

    """
    Present  a  practical  adversary A.
    """
    def adversary(lr, dec):
        return (None, None)

    """
    State the advantage achieved by your adversary:
    """
    if __name__ == '__main__':
        g = GameCCA(encrypt, decrypt, key_len, block)
        s = CCASim(g, adversary)

        print "\nThe advantage of your adversary is ~" + str(s.compute_advantage())

First we have the import block::

    from crypto.primitives import random_string_bits
    from crypto.tools import xor_strings, split
    from crypto.games.game_cca import GameCCA
    from crypto.simulator.cca_sim import CCASim
    from crypto.abstract.block_cipher import BlockCipher

The assignment needs to wire the game to the simulator, so we need to import
the GameCCA class and CCASim class. These imports are required in order to
run the assignment. Next, we have imports for functions that will be useful
when creating and completing the assignment. These functions are described in
:doc:`conventions</conventions>`.

The next section is the portion that defines key length, block size, and
abstract crypto primitives::

    """
    Let enc: {0,1}^k x {0,1}^n -> {0,1}^n be a block cipher with k,n = 128.
    Let encrypt, decrypt be the following encryption algorithm and decryption
    algorithms, respectively:
    """
    n = 128
    block = n/8
    key_len = n/8
    cipher = BlockCipher(block, key_len)
    enc = cipher.encrypt
    enc_i = cipher.decrypt

For the example we set n and k = 128 and then we build the block cipher with
these values.


Now we need to define the encryption and decryption functions. I am going to
skip over the implementation details and explain the easiest way to implement
these functions in general. If you want to see the details, this example was
taken from the ind_cca assignment in the assignments folder. It is much
easier to create these functions by converting pseudo-code into python code.
With the help of the conventions section it is easier to define the scheme in
pseudo-code and then convert it to python.

Finally, to be able to run the assignment, you need to create a game object
and a simulator object::

    if __name__ == '__main__':
        g = GameCCA(encrypt, decrypt, key_len, block)
        s = CCASim(g, adversary)

        print "\nThe advantage of your adversary is ~" + str(s.compute_advantage())

To create a game object you need to call the __init__ function of the game
class. To do this you call GameXX(params). In the current example we call
GameCCA. Once the game object is created call the Simulator __init__
function. Finally, run the simulator by calling the compute_advantage function.


How To Create Games
===================
Each assignment has a set of oracles that should be defined in a Game_xx.py
file. To create a blank game follow the steps to create a blank assignment,
but create the game in the crypto.games directory. Below is a sample game
that extends the game GameLR::

    from crypto.games.game_lr import GameLR

    class demo (GameLR):
        def __init__(self, encrypt, key_len, block_len):
            self.g = GameLR(encrypt,key_len,block_len)
            self.count = 0

        def initialize(self, b):
            self.g.initialize(b)
            self.count=0

        def lr(self, l, r):
            self.count +=1
            return self.g.lr(l, r)

        def finalize(self, guess):
            if self.count >= 3:
                return False
            else:
                return self.g.finalize(guess)

Let's break this up into smaller digestible sizes.

First, this game leverages the game GameLR so it must be imported::

    from crypto.games.game_lr import GameLR

Notice that the class definition takes the GameLR as a parameter. This has to
do with python classes::

   class demo (GameLR):

Next we will walk through each function starting with the __init__ function.

init::

    def __init__(self, encrypt, key_len, block_len):
                self.g = GameLR(encrypt,key_len,block_len)
                self.count = 0

This is the python class constructor. Here we create a GameLR to use to do
most of the work of us. We also add a variable to the demo class to keep
track of the number of queries made to the lr oracle.
initialize::

    def initialize(self, b):
            self.g.initialize(b)
            self.count=0

The initialize function is used to pass parameters at run time. It is
important to reset variables between runs because the class object is not
destroyed at the end of a run.

lr::

    def lr(self, l, r):
            self.count +=1
            return self.g.lr(l, r)

The lr oracle in the demo class only increments the count and then calls
the game object to get a cipher text.

finalize::

    def finalize(self, guess):
            if self.count >= 3:
                return False
            else:
                return self.g.finalize(guess)

Finalize again will delegate most of the work to the game object, but it does
check the count to make sure the Adversary doesn't call the oracle too many
times.

It is important to note that this game will output -1 if the Adversary makes
too many lr oracle calls.

How To Create Simulators
========================
Each assignment has a simulator that should be defined in a xx_sim.py
file. To create a blank simulator file, follow the steps to create a blank
assignment, but create the simulator in the crypto.simulator directory. Below
is a breakdown of the LR simulator that extends the base_sim class::

    from crypto.simulator.base_sim import BaseSim

    class LRSim(BaseSim):

        def run(self, b):
            self.game.initialize(b)
            return self.game.finalize(self.adversary(self.game.lr))

        def compute_success_ratio(self, b):
            results = []
            for i in xrange(0, 1000):
                results += [self.run(b)]

            successes = float(results.count(True))
            failures = float(results.count(False))
            return successes / (successes + failures)

        def compute_advantage(self):
            """
            Adv = Pr[Right => 1] - Pr[Left => 1]
            """
            return self.compute_success_ratio(1) - (1 - self.compute_success_ratio(0))

The BaseSim class is the parent class to all of the simulators and you should
include it in all of your games. If you don't you will need to define the
__init__ method. The __init__ function takes as parameters the game and
adversary you wish to simulate.

Each simulator has three functions: a run function that runs the adversary
against the game, an advantage calculator, and a success calculator. These
functions can be designed in any way you want with the caveat that the
advantage is calculated by running the game. The above example does exactly
that. When the compute_advantage is called, the advantage is calculated by
determining the success ratio in each world::

        def compute_advantage(self):
            """
            Adv = Pr[Right => 1] - Pr[Left => 1]
            """
            return self.compute_success_ratio(1) - (1 - self.compute_success_ratio(0))

The only thing this function does is call the compute_success_ration and
returns an IND-CPA advantage as the success ration in the right world - the
failure ratio in the right world. To see where the game is run we need to
look into the compute_success_ratio function::

        def compute_success_ratio(self, b):
            results = []
            for i in xrange(0, 1000):
                results += [self.run(b)]

            successes = float(results.count(True))
            failures = float(results.count(False))
            return successes / (successes + failures)

This function calls the run function 1000 times and sums up the number of times
that the adversary wins. It then returns the ratio for successes to total
runs. Your simulators can, and in many cases should be designed differently.
This is because games have different definitions of success and failure.

The run function is the real simulator. It initializes the the game every
time it is run. This is extremely important. If you do not reinitialize the
game every run, there is a high probability that you will compute an
incorrect advantage. Here is the run function again::

        def run(self, b):
            self.game.initialize(b)
            return self.game.finalize(self.adversary(self.game.lr))

The run function will then call finalize on the output of the Adversary.
Since this is an lr adversary, it will output a guess for the world and
finalize will return true if the guess is correct.

Defining simulators should be fairly straightforward. The run function can be
nearly identical between simulators (with the exception of parameters), but the
advantage and success ratio functions will change most of the time.
