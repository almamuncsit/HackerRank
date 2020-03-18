#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	swap = -1
	sorted_arr = sorted(arr)
	for i in range(len(arr)):
		if arr[i] != sorted_arr[i]:
			swap += 1

	if swap == -1:
		return 0
	else:
		return swap


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)
    # fptr.write(str(res) + '\n')

    # fptr.close()



int minimumSwaps(vector<int> arr) {
    
    int i,c=0,n=arr.size();
    for(i=0;i<n;i++)
    {
        if(arr[i]==(i+1))
            continue;
        
        swap(arr[i],arr[arr[i]-1]);
        c++;
        i--;
    }
    return c;

}