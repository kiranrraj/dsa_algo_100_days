# Problem: 6
# Problem: Merge Sorted Array where one array have m+n length
# Author: Kiranraj R.
# Data: 24/12/2025
# --------------------------------------------
# Question
# You are given two sorted integer arrays nums1 and nums2, sorted in non-decreasing order.
# nums1 has a length of m + n. The first m elements of nums1 are valid. The last n elements
# of nums1 are empty space (represented by 0) and should be ignored nums2 has a length of n
#
# Time Complexity	O(m + n)
# Space Complexity	O(1)


def mergeSortedArrayV2(arr1, m, arr2, n):
    position = m + n - 1
    arr1_element = m - 1
    arr2_element = n - 1
    while arr1_element >= 0 and arr2_element >= 0:
        if arr1[arr1_element] < arr2[arr2_element]:
            arr1[position] = arr2[arr2_element]
            arr2_element -= 1
        else:
            arr1[position] = arr1[arr1_element]
            arr1_element -= 1
        position -= 1

    while arr2_element >= 0:
        arr1[position] = arr2[arr2_element]
        position -= 1
        arr2_element -= 1

    return arr1


nums1 = [1, 3, 5, 0, 0, 0]
m = 3
nums2 = [2, 4, 6]
n = 3

print(mergeSortedArrayV2(nums1, m, nums2, n))
