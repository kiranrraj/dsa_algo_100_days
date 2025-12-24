# Problem: 5
# Problem: Merge Sorted Array (two-pointer technique)
# Author: Kiranraj R.
# Data: 24/12/2025
# --------------------------------------------
# Time Complexity: O(n + m) (each element from both arrays is visited once)
# Space Complexity: O(n + m) (merged array)


def mergeSortedArray(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    i, j = 0, 0
    mergedArr = []
    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            mergedArr.append(arr1[i])
            i += 1
        else:
            mergedArr.append(arr2[j])
            j += 1
    if i < l1:
        mergedArr.extend(arr1[i:])
    if j < l2:
        mergedArr.extend(arr2[j:])
    return mergedArr


print(mergeSortedArray([1, 3, 5, 7], [2, 4, 6, 8]))
