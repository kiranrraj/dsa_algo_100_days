# Problem: 28
# Problem: Maximum Sum Subarray of Size K
# Author: Kiranraj R.
# Data: 29/12/2025
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(1)


def max_sum_subarray(arr, size):
    window_sum = sum(arr[:size])
    max_sum = window_sum

    for i in range(size, len(arr)):
        window_sum = window_sum + arr[i] - arr[i - size]
        max_sum = max(max_sum, window_sum)
    return max_sum


print(max_sum_subarray([1, 2, 3, 4, 5, 6], 2))
print(max_sum_subarray([1, 2, 3, 4, 5, 6], 3))
