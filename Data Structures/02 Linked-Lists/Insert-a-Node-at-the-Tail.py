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

def print_singly_linked_list(node):
    while node:
        # fptr.write(str(node.data))
        print(node.data)

        node = node.next

        # if node:
            # fptr.write(sep)
            # print(sep)


def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
    else:
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = SinglyLinkedListNode(data)
    return head
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)
    # print_singly_linked_list(llist.head, '\n', fptr)
    # fptr.write('\n')

    # fptr.close()
