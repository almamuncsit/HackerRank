#!/bin/python3

from collections import defaultdict


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    frequency = defaultdict(int)
    need_delete = 0
    for char in a:
        frequency[char] += 1
    for char in b:
        frequency[char] -= 1
    for count in frequency.values():
        need_delete += abs(count)
    return need_delete


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
