# Problem: 40
# Problem: Merge two array alternatively
# Author: Kiranraj R.
# Date: 02/01/2026
# --------------------------------------------
# Time Complexity	O(n+m)
# Space Complexity	O(n+m)


def mergeAlter(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        result.append(arr1[i])
        result.append(arr2[j])
        i += 1
        j += 1

    if len(arr1) > i:
        result.extend(arr1[i : len(arr1)])

    if len(arr2) > j:
        result.extend(arr1[j : len(arr2)])

    return result


print(mergeAlter([1, 2, 3, 4], [5, 6, 7, 8]))
