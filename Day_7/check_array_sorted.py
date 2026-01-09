# Problem: 23
# Problem: Check array is sorted or not
# Author: Kiranraj R.
# Date: 28/12/2025
# ----------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1)


def is_array_sorted(arr):
    current = arr[0]
    length = len(arr)

    if length <= 1:
        return True

    for i in range(1, length):
        if current > arr[i]:
            return False
        else:
            current = arr[i]
    return True


print(is_array_sorted([1, 2, 3, 4, 5, 6]))
print(is_array_sorted([1, 9, 3, 4, 5, 6]))
