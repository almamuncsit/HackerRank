#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
	bribes = 0
	for i in range(len(q)-1, -1, -1):
		num = i+1
		if q[i] == num:
			pass
		elif i > 0 and q[i-1] == num:
			bribes += 1
			q[i-1], q[i] = q[i], q[i-1]
		elif i > 1 and q[i-2] == num:
			bribes += 2
			q[i-2], q[i-1] = q[i-1], q[i-2]
			q[i], q[i-1] = q[i-1], q[i]
		else:
			bribes = -1
			break
	
	if bribes == -1:
		return 'Too chaotic'
	else:
		return bribes


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
