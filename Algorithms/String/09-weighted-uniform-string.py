#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    memo = {}
    ans = []
    for i in range(len(s)):
        if i == 0 or s[i-1] != s[i]:
            weight = ord(s[i])-96
        else:
            weight += ord(s[i])-96
        memo[weight] = 1
    for query in queries:
        if query in memo:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)
    print(result)
    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    # fptr.close()