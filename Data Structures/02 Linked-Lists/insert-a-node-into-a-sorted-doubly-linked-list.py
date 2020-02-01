#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node):
    while node:
        # fptr.write(str(node.data))
        print(node.data)
        node = node.next

        # if node:
        #     fptr.write(sep)

# Complete the sortedInsert function below.

def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if head is None:
        return new_node

    if head.data >= data:
        head.prev = new_node
        new_node.next = head
        return new_node
        
    current_node = head
    while current_node.next:
        current_node = current_node.next
        if current_node.data >= data:
            current_node.prev.next = new_node
            new_node.next = current_node
            current_node.prev = new_node
            return head

    current_node.next = new_node
    new_node.prev = current_node
    return head


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1)
    #     fptr.write('\n')

    # fptr.close()
