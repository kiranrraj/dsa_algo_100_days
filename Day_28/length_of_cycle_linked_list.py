# Problem: 87
# Problem: Length of Cycle in Linked List
# Author: Kiranraj R.
# Date: 18/01/2026
# DSA Topic: Linked List, Cycle Detection
# Difficulty Level: Medium
# --------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(1)
# --------------------------------

# Problem Statement:
# Given the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer. Return the length of
# the cycle if it exists, otherwise return 0.

# Approach:
# 1. Use Floyd's Tortoise and Hare algorithm to detect a cycle.
# 2. If a cycle is detected, keep one pointer fixed and move the other pointer
#    around the cycle until it meets the first pointer again, counting the number
#    of nodes in the cycle.
# 3. Return the count as the length of the cycle.
# 4. If no cycle is detected, return 0.


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def cycle_length(head: ListNode) -> int:
    if not head:
        return 0

    slow = head
    fast = head
    has_cycle = False

    # Step 1: Detect cycle using Floyd's algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return 0

    # Step 2: Calculate the length of the cycle
    cycle_length = 1
    current = slow.next
    while current != slow:
        cycle_length += 1
        current = current.next

    return cycle_length


# Example usage:
# Case 1: Cycle exists
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print(cycle_length(node1))

# Case 2: No cycle
nodeA = ListNode(1)
print(cycle_length(nodeA))

# Case 3: Self-loop
nodeB = ListNode(1)
nodeB.next = nodeB
print(cycle_length(nodeB))
