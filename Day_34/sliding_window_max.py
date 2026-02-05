# Problem: 101
# Problem: Sliding Window Maximum
# Author: Kiranraj R.
# Date: 02/02/2026
# DSA Topic: Sliding Window
# Difficulty Level: Hard
# --------------------------------

# Problem Statement:
# Given an array nums and an integer k, there is a sliding window of size k
# which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
# Return the max sliding window.
# --------------------------------

# Approach:
# 1. Use a deque to store indices of array elements.
# 2. Iterate through the array, maintaining the deque to ensure
#    that the largest element's index is always at the front.
# 3. For each position of the sliding window, append the maximum
#    element's index to the result list.
# --------------------------------

# Time Complexity: O(n)
# Space Complexity: O(k)
# -----------------

from collections import deque


def sliding_window_max(nums, k):
    result = []
    window = deque()
    for i, num in enumerate(nums):
        # Remove indices that are out of the current window
        while window and window[0] <= i - k:
            window.popleft()
        # Remove elements smaller than the current element
        while window and nums[window[-1]] < num:
            window.pop()
        window.append(i)
        # Append the maximum element for the current window
        if i >= k - 1:
            result.append(nums[window[0]])
    return result


# Example usage:
if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = sliding_window_max(nums, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {result}")
    # Output: [3, 3, 5, 5, 6, 7]
