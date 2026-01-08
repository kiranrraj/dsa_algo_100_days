# Problem: 57
# Problem: Interleave First Half of Queue with Second Half
# Author: Kiranraj R.
# Date: 07/01/2026
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)


from collections import deque


def interleave_queue(queue):
    n = len(queue)
    if n < 2:
        return queue

    left_queue = deque()
    right_queue = deque()

    for _ in range(n // 2):
        left_queue.append(queue.popleft())

    while queue:
        right_queue.append(queue.popleft())

    while left_queue:
        queue.append(left_queue.popleft())
        queue.append(right_queue.popleft())

    while right_queue:
        queue.append(right_queue.popleft())

    return queue


print(interleave_queue(deque([1, 2, 3, 4, 5, 6])))
# deque([1, 4, 2, 5, 3, 6])
print(interleave_queue(deque([1, 2, 3, 4, 5])))
# deque([1, 3, 2, 4, 5])
