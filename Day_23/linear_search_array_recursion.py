# Problem: 75
# Problem: Linear search in an array using recursion
# Author: Kiranraj R.
# Date: 13/01/2026
# DSA topic: Recursion
# Difficulty: Easy
# -------------------------------------------

# Time Complexity:  O(n)
# Space Complexity: O(n) (due to recursion stack)
# -------------------------------------------
# Problem Statement:
# Given an array and a target value, check if the target
# exists in the array using recursion.
# -------------------------------------------
# Approach:
# 1. Base Case: If the array has only one element, return that element.
# 2. Found: If the current element matches the target, return True.
# 3. Recur: Recursively search in the rest of the array.
# -------------------------------------------


def linear_search(arr, index, target):
    if index == len(arr):
        return False
    if arr[index] == target:
        return True

    return linear_search(arr, index + 1, target)


print(linear_search([1, 2, 3, 4, 5, 6], 0, 9))
print(linear_search([1, 2, 3, 4, 5, 6], 0, 4))
print(linear_search([], 0, 9))
