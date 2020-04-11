#!/bin/python3

from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_count = Counter(a)
    b_count = Counter(b)
    need_delete = 0

    for char, count in a_count.items():
        if char in b_count:
            if b_count[char] == count:
                b_count[char] = 0
                a_count[char] = 0
            else:
                need_delete += abs(a_count[char] - b_count[char])
                b_count[char] = 0
                a_count[char] = 0
        else:
            need_delete += count

    for char, count in b_count.items():
        if count > 0:
            need_delete += count

    return need_delete


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
