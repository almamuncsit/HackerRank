#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        # fptr.write(str(node.data))
        print(node.data)
        node = node.next

        # if node:
        #     fptr.write(sep)

# Complete the getNode function below.

def getNode(head, positionFromTail):
    current = head
    result = head
    index = 0
    while current:
        if index > positionFromTail:
            result = result.next
        index += 1
        current = current.next

    return result.data

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
