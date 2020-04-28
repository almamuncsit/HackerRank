#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum1, sum2 = 0, 0
    for i in range(len(arr)):
        sum1 += arr[i][i]
    i = 0
    j = len(arr)-1
    while i < len(arr):
        sum2 += arr[i][j]
        i += 1
        j -= 1
    return abs(sum1 - sum2)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

# fptr.write(str(result) + '\n')

# fptr.close()
