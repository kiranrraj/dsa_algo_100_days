# Problem: 91
# Problem: Remove Duplicates from Sorted Linked List
# Author: Kiranraj R.
# Date: 19/01/2026
# DSA Topic: Linked List
# Difficulty Level: Easy
# --------------------------------

# Problem Statement:
# Given the head of a sorted linked list, delete all duplicates such that each
# element appears only once. Return the linked list sorted as well.
# --------------------------------
# Approach:
# 1. Traverse the linked list using a pointer.
# 2. Compare the current node's value with the next node's value.
# 3. If they are the same, skip the next node by adjusting the current node's next pointer.
# 4. If they are different, move the pointer to the next node.
# 5. Repeat steps 2-4 until the end of the list is reached.
# --------------------------------

# Time Complexity:  O(n)
# Space Complexity: O(1)
# --------------------------------


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def remove_duplicates(head):
    current = head
    while current.next != None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head


# Example usage:
node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = remove_duplicates(node1)

# Print result
temp = head
while temp:
    print(temp.value, end=" -> ")
    temp = temp.next
print("None")
