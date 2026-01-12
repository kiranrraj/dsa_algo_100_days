# Problem: 69
# Problem: Recursion count from n to 1 and 1 to n
# Author: Kiranraj R.
# Date: 12/01/2026
# DSA topic: Recursion
# Difficulty: Easy
# -------------------------------------------
#
# Time Complexity:  O(n)
# Space Complexity: O(n) (due to recursion stack)
# -------------------------------------------
# Problem Statement:
# Count from 1 to n using recursion
# -------------------------------------------
# Recursion Approach:
# Code before the recursive call runs while going deeper.
# Code after the recursive call runs while coming back.


# Count from 1 to n using recursion
def count_1_to_n(current, n):
    if current > n:
        return
    print(current, end=" ")
    count_1_to_n(current + 1, n)


count_1_to_n(1, 10)
print("\n")

# ---------------------------------
# Call stack visualization:
# count_1_to_n(1, 3)
#   print(1)
#   count_1_to_n(2, 3)
#       print(2)
#       count_1_to_n(3, 3)
#           print(3)
#           count_1_to_n(4, 3)
#               -> return
#           -> return
#       -> return
#   -> return
# output: 1 2 3


#
# Count from 1 to n using recursion, without extra parameter
# -----------------------------------------------------------------------
# Approach:
# In recursion, code written before the recursive call runs first, and code
# written after the recursive call runs when the function returns. Thus, to
# print from 1 to n, we first make the recursive call and then print the
# number after returning from the call.
# -----------------------------------------------------------------------


def count_1_to_n_v2(n):
    if n == 0:
        return
    count_1_to_n_v2(n - 1)
    print(n, end=" ")


count_1_to_n_v2(10)

# Call stack visualization:
# count_1_to_n_v2(3)
#   -> count_1_to_n_v2(2)
#       -> count_1_to_n_v2(1)
#           -> count_1_to_n_v2(0)
#               -> return
#           print(1)
#       print(2)
#   print(3)
#
# Output: 1 2 3
