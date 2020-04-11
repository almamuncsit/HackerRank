from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for i in range(len(word)):
            index = word[i]
            if i == len(word) - 1 and index in root.children:
                return False
            if index not in root.children:
                root.children[index] = TrieNode()
            root = root.children.get(index)
            if root.terminating:
                return False
        root.terminating = True
        return True


if __name__ == "__main__":
    n = int(input())
    ok = True
    t = Trie()
    bad_string = None
    for _ in range(n):
        string = input()
        if not ok:
            continue
        ok = t.insert(string)
        if not ok:
            bad_string = string
    if ok:
        print('GOOD SET')
    elif bad_string:
        print('BAD SET')
        print(bad_string)
