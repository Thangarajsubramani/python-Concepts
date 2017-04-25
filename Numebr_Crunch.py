import numpy as np

def f1(num):
    total = 0.0
    for i in range(num): 
        for j in range(1, num):
            total += (float(i) / j)
    return total

def f2(num):
    i = np.arange(num, dtype=np.float)
    j = np.arange(1, num, dtype=np.float)
    return np.divide.outer(i, j).sum()

def f3(num):
    """Less memory-hungry (and faster) version of f2."""
    total = 0.0
    j = np.arange(1, num, dtype=np.float)
    for i in xrange(num):
        total += (i / j).sum()
    return total
