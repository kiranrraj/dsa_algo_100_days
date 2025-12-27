# Problem: 24
# Problem: Check second largest number in array
# Author: Kiranraj R.
# Data: 28/12/2025
# ----------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)


def second_largest_num(arr):
    largest = float("-inf")
    second_largest = float("-inf")

    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        # i is between largest and second_largest
        elif i > second_largest and i < largest:
            second_largest = i
    return second_largest if second_largest != float("-inf") else None


print(second_largest_num([10, 12, 33, 19, 53]))
print(second_largest_num([21, 44, 70, 90, 5]))
