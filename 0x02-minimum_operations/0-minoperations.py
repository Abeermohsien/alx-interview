#!/usr/bin/python3
"""monoperation  Module"""


def minOperations(n):
    """get fewest operationss
    """
    # output should be 2 chars
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n can be divided by root
        if n % root == 0:
            # even divisiom = operations
            ops += root
            # n become remainder
            n = n / root
            # mince the root to find the smallest even divisions n
            root -= 1
        root += 1
    return ops
