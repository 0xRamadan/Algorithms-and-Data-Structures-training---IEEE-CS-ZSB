
#
#       CS21-Science-Day-05
#       name: Mahmoud Abdallah 
#       task: cycle detection
#       link: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
#

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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    # idea to create two pointers, make the logic and finially check if the two pointers are the same
    # note that head is a pointer
    pointer2 = pointer1 = head
    
    # make sure that the linkedlist is not empty or having a single node (in that case there will not be a cylce to detect)
    
    while pointer1 != None and pointer1.next != None:
        # set pointers
        pointer1 = pointer1.next.next 
        pointer2 = pointer2.next
        
        # check if the two pointers are same 
        if pointer1 == pointer2:
            return True
    return False
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)
        
        print(str(int(result)))

        fptr.write(str(int(result)) + '\n')

    fptr.close()