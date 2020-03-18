#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for q in queries:
        arr[q[0]-1] += q[2]
        if( (q[1])<=len(arr) ): 
            arr[q[1]] -= q[2]

    max = x = 0
    for i in arr:
       x=x+i;
       if(max<x): max=x;

    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
