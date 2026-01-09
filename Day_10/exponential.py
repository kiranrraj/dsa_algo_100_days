# Problem: 36
# Problem: Exponential of the number
# Author: Kiranraj R.
# Date: 31/12/2025
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)


def exponentialFunc(base, exponential):
    if exponential == 0:
        return 1
    return base * exponentialFunc(base, exponential - 1)


print(exponentialFunc(3, 5))
