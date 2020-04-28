#!/bin/python3

import math
import os
import random
import re
import sys


def connectedFriends(student, graph):
    queue = []
    visited = set()
    for friend in graph[student]:
        if friend not in [1, 2]:
            visited.add(friend)
            queue.append(friend)
    while queue:
        item = queue.pop()
        for friend in graph[item]:
            if friend not in [1, 2] and friend not in visited:
                visited.add(friend)
    return visited


def configureProjectPresentation(n, friendships):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for friendship in friendships:
        graph[friendship[0]].append(friendship[1])
        graph[friendship[1]].append(friendship[0])

    two_friends = connectedFriends(2, graph)
    one_friends = connectedFriends(1, graph)
    team = list(one_friends - two_friends)
    team.sort()
    return team if team else [-1]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        freiendships = []

        for _ in range(m):
            freiendships.append(list(map(int, input().rstrip().split())))

        result = configureProjectPresentation(n, freiendships)
        print(result)
        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')
        # fptr.close()
