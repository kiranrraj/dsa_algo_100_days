# Problem: 35
# Problem: Find greatest common divisor
# Author: Kiranraj R.
# Date: 31/12/2025
# --------------------------------------------
# Time Complexity   : O(log(min(num1, num2)))
# Space Complexity  : O(log(min(num1, num2)))


def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


print(gcd(48, 18))
