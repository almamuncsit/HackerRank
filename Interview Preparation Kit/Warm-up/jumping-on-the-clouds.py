#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	current_index = 0
	jumps = 0
	while current_index < len(c)-1:
		if current_index <= len(c)-3 and c[current_index+2] == 0:
			current_index = current_index+2
			jumps += 1
		elif c[current_index+1] == 0:
			current_index = current_index+1
			jumps += 1
		else:
			return jumps

	return jumps



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
