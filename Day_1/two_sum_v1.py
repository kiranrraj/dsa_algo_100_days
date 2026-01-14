# Problem: 1
# Problem: Two sum version that return value
# Author: Kiranraj R.
# Date: 22/12/2025
# Difficulty: Easy
# DSA Topic: Hashing
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)
# Problem Statement: Given an array of integers, return the indices of the two
# numbers such that they add up to a specific target. You may assume that each
# input would have exactly one solution, and you may not use the same element twice.
# --------------------------------------------
# Approach: Use a set to track seen numbers and check for complements.
# --------------------------------------------


def two_sum_v1(arr, target):
    seen = set()
    for x in arr:
        complement = target - x
        if complement in seen:
            return (complement, x)
        seen.add(x)
    return None


# Example usage:
print(two_sum_v1([1, 2, 3, 4, 5], 8))
print(two_sum_v1([10, 15, 3, 7], 17))
print(two_sum_v1([2, 7, 11, 15], 9))
print(two_sum_v1([3, 2, 4], 6))
print(two_sum_v1([3, 3], 6))
# --------------------------------------------
# Calculate what number is needed to reach the target.
