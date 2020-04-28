#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    memo = {'n': 0, 'l': 0, 'u': 0, 's': 0}

    for i in range(n):
        if password[i] in numbers:
            memo['n'] = 1
        elif password[i] in lower_case:
            memo['l'] = 1
        elif password[i] in upper_case:
            memo['u'] = 1
        else:
            memo['s'] = 1

    required_char = 0
    for item in memo.values():
        if item == 0:
            required_char += 1

    return max(6 - n, required_char)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)
    print(answer)
    # fptr.write(str(answer) + '\n')
    # fptr.close()
