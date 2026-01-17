# Problem: 85
# Problem: Cycle Detection in Linked List (Hash Set Method)
# Author: Kiranraj R.
# Date: 17/01/2026
# DSA topic: Linked List / Hash Set
# Difficulty: Medium
# -------------------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(n)
# -------------------------------------------

# Problem Statement:
# Given a linked list, determine if it has a cycle in it
# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail
# 's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# -------------------------------------------

# Approach:
# 1. Use a hash set to keep track of visited nodes.
# 2. Traverse the linked list and for each node, check if it is already in the set.
# 3. If it is, a cycle is detected; return True.
# 4. If it is not, add it to the set and move to the next node.
# 5. If the end of the list is reached (null), return False.
# -------------------------------------------


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head: ListNode) -> bool:
    visited = set()
    current = head

    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next

    return False


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
