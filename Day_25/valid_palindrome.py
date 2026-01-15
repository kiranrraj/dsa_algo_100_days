# Problem: 81
# Problem: Valid Palindrome (Ignore Non-Alphanumeric)
# Author: Kiranraj R.
# Date: 15/01/2026
# DSA topic: String / Two Pointers
# Difficulty: Easy
# -------------------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(1)
# -------------------------------------------
# Problem Statement:
# Given a string s, return True if it is a palindrome, or False otherwise.
# A palindrome reads the same forward and backward.
# Ignore non-alphanumeric characters and ignore case.
# -------------------------------------------
# Approach:
# 1. Use two pointers: left at start, right at end.
# 2. Move left forward until it points to an alphanumeric character.
# 3. Move right backward until it points to an alphanumeric character.
# 4. Compare characters (case-insensitive). If mismatch, return False.
# 5. Continue until left >= right. Return True.
# -------------------------------------------


def is_valid_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Example usage:
print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_valid_palindrome("race a car"))  # False
print(is_valid_palindrome(" "))  # True
