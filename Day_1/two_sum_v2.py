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
