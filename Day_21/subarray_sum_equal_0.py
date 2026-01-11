# Problem: 67
# Problem: Subarray Sum Equals 0
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
# Given an array of integers nums, return the total number of
# subarrays whose sum equals to 0.
# -------------------------------------------
# Approach:
## Every time the same running sum appears again, the subarray between them sums to 0.
# I maintain a running prefix sum and a hash map that stores how many times each prefix sum has
# appeared. At each index, I check if running_sum − 0 exists in the map. If it does, each
# occurrence represents a subarray ending at the current index whose sum is 0.
# --------------------------------------------


def subarray_sum_equals_0(arr):
    if len(arr) < 1:
        return 0
    # To keep the count of running sum
    # {running_sum : count}
    frequency = {0: 1}
    running_sum = 0
    # Number of subarray
    count = 0

    for elem in arr:
        # Calculate running sum at each position
        running_sum += elem
        # Main Logic
        # Every time the same running sum appears again, the subarray between them sums to 0. So we
        # increment the count with the frequency. To understand at ith position the running sum as 7
        # and current running sum is 7 means, in between ith and current position's sub array was
        # zero, which is what we need to count
        if running_sum in frequency:
            count += frequency[running_sum]
        # add running_sum to the hash
        frequency[running_sum] = frequency.get(running_sum, 0) + 1
    return count


print(subarray_sum_equals_0([1, -1, 1, -1]))
