#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    h = 'hackerrank'
    j = 0
    if len(h) > len(s):
        return 'NO'
    for i in range(len(s)):
        if s[i] == h[j]:
            j += 1
            if j == len(h)-1:
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
