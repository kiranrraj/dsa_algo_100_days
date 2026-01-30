# Problem: 96
# Problem: Reverse the letters in each word of a given string
# Author: Kiranraj R.
# Date: 30/01/2026
# DSA Topic: String Manipulation
# Difficulty Level: Easy
# --------------------------------

# Problem Statement:
# Given an input string s, reverse the letters in each word while maintaining the original word order
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string with each word's letters reversed but the word order unchanged.
# --------------------------------

# Approach:
# 1. Split the string into words based on spaces.
# 2. Reverse the letters in each word.
# 3. Join the modified list of words with a single space.
# --------------------------------

# Time Complexity:  O(n)
# Space Complexity: O(n)
# --------------------------------


def reverse_letters_in_words(s: str) -> str:
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


# Example usage:
if __name__ == "__main__":
    input_string = "kiran raj r"
    result = reverse_letters_in_words(input_string)
    print(f"Input: '{input_string}'")
    print(f"Output: '{result}'")


# Output: 'ranik jar r'
