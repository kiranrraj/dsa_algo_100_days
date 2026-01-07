# Problem: 56
# Problem: Reverse First K Elements of a Queue
# Author: Kiranraj R.
# Data: 07/01/2026
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(k)


from collections import deque


def reverse_k_elem_queue(queue, k):
    # if k is 0 or k greater than queue length return the queue
    if k <= 0 or k > len(queue):
        return queue

    # To hold k elements
    stack = []

    # Remove first k elements
    for _ in range(k):
        stack.append(queue.popleft())

    # Insert the k elements in reverse order to the back of the
    # queue, as we can add only at the back of the queue.
    while stack:
        queue.append(stack.pop())

    # Calculate the elements to move to back of the queue so that
    # the reversed elements will come to front
    remaining_count = len(queue) - k

    for _ in range(remaining_count):
        # Move elements from front and add to back
        queue.append(queue.popleft())

    return queue


q1 = deque([1, 2, 3, 4, 5])
K = 3
print(reverse_k_elem_queue(q1, K))
# deque([3, 2, 1, 4, 5])
