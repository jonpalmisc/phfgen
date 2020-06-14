# Set PYTHONHASHSEED when running this program, e.g.:
# $ export PYTHONHASHSEED=0
# $ python generate.py

import sys
import random
import string

sys.path.append('..')
from perfect_hash import generate_code, run_code


class PythonHash(object):
    """
    Random hash function generator.
    """
    chars = string.ascii_letters + string.digits

    def __init__(self, NG):
        self.NG = NG
        self.salt = ''.join(random.choice(self.chars) for _ in range(10))

    def __call__(self, key):
        return hash(self.salt + key) % self.NG

    template = """
def perfect_hash(key):
    return (G[hash("$S1" + key) % $NG] +
            G[hash("$S2" + key) % $NG]) % $NG
"""


keys = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()

code = generate_code(keys, PythonHash)
print(code)
run_code(code)
