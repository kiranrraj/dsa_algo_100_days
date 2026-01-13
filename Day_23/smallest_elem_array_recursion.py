# Problem: 73
# Problem: Smallest element in an array using recursion
# Author: Kiranraj R.
# Date: 13/01/2026
# DSA topic: Recursion
# Difficulty: Easy
# -------------------------------------------

# Time Complexity:  O(n)
# Space Complexity: O(n) (due to recursion stack)
# -------------------------------------------
## The base case stops recursion; the return statement builds the answer.
# -------------------------------------------
# Problem Statement:
# Given an array, find the smallest element using recursion.
# -------------------------------------------
# Approach:
# 1. Base Case: If the array has only one element, return that element.
# 2. min in rest: Recursively find the smallest element in the rest of the array.
# 3. Compare: Return the minimum of the current element and the smallest element
# found in the rest of the array.


def find_smallest(arr, index):
    # Exit when you reach the last element
    if index == len(arr):
        return float("inf")
    # Check for minimum in the rest of the array
    min_rest = find_smallest(arr, index + 1)
    # Compare the current element with
    # calculated minimum till now.
    return min(min_rest, arr[index])


arr = [3, 5, 2, 9, 1]
result = find_smallest(arr, 0)
print("Smallest element in the array is:", result)
print(find_smallest([], 0))
