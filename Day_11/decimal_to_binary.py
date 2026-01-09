# Problem: 39
# Problem: Decimal to binary
# Author: Kiranraj R.
# Date: 01/01/2026
# --------------------------------------------
# Time Complexity	O(n)
# Space Complexity	O(n)


def decimal_to_binary(num):
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    return decimal_to_binary(num // 2) + str(num % 2)


print(decimal_to_binary(8))
