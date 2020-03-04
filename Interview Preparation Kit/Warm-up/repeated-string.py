#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
	if s == 'a':
		return n
	count_a = s.count('a')
	count_a = count_a * (n//len(s))
	count_a += s[:(n%len(s))].count('a')

	return count_a

	# new_s = s * ( (n//len(s))+1 )
	# new_s = new_s[:n]
	# return new_s.count('a')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
