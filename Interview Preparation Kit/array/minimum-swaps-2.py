#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	swap = 0
	i = 0
	while i < len(arr):
		if arr[i] == (i+1):
			i += 1
		else:
			swap += 1
			pos = arr[i] -1
			arr[i], arr[pos] = arr[pos], arr[i]

	return swap


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)
    # fptr.write(str(res) + '\n')

    # fptr.close()
