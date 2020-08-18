#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
	magazine_count = {}
	note_count = {}
	
	for word in magazine:
		magazine_count[word] = magazine_count.get(word, 0) + 1
	
	for word in note:
		note_count[word] = note_count.get(word, 0) + 1
	
	for note, count in note_count.items():
		if note not in magazine_count or magazine_count[note] < count:
			return 'No'

	return 'Yes'


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    result = checkMagazine(magazine, note)
    print(result)
