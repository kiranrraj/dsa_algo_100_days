# Problem: 72
# Problem: Largest element in an array using recursion
# Author: Kiranraj R.
# Date: 13/01/2026
# DSA topic: Recursion
# Difficulty: Easy
# -------------------------------------------

# Time Complexity:  O(n)
# Space Complexity: O(n) (due to recursion stack)
# -------------------------------------------
# Problem Statement:
# Given an array, find the largest element using recursion.
# -------------------------------------------
# Approach:
# 1. Base Case: If the array has only one element, return that element.
# 2. max in rest: Recursively find the largest element in the rest of the array.
# 3. Compare: Return the maximum of the current element and the largest element
# found in the rest of the array.
# -------------------------------------------


def largest_element(arr, index):
    if index == len(arr) - 1:
        return arr[index]

    max_in_rest = largest_element(arr, index + 1)

    return max(arr[index], max_in_rest)


arr = [3, 5, 2, 9, 1]
result = largest_element(arr, 0)
print("Largest element in the array is:", result)
# Output: Largest element in the array is: 9
# ---------------------------------

arr2 = [10, 4, 2, 8, 6, 12, 3]
result2 = largest_element(arr2, 0)
print("Largest element in the array is:", result2)
# Output: Largest element in the array is: 12
# ---------------------------------
