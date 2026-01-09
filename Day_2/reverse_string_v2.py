# Problem: 4
# Problem: Reverse a string
# Author: Kiranraj R.
# Date: 23/12/2025
# --------------------------------------------
# Time complexity: O(n)
# Space complexity: O(n)


def reverseString_v2(string):
    return string[::-1]


def reverseString_v3(string):
    return "".join(reversed(string))
