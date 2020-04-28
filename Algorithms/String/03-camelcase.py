#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the camelcase function below.
def camelcase(s):
    if not s:
        return 0
    word = 1
    for c in s:
        if 'A' <= c <= 'Z':
            word += 1
    return word

# Complete the camelcase function below.
# def camelcase(s):
#     if not s:
#         return 0
#     word = 1
#     for c in s:
#         c.isupper()
#         if c.isupper():
#             word += 1
#     return word


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
