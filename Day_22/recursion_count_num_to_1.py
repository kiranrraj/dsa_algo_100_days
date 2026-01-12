# Problem: 70
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
# Count from n to 1 using recursion
# -------------------------------------------
# Recursion Approach:
# Code before the recursive call runs while going deeper.
# Code after the recursive call runs while coming back.


# Count from n to 0 using recursion
def count_n_to_1(n):
    if n == 0:
        return
    print(n, end=" ")
    count_n_to_1(n - 1)


count_n_to_1(4)
print("\n")

# ---------------------------------
# Call stack visualization:
# count_n_to_1(4)
#   print(4)
#   count_n_to_1(3)
#       print(3)
#       count_n_to_1(2)
#           print(2)
#           count_n_to_1(1)
#               print(1)
#               count_n_to_1(0)
#                   -> return
#
# output: 4 3 2 1
