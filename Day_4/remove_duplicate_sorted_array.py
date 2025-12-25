# Problem: 7
# Problem: Remove duplicate elements from sorted array
# Author: Kiranraj R.
# Data: 25/12/2025
# --------------------------------------------
# Given an integer array nums sorted in non-decreasing order, remove the duplicate
# values in-place such that each unique element appears only once. The relative order
# of the elements must be preserved. After processing, the first k elements of the array
# should contain the unique elements in sorted order, where k is the total number of
# unique elements in the array. The elements beyond index k - 1 may retain any value and
# can be ignored. You must perform this operation in-place without using extra space for
# another array, and finally return the modified array or the value of k


def remove_duplicate_sorted_array(arr1):
    index = 1
    for i in range(1, len(arr1)):
        if arr1[i] != arr1[i - 1]:
            arr1[index] = arr1[i]
            index += 1
    return arr1


print(remove_duplicate_sorted_array([1, 2, 3, 3, 4, 4, 5, 5, 5]))
