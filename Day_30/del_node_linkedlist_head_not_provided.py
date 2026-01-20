# Problem: 94
# Problem: Delete a node in a singly linked list, given only access to that node
# Author: Kiranraj R.
# Date: 20/01/2026
# DSA Topic: Linked List
# Difficulty Level: Easy
# --------------------------------

# Problem Statement:
# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted directly (not the head of the list).
# It is guaranteed that the node to be deleted is not a tail node in the list.
# --------------------------------

# Approach:
# 1. Copy the next node's value into this node.
# 2. Remove the next node by adjusting the next pointer of the current node.
# --------------------------------

# Time Complexity:  O(1)
# Space Complexity: O(1)
# --------------------------------


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def delete_node(node):
    # Copy the next node's value into this node
    node.value = node.next.value
    # Remove next node, as we cannot move backward to find the
    # node before the one we want to delete.
    node.next = node.next.next


# Example usage:
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Delete node3 (value = 3)
delete_node(node3)

# Print list starting from head
temp = node1
while temp:
    print(temp.value, end=" -> ")
    temp = temp.next
print("None")
