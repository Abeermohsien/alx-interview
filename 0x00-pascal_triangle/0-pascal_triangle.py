#!/usr/bin/python3
"""
pascal function"""


def pascal_triangle(n):
    """make pascal triangle function that gives a list of lists of interger"""
    result = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            result.append(level)
    return result
