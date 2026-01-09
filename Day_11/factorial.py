# Problem: 38
# Problem: Factorial of a number
# Author: Kiranraj R.
# Date: 01/01/2026
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


print(factorial(0))
