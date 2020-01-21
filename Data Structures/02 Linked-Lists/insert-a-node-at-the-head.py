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

def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next

def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode( data )
    if llist is None:
        return node
    else:
        node.next = llist
        return node



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head)
    
    # print_singly_linked_list(llist.head, '\n', fptr)
    # fptr.write('\n')
    # fptr.close()