#!/bin/python3

import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    lastAnswer = 0
    ansArr = []
    printData = []
    for _ in range(n):
        ansArr.append([])

    for x in queries:
        if x[0] == 1:
            seq = (x[1] ^ lastAnswer) % n
            ansArr[seq].append(x[2])
        else:
            seq = (x[1] ^ lastAnswer) % n
            lastAnswer = ansArr[ seq ][ x[2]%len(ansArr[seq]) ]
            printData.append(lastAnswer)

    return printData

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
