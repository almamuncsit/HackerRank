#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'getMaxCharCount' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#

def getMaxCharCount(s, queries):
    answer = []
    for query in queries:
        sub_str = s[query[0]:query[1] + 1]
        sub_str = sub_str.lower()
        str_count = Counter(sub_str)
        max_key = sub_str[0]
        for letter in str_count.keys():
            if letter > max_key:
                max_key = letter
        answer.append(str_count[max_key])
    return answer


# def getMaxCharCount(s, queries):
#     answer = []
#     for query in queries:
#         sub_str = s[query[0]:query[1] + 1]
#         sub_str = sub_str.lower()
#         sub_str = list(sub_str)
#         sub_str.sort()
#         answer.append(sub_str.count(sub_str[-1]))
#     return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    q = int(input().strip())

    query = []

    for _ in range(q):
        query.append(list(map(int, input().rstrip().split())))

    ans = getMaxCharCount(s, query)
    print(ans)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')
    # fptr.close()
