#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    s_list = list(map(ord, s))
    k = k % 26
    for i in range(len(s_list)):
        if 65 <= s_list[i] <= 90:
            s_list[i] = 65 + ((s_list[i] - 65) + k) % 26
        elif 97 <= s_list[i] <= 122:
            s_list[i] = 97 + ((s_list[i] - 97) + k) % 26
    s_list = map(chr, s_list)    
    return ''.join(s_list)
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
