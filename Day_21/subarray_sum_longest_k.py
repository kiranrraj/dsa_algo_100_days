# Problem: 68
# Problem: Longest subarray with sum equals k
# Author: Kiranraj R.
# Date: 11/01/2026
# DSA topic: Prefix Sum + Hash Map
# Difficulty: Medium
# -------------------------------------------
#
# Time Complexity:  O(n)
# Space Complexity: O(n)

# -------------------------------------------
# Problem Statement:
# Given an array of integers nums, return the
# longest subarray length whose sum equals to k.
# -------------------------------------------
# Approach:
# To find the longest subarray with sum equal to k, we can use a hash map to store the earliest
# occurrence of each prefix sum. As we iterate through the array, we calculate the running prefix
# sum. For each prefix sum, we check if there exists a previous prefix sum such that the difference
# between the current prefix sum and the previous prefix sum equals k. If such a previous prefix
# sum exists, we calculate the length of the subarray and update the maximum length.


def longest_subarray_sum_k(arr, k):
    if not arr:
        return 0, None

    # {sum : index}
    first_index = {0: -1}
    prefix_sum = 0
    best_len = 0
    best_range = None

    for j, x in enumerate(arr):
        prefix_sum += x
        need = prefix_sum - k

        # If we have seen "need" before, that means the subarray
        # between the previous index and current index sums to k
        # that is what we are looking for, now we need to check if
        # its the longest one
        if need in first_index:
            i = first_index[need]
            curr_len = j - i
            # Update best length and range if needed
            if curr_len > best_len:
                best_len = curr_len
                best_range = (i + 1, j)

        # If we have not seen this prefix sum before,
        # we add it to the hash map with its index.
        if prefix_sum not in first_index:
            first_index[prefix_sum] = j

    return best_len, best_range


print(longest_subarray_sum_k([1, 2, 3, 4, 5, 6, 7], 12))
