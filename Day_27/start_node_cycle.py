# Problem: 86
# Problem: Find Starting Node of Cycle in Linked List
# Author: Kiranraj R.
# Date: 17/01/2026
# DSA topic: Linked List / Two Pointers
# Difficulty: Medium
# -------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------

# Problem Statement:
# Given a linked list that may contain a cycle, return the node where the
# cycle begins. If there is no cycle, return null. There is a cycle in a
# linked list if there is some node in the list that can be reached again
# by continuously following the next pointer. Internally, pos is used to
# denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# -------------------------------------------

# Approach:
# 1. Use Floyd's Cycle Detection Algorithm to find the meeting point of
#    slow and fast pointers.
# 2. If a cycle is detected, initialize one pointer to the head and keep
#    the other pointer at the meeting point.
# 3. Move both pointers one step at a time until they meet again.
# 4. The meeting point is the start of the cycle.
# -------------------------------------------


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def detect_cycle_start(head: ListNode) -> ListNode:
    if not head:
        return None

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
        return None

    # Step 2: Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


# Example usage:
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print(detect_cycle_start(node1).value)
nodeA = ListNode(1)
print(detect_cycle_start(nodeA))
nodeB1 = ListNode(1)
nodeB2 = ListNode(2)
nodeB1.next = nodeB2
nodeB2.next = nodeB1
print(detect_cycle_start(nodeB1).value)
