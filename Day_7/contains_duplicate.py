# Problem: 26
# Problem: Check for duplicate
# Author: Kiranraj R.
# Data: 28/12/2025
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)
def check_for_duplicate(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False


print(check_for_duplicate([4, 5, 6, 7, 2, 3]))
