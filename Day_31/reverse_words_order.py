# Problem: 95
# Problem: Reverse the order of words in a given string
# Author: Kiranraj R.
# Date: 30/01/2026
# DSA Topic: String Manipulation
# Difficulty Level: Easy
# --------------------------------

# Problem Statement:
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

# Approach:
# 1. Split the string into words based on spaces.
# 2. Reverse the list of words.
# 3. Join the reversed list of words with a single space.
# --------------------------------

# Time Complexity:  O(n)
# Space Complexity: O(n)
# --------------------------------


def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


# Example usage:
if __name__ == "__main__":
    input_string = "the sky is blue"
    result = reverse_words(input_string)
    print(f"Input: '{input_string}'")
    print(f"Output: '{result}'")
# Output: 'blue is sky the'
