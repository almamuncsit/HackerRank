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

def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    node = head
    for x in range(position-1):
        node = node.next

    new_node.next = node.next
    node.next = new_node

    return head


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head)

    # fptr.write('\n')
    # fptr.close()
