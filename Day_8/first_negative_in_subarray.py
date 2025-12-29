# Problem: 27
# Problem: Find the first negative number in the subarray (Brute Force)
# Author: Kiranraj R.
# Data: 29/12/2025
# --------------------------------------------


def find_first_negaive(subarray):
    for i in subarray:
        if i < 0:
            print(subarray, " ", i)
            return
    print(subarray, " ", None)


def find_fist_negative_in_window(arr, k):
    subarray = arr[:k]
    for i in range(k, len(arr)):
        subarray = subarray + arr[i] - arr[i - k]
        find_first_negaive(subarray)


find_fist_negative_in_window([1, -2, 3, -4, -6, 1, 2, 3, 4, -8, -7, 10, 30, 12], 3)
