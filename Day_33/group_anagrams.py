# Problem: 100
# Problem: Group Anagrams
# Author: Kiranraj R.
# Date: 01/02/2026
# DSA Topic: Hashing
# Difficulty Level: Medium
# --------------------------------

# Problem Statement:
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order. An Anagram is a word
# or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.
# --------------------------------

# Approach:
# 1. Create a dictionary to store the groups of anagrams.
# 2. For each string in the input list, sort the string to create a key.
# 3. Append the original string to the list corresponding to the sorted key in the dictionary.
# 4. Finally, return the values of the dictionary as a list of lists.
# --------------------------------

# Time Complexity: O(n*mlogm)
# Space Complexity: O(n)
# -----------------


def group_anagrams(strs):
    # Create a dictionary to store the groups of anagrams
    anagram_groups = {}

    for word in strs:
        # Sort the word to create a key
        sorted_word = "".join(sorted(word))

        if sorted_word in anagram_groups:
            # Append the original word to the existing list
            anagram_groups[sorted_word].append(word)
        else:
            # Create a new list for this sorted word
            anagram_groups[sorted_word] = [word]

    # Return the grouped anagrams as a list of lists
    # we only need the values of the dictionary
    return list(anagram_groups.values())


# Example usage:
if __name__ == "__main__":
    strs = ["listen", "silent", "enlist", "inlets", "google", "gogole"]
    result = group_anagrams(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    # Output: [['listen', 'silent', 'enlist', 'inlets'], ['google', 'gogole']]
