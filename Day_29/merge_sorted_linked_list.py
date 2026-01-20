# Problem: 92
# Problem: Merge Two Sorted Linked Lists (With Dummy Node)
# Author: Kiranraj R.
# Date: 19/01/2026
# DSA Topic: Linked List
# Difficulty Level: Easy
# --------------------------------

# Problem Statement:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists. Return the head of the merged linked list.
# --------------------------------

# Approach:
# 1. Create a dummy node to help build the merged list.
# 2. Initialize a current pointer to the dummy node.
# 3. Loop until one of the lists becomes empty.
# 4. Compare the values of the current nodes in both lists.
# 5. Attach the smaller node to the current pointer and move the corresponding list pointer forward.
# 6. Move the current pointer forward.
# 7. After the loop, if one list still has nodes, attach them directly to the current pointer.
# 8. The real head is after the dummy node.
# --------------------------------

# Time Complexity:  O(n+m) where n and m are the lengths of the two lists
# Space Complexity: O(1)
# --------------------------------


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_two_sorted_lists(list1, list2):
    # Create a dummy node to help build the merged list
    dummy = Node()
    current = dummy  # This will move along the merged list

    # Loop until one of the lists becomes empty
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1  # attach node from list1
            list1 = list1.next  # move list1 forward
        else:
            current.next = list2  # attach node from list2
            list2 = list2.next  # move list2 forward

        current = current.next  # move current forward

    # If one list still has nodes, attach them directly
    if list1:
        current.next = list1
    else:
        current.next = list2

    # The real head is after the dummy node
    return dummy.next
