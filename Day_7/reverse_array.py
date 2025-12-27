# Problem: 22
# Problem: Reverse an array
# Author: Kiranraj R.
# Data: 28/12/2025
# ----------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)


def reverse_array_v1(arr):

    length = len(arr)
    if length < 1:
        return arr
    for i in range(length // 2):
        arr[i], arr[length - 1 - i] = arr[length - 1 - i], arr[i]
    return arr


def reverse_array_v2(arr):
    length = len(arr)
    if length < 1:
        return arr
    left = 0
    right = length - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


print(reverse_array_v1([1, 2, 3, 4, 5]))
print(reverse_array_v2([1, 2, 3, 4, 5]))
