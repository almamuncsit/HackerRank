#!/bin/python3

import os
import sys
from heapq import heapify, heappop, heappush


#
# Complete the cookies function below.
#
def cookies(k, A):
    if len(A) < 1:
        return -1
    heapify(A)
    operation = 0
    x = heappop(A)
    while x < k and len(A) >= 1:
        y = heappop(A)
        heappush(A, (x + 2 * y))
        operation += 1
        x = heappop(A)
    if x < k:
        return -1

    return operation


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
