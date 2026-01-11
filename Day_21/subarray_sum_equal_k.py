# Problem: 66
# Problem: Subarray Sum Equals K
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
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
# -------------------------------------------
# Approach:
# I maintain a running prefix sum and a hash map that stores how many times each prefix sum has
# appeared. At each index, I check if running_sum − target exists in the map. If it does, each
# occurrence represents a subarray ending at the current index whose sum is the target.
# --------------------------------------------


def subarray_sum_k(arr, target):
    if len(arr) < 1:
        return
    # To keep the count of running sum
    # {running_sum : count}
    frequency = {0: 1}
    running_sum = 0
    # Number of subarray
    count = 0

    for elem in arr:
        # Calculate running sum at each position
        running_sum += elem
        # To check if we can reduce any previous
        # running sum to get the target, we use
        # current sum - target
        need = running_sum - target
        # if what we need to remove to get the target
        # is available a as a previous running sum
        # we can say we have more sub array,
        # current count + value aganist key need
        if need in frequency:
            count += frequency[need]
        # add running_sum to the hash
        frequency[running_sum] = frequency.get(running_sum, 0) + 1
    return count


print(subarray_sum_k([1, 2, 3, 4, 5, 6, 7], 6))
