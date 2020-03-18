#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for i in range(0, 4):
        for j in range(0, 4):
            sum = arr[j][i] + arr[j][i+1] + arr[j][i+2]
            sum += arr[j+1][i+1]
            sum += arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]
            sums.append(sum)
    sums = sorted(sums)

    return sums[-1]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
