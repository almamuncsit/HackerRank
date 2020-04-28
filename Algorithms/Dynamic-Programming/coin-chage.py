#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    c.sort()
    c.insert(0, 0)
    matrix = [[None for _ in range(n + 1)] for j in range(len(c))]
    matrix[0][0] = 1
    for j in range(1, n + 1):
        matrix[0][j] = 0

    for i in range(1, len(matrix)):
        for j in range(n + 1):
            if c[i] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - c[i]]

    return matrix[-1][-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
