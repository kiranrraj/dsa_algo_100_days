# Problem: 93
# Problem: Merge Two Sorted Linked Lists (Without Dummy Node)
# Author: Kiranraj R.
# Date: 20/01/2026
# DSA Topic: Linked List
# Difficulty Level: Easy
# --------------------------------

# Problem Statement:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists. Return the head of the merged linked list.
# --------------------------------
# Approach:
# 1. Check if either list is empty; if so, return the other list.
# 2. Determine the head of the merged list by comparing the first nodes of both lists.
# 3. Create a tail pointer to keep track of the last node in the merged list.
# 4. Loop through both lists, comparing the current nodes and attaching the smaller
#    one to the merged list.
# 5. Move the tail pointer forward and the pointer of the list from which a node was taken.
# 6. After the loop, if there are remaining nodes in either list, attach them to the end
#    of the merged list.
# --------------------------------

# Time Complexity:  O(n+m)
# Space Complexity: O(1)
# --------------------------------


def merge_two_sorted_lists(l1, l2):
    # If one list is empty, return the other
    if not l1:
        return l2
    if not l2:
        return l1

    # Step 1: Decide the head of merged list
    if l1.value <= l2.value:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    # Tail will build the merged list
    tail = head

    # Step 2: Merge by comparing nodes
    while l1 and l2:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Step 3: Attach remaining nodes
    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return head


# Example usage:
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

nodeA = Node(2)
nodeB = Node(4)
nodeC = Node(6)
nodeD = Node(8)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD

merged = merge_two_sorted_lists(node1, nodeA)

# Print result
temp = merged
while temp:
    print(temp.value, end=" -> ")
    temp = temp.next
print("None")
