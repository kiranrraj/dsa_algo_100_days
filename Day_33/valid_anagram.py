# Problem: 99
# Problem: Valid Anagram
# Author: Kiranraj R.
# Date: 01/02/2026
# DSA Topic: Hashing
# Difficulty Level: Easy
# --------------------------------

# Problem Statement:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
# --------------------------------

# Approach:
# 1. Create two dictionaries to count the frequency of each letter in both strings.
# 2. Compare the two dictionaries. If they are equal, return True; otherwise, return False.
# --------------------------------

# Time Complexity: O(n)
# Space Complexity: O(n)
# -----------------


def valid_anagram(word1, word2):
    word1_dict = {}
    word2_dict = {}

    if len(word1) != len(word2):
        return False

    for letter in word1:
        if letter in word1_dict:
            word1_dict[letter] += 1
        else:
            word1_dict[letter] = 1

    for letter in word2:
        if letter in word2_dict:
            word2_dict[letter] += 1
        else:
            word2_dict[letter] = 1

    return word1_dict == word2_dict


# Example usage:
print(valid_anagram("listen", "silent"))  # True
print(valid_anagram("hello", "world"))  # False
print(valid_anagram("anagram", "nagaram"))  # True
print(valid_anagram("python", "java"))  # False
