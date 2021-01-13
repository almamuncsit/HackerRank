#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    new_set = set(map(lambda x: x.lower(), list(s)))
    return 'pangram' if len(new_set) == 27 else 'not pangram'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = pangrams(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()
