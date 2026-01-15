# Problem: 82
# Problem: Length of Last Word
# Author: Kiranraj R.
# Date: 16/01/2026
# DSA topic: String
# Difficulty: Easy
# -------------------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(1)
# -------------------------------------------
# Problem Statement:
# Given a string s consisting of words and spaces,
# return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# -------------------------------------------
# Approach:
# 1. Start from the end of the string.
# 2. Skip trailing spaces.
# 3. Count characters until a space is found or start is reached.
# 4. Return the count.
# -------------------------------------------


def length_of_last_word(s: str) -> int:
    length = 0
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == " ":
        i -= 1

    # Count characters of last word
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1

    return length


# Example usage:
print(length_of_last_word("Hello World"))  # 5
print(length_of_last_word("   fly me   to   "))  # 2
print(length_of_last_word("a"))  # 1
