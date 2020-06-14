Creating minimal perfect hash functions
---------------------------------------

Generate a minimal perfect hash function for a given set of keys.
A given code template is filled with parameters, such that the
output is code which implements the hash function.
Templates can easily be constructed for any programming language.


### Installation

The minimal perfect hash function generator is written in pure Python,
and can be installed using:

    $ pip install perfect-hash

The code supports Python 2.7 and Python 3.5 or higher.
However, some of the examples do not support Python 2 anymore.


### Acknowledgments

Part of the code is based on an a program A.M. Kuchling wrote:
http://www.amk.ca/python/code/perfect-hash

The algorithm the program uses is described in the paper
'Optimal algorithms for minimal perfect hashing',
Z. J. Czech, G. Havas and B.S. Majewski.
http://cmph.sourceforge.net/papers/chm92.pdf
