# Problem: 84
# Problem: Floyd’s Cycle Detection Algorithm
# Author: Kiranraj R.
# Date: 17/01/2026
# DSA topic: Linked List / Two Pointers
# Difficulty: Medium
# -------------------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(1)
# -------------------------------------------
# Problem Statement:
# Given a linked list, determine if it has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# -------------------------------------------


# Approach:
# 1. Use two pointers, slow and fast.
# 2. Move slow one step at a time and fast two steps at a time.
# 3. If there is a cycle, the fast pointer will eventually meet the slow pointer.
# -------------------------------------------


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head: ListNode) -> bool:
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next  # Move slow by 1 step
        fast = fast.next.next  # Move fast by 2 steps

        if slow == fast:  # Cycle detected
            return True

    return False  # No cycle detected


# Example usage:

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(has_cycle(node1))
