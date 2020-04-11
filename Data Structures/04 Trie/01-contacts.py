#!/bin/python3

import os
import sys
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False
        self.counter = 1


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # Insert word into trie
    def insert(self, word):
        root = self.root
        for index in word:
            if index not in root.children:
                root.children[index] = TrieNode()
            else:
                root.children[index].counter += 1
            root = root.children.get(index)
        root.terminating = True

    # Search a word in the trie
    def search(self, word):
        root = self.root
        if not root: return 0
        for index in word:
            root = root.children.get(index)
            if not root:
                return 0
        return root.counter


#
# Complete the contacts function below.
#
def contacts(queries):
    trie = Trie()
    results = []
    for query in queries:
        if query[0] == 'add':
            trie.insert(query[1])
        elif query[0] == 'find':
            results.append(trie.search(query[1]))
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
