# Problem: 58
# Problem: Queue Palindrome
# Author: Kiranraj R.
# Data: 07/01/2026
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)

from collections import deque


def queue_palindrome(q):
    stack = []
    n = len(q)
    if n % 2 != 0:
        flag = True
    else:
        flag = False

    for i in range(n // 2):
        stack.append(q.popleft())
    if flag:
        q.popleft()
    for i in range(n // 2):
        if stack.pop() != q.popleft():
            return False
    return True


print(queue_palindrome(deque([1, 2, 3, 2, 1])))
print(queue_palindrome(deque([1, 2, 3, 4])))
