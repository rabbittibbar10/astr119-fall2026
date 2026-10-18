#------------------------------------------------------------------------------
# This module defines multitab() a multiplication table generator.
#------------------------------------------------------------------------------
import math

def multitab(n):
    """Print multiplication table up to n.

    Parameters
    ----------
    n : positive integer scalar

    Returns
    -------
    None
    """
    assert (type(n) is int) and (n > 0), "n must be positive integer"

    for i in range(1,n+1):
        row = []
        for j in range(1,n+1):
            row.append(i * j)
        print(row)

### To run as a utility
if __name__ == '__main__':
    n = int(input("Multiplication table size: "))
    multitab(n)
