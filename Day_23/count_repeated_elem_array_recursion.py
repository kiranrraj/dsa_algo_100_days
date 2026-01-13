# Problem: 77
# Problem: Count occurrences of an element in an array using recursion
# Author: Kiranraj R.
# Date: 13/01/2026
# DSA topic: Recursion
# Difficulty: Easy
# -------------------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(n) (due to recursion stack)
# -------------------------------------------
# Problem Statement:
# Given an array and a target value, count the number of occurrences
# of the target value in the array using recursion.
# -------------------------------------------
# Approach:
# 1. Base Case: If the index reaches the end of the array, return 0.
# 2. Found: If the current element matches the target, return 1.
# 3. Recur: Recursively search in the rest of the array.
# -------------------------------------------


def count_x(arr, index, target):
    if index == len(arr):
        return 0
    current_count = 1 if arr[index] == target else 0
    count = count_x(arr, index + 1, target)
    return count + current_count


print(count_x([1, 2, 3, 4, 2, 5, 2], 0, 2))  # Output: 3
print(count_x([1, 2, 3, 4, 5], 0, 6))  # Output: 0
print(count_x([], 0, 2))  # Output: 0
