# Problem: 1
# Problem: Two sum version that return value
# Author: Kiranraj R.
# Data: 22/12/2025
# --------------------------------------------
# Uses a hash map for O(1) lookups
# Runs in O(n) time and O(n) space


def two_sum_v1(arr, target):
    seen = set()
    for x in arr:
        complement = target - x
        if complement in seen:
            return (complement, x)
        seen.add(x)
    return None


print(two_sum_v1([1, 2, 3, 4, 5], 8))
