#!/bin/python3

import math
import os
import random
import re
import sys
import copy

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

"""
def reverse(head):
    if head == None || head.next == None:
        return head

    previous_node = None
    new_head = None

    while head:
        new_head = copy.deepcopy(head)
        new_head.next = previous_node
        previous_node = new_head
        head = head.next

    return new_head
"""

def reverse(head):
    if head == None or head.next == None:
        return head
    
    node = head.next
    head.next = None
    new_head = reverse(node)
    node.next = head

    return new_head



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1)
        # fptr.write('\n')

    # fptr.close()

