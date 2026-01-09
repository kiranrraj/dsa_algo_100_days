# Problem: 9
# Problem: Remove duplicate elements from sorted array
# Author: Kiranraj R.
# Date: 25/12/2025
# --------------------------------------------
# You are given a sorted integer array nums (sorted in non-decreasing order),
# and your task is to modify the array in-place so that only the first occurrence
# of each unique value remains in its original position. Any duplicate value that
# appears after its first occurrence should be replaced with the placeholder "_".
# After marking all duplicate occurrences, rearrange the array in-place so that all
# unique values appear at the beginning of the array in sorted order, while all "_"
# placeholders are moved to the end of the array. The relative order of the unique
# numbers must be preserved, and no additional arrays should be used to store the results.


def remove_duplicate_sorted_array(arr1):

    for i in range(1, len(arr1)):
        if arr1[i] == arr1[i - 1]:
            arr1[i] = "_"

    index = 0

    for j in range(len(arr1)):
        if arr1[j] != "_":
            arr1[index] = arr1[j]
            index += 1

    while index < len(arr1):
        arr1[index] = "_"
        index += 1

    return arr1


print(remove_duplicate_sorted_array([1, 2, 3, 3, 4, 4, 5, 5, 5, 5]))
