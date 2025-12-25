# Problem: 8
# Problem: Remove duplicate elements from sorted array
# Author: Kiranraj R.
# Data: 25/12/2025
# --------------------------------------------
# You are given an integer array nums sorted in non-decreasing order. Your task is
# to modify the array in-place such that only the first occurrence of each value
# remains unchanged, and every subsequent duplicate occurrence of the same value
# is replaced with the placeholder "_". The relative order of the elements should
# be preserved, and you should not use any additional arrays to store the result.
# This operation must be done in-place. The final array should contain the unique
# values in their original positions, while all positions corresponding to duplicate
# values should contain "_".


def remove_duplicate_sorted_array(arr1):
    seen = set()

    for i in range(1, len(arr1)):
        if arr1[i] == arr1[i - 1]:
            arr1[i] = "_"
    return arr1


print(remove_duplicate_sorted_array([1, 2, 3, 3, 4, 4, 5, 5, 5]))
