# Problem: 76
# Problem: Linear search in an array using recursion. No index approach
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
# 1. Base Case: If the array is empty, return False.
# 2. If first element matches target, return True.
# 3. Recursive call on the remaining array.
# -------------------------------------------


def linear_search(arr, target):
    # Base case: empty array
    if not arr:
        return False

    # If first element matches target
    if arr[0] == target:
        return True

    # Recursive call on the remaining array
    return linear_search(arr[1:], target)


print(linear_search([1, 2, 3, 4, 5, 6], 9))
print(linear_search([1, 2, 3, 4, 5, 6], 4))
print(linear_search([], 9))
