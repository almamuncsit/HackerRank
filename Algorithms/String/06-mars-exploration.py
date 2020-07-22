#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
	sos = 'SOS'
	count = 0
	for x in range(len(s)):
		if s[x] != sos[x%3]:
			count += 1
	return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = marsExploration(s)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
