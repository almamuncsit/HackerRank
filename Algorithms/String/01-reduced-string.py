#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superReducedString function below.
def superReducedString(s):
    stack = []
    for c in s:
        if len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if stack:
        return ''.join(stack)
    else:
        return 'Empty String'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = superReducedString(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()
