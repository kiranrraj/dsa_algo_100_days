# Problem: 71
# Problem: Check array is sorted using recursion
# Author: Kiranraj R.
# Date: 12/01/2026
# DSA topic: Recursion
# Difficulty: Easy
# -------------------------------------------

# Time Complexity:  O(n)
# Space Complexity: O(n) (due to recursion stack)
# -------------------------------------------
# Problem Statement:
# Given an array, check if it is sorted in
# non-decreasing order using recursion.
# -------------------------------------------


def check_sorted(arr, index=0):
    if index >= len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return check_sorted(arr, index + 1)


print(check_sorted([1, 2, 3, 4, 5]))
print(check_sorted([1, 3, 2, 4, 5]))
print(check_sorted([]))
print(check_sorted([10, 1]))
print(check_sorted([1, 2, 2, 3, 4]))
