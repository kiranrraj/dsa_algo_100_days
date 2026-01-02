# Problem: 41
# Problem: Merge sorted array
# Author: Kiranraj R.
# Data: 02/01/2026
# --------------------------------------------
# Time Complexity	O(n+m)
# Space Complexity	O(n+m)


def mergeSorted(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    if i < len(arr1):
        result.extend(arr1[i:])
    if j < len(arr2):
        result.extend(arr2[j:])

    return result


print(mergeSorted([1, 2, 3, 4], [5, 6, 7, 8]))
