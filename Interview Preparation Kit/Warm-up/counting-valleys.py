#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	valleys = 0
	current_position = 0
	for c in s:
		if c == 'D':
			if current_position == 0:
				valleys += 1
				current_position -= 1
			else:
				current_position -= 1
		else:
			current_position += 1

	return valleys


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
