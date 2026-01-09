# Problem: 21
# Problem: Find min and max in an array
# Author: Kiranraj R.
# Date: 28/12/2025
# ----------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)


def find_min_max_array(arr):
    current_min = arr[0]
    current_max = arr[0]

    for i in arr:
        if i < current_min:
            current_min = i
        if i > current_max:
            current_max = i
    return (current_min, current_max)


print(find_min_max_array([10, 4, 7, 3, 20, 4, 5, 7]))
