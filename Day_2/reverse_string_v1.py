# Problem: 3
# Problem: Reverse a string
# Author: Kiranraj R.
# Date: 23/12/2025
# --------------------------------------------
# Time complexity: O(n)
# Space complexity: O(n)


def reverseString(string):
    arrStr = list(string)
    i, j = 0, len(arrStr) - 1

    while i < j:
        arrStr[i], arrStr[j] = arrStr[j], arrStr[i]
        i += 1
        j -= 1

    return "".join(arrStr)


print(reverseString("kiran"))
