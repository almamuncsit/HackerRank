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

# Complete the mergeLists function below.

def mergeLists(head1, head2):
    new_list = SinglyLinkedList()
    while head1 and head2:
        if head1.data < head2.data:
            new_list.insert_node(head1.data)
            head1 = head1.next
        else:
            new_list.insert_node(head2.data)
            head2 = head2.next
    if head1:
        new_list.tail.next = head1
    else:
        new_list.tail.next = head2

    return new_list.head


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3)
        # fptr.write('\n')

    # fptr.close()
