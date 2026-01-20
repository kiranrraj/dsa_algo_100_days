# Problem: 89
# Problem: Reverse Linked List
# Author: Kiranraj R.
# Date: 19/01/2026
# DSA Topic: Linked List
# Difficulty Level: Easy
# --------------------------------
# Problem Statement:
# Given the head of a linked list, reverse the list, and return the reversed list.
# --------------------------------
# Approach:
# 1. Initialize three pointers: prev as None, current as head, and next_node as None.
# 2. Iterate through the linked list. In each iteration:
#    a. Save the next node by setting next_node = current.next.
#    b. Reverse the link by setting current.next = prev.
#    c. Move prev forward by setting
#    prev = current.
#    d. Move current forward by setting current = next_node.
# 3. Once the iteration is complete, prev will be the new head of the reversed list.
# --------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(1)
# --------------------------------


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linkedlist(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # 1. Save next node
        current.next = prev  # 2. Reverse the link
        prev = current  # 3. Move prev forward
        current = next_node  # 4. Move current forward

    return prev  # New head of reversed list
