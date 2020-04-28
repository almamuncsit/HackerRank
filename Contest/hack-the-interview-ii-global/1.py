#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'maxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER m
#

def maxScore(a, m):
    a.sort()
    products = defaultdict(list)
    for i in range(len(a)):
        key = (i // m) + 1
        products[key].append(a[i])
    last_key = ((len(a) - 1) // m) + 1
    if len(products[last_key]) < m:
        products[last_key - 1].extend(products[last_key])
        del products[last_key]
    score = 0
    c = (10 ** 9) + 7
    for item in products.items():
        score += item[0] * sum(item[1])
    return score % c


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    ans = maxScore(a, m)
    print(ans)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
