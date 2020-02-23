#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	items = {}
	pair = 0
	for x in ar:
		if x in items:
			items[x] += 1
		else:
			items[x] = 1
	
	for key, val in items.items():
		pair += (val // 2)

	return pair

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()
