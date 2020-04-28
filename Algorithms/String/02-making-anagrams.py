#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    map_1 = Counter(s1)
    map_2 = Counter(s2)
    common = 0
    for item in map_1.keys():
        if item in map_2:
            common += min(map_1[item], map_2[item])
    return (len(s1) + len(s2)) - (common * 2)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()

    result = makingAnagrams(s1, s2)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
