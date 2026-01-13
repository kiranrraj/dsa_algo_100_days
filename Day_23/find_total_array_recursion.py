# Problem: 74
# Problem: Find total of array using recursion
# Author: Kiranraj R.
# Date: 13/01/2026
# DSA topic: Recursion
# Difficulty: Easy
# -------------------------------------------

# Time Complexity:  O(n)
# Space Complexity: O(n) (due to recursion stack)
# -------------------------------------------
# Problem Statement:
# Given an array, find the total sum of its elements using recursion.
# -------------------------------------------
# Approach:
# 1. Base Case: If the array has only one element, return that element.
# 2. sum in rest: Recursively find the sum of the rest of the array.
# 3. Add: Return the sum of the current element and the sum of the rest
# of the array.
# -------------------------------------------


def find_total(arr, index):
    # Exit when you reach the last element
    if index == len(arr):
        return 0
    # Check sum of rest of the arr
    total = find_total(arr, index + 1)
    # Add total plus the current value
    return total + arr[index]


print(find_total([3, 5, 2, 9, 1], 0))  # Output: 20
print(find_total([], 0))  # Output: 0
print(find_total([10, 20, 30], 0))  # Output: 60
print(find_total([7], 0))  # Output: 7
