# Problem: 90
# Problem: Find Middle of Linked List
# Author: Kiranraj R.
# Date: 19/01/2026
# DSA Topic: Linked List
# Difficulty Level: Easy
# --------------------------------
# Problem Statement:
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# --------------------------------
# Approach:
# 1. Use two pointers, slow and fast. Initialize both to the head of the list.
# 2. Move slow one step at a time and fast two steps at a time.
# 3. When fast reaches the end of the list, slow will be at the middle node.
# 4. Return the value of the middle node.

# --------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(1)
# --------------------------------


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next  # move 1 step
        fast = fast.next.next  # move 2 steps

    return slow


# Example usage:
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

middle = find_middle(node1)
print(middle.value)
