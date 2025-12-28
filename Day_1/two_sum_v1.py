# Problem: 1
# Problem: Two sum version that return value
# Author: Kiranraj R.
# Data: 22/12/2025
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)


def two_sum_v1(arr, target):
    seen = set()
    for x in arr:
        complement = target - x
        if complement in seen:
            return (complement, x)
        seen.add(x)
    return None


print(two_sum_v1([1, 2, 3, 4, 5], 8))

## Calculate what number is needed to reach the target.
