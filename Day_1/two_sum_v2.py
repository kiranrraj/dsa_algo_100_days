# Problem: 2
# Problem: Two sum version that return indices
# Author: Kiranraj R.
# Data: 22/12/2025
# --------------------------------------------
# Uses a hash map for O(1) lookups
# Runs in O(n) time and O(n) space

from typing import List, Optional, Tuple


def two_sum_v2(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    seen = {}
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return (seen[complement], i)
        seen[x] = i
    return None


# Calculate the number needed to reach the target.
# Check if that needed number is already in seen
# If yes → return the stored index and the current index.
# If not → store the current number along with its index.
