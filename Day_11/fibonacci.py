# Problem: 37
# Problem: Fibonacci
# Author: Kiranraj R.
# Date: 01/01/2026
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))
