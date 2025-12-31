# Problem: 34
# Problem: Sum of digits
# Author: Kiranraj R.
# Data: 31/12/2025
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)


def sum_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_digits(num // 10)


print(sum_digits(123))
