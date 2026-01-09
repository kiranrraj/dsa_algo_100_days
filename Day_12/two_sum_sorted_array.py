# Problem: 42
# Problem: The Two Sum II - Input Array Is Sorted
# Author: Kiranraj R.
# Date: 02/01/2026
# --------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)


def two_sum(arr, target):
    if len(arr) < 2:
        return None
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if target == current_sum:
            return (arr[left], arr[right])
        elif target > current_sum:
            left += 1
        else:
            right -= 1
    return None


print(two_sum([1, 2, 3, 4, 5, 6], 9))
