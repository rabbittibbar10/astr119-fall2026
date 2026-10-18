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


    #find width of largest number N*N and add 1 for spacing
    width = len(str(n*n))+1

    for i in range(1,n+1):
        row = []
        for j in range(1,n+1):
            #print the product alligned nicely (< means left alligned)
            print(f"{i * j:<{width}}", end="")
        print()

### To run as a utility
if __name__ == '__main__':
    n = int(input("Multiplication table size: "))
    multitab(n)
