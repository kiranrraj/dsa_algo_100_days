# Problem: 88
# Problem: Remove Cycle from Linked List
# Author: Kiranraj R.
# Date: 18/01/2026
# DSA Topic: Linked List, Cycle Detection
# Difficulty Level: Medium
# --------------------------------
# Problem Statement:
# Given a linked list that may contain a cycle, remove the cycle if present.
# After removing the cycle, the linked list should become a linear linked list.
# Do not modify the values of the nodes, only adjust pointers.
# --------------------------------
# Approach:
# 1. Use Floyd's Cycle Detection Algorithm to detect the cycle.
# 2. If no cycle exists, return the head as it is.
# 3. If a cycle exists, find the starting node of the cycle.
# 4. Traverse the cycle to find the last node in the cycle.
# 5. Set the next of the last node to None to remove the cycle.
# --------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(1)
# --------------------------------


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def print_list(head):
    temp = head
    while temp:
        print(temp.value, end=" -> ")
        temp = temp.next
    print("None")


def remove_cycle(head: ListNode) -> ListNode:
    if not head:
        return head

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
        return head

    # Step 2: Find the starting node of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Step 3: Find the last node in the cycle
    cycle_start = slow
    while cycle_start.next != slow:
        cycle_start = cycle_start.next

    # Step 4: Remove the cycle
    cycle_start.next = None

    return head


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
# after removing cycle
head = remove_cycle(node1)
print_list(head)


# Case 2: No cycle
nodeA = ListNode(1)
# after removing cycle
head = remove_cycle(nodeA)
print_list(head)


# Case 3: Self-loop
nodeB = ListNode(1)
nodeB.next = nodeB
# after removing cycle
head = remove_cycle(nodeB)
print_list(head)
