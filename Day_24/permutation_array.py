# Problem: 78
# Problem: Permutations of a String/Array
# Author: Kiranraj R.
# Date: 14/01/2026
# DSA topic: Recursion
# Difficulty: Medium
# -------------------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(n) (due to recursion stack)
# -------------------------------------------
# Problem Statement:
# Given a string/array, find all the permutations of the string/array using recursion.
# -------------------------------------------
# Approach:
# 1. Base Case: If we reach the end of the string/array, record the current permutation.
# 2. Swap: For each index, swap the current index with every other index to generate new permutations.
# 3. Recurse: Move to the next index and repeat the process.
# 4. Backtrack: Swap back to restore the original configuration for the next iteration.
# -------------------------------------------


def permute(letters):
    result = []

    def backtrack(index):
        # If we are at the last letter, there are no more swaps to make.
        if index == len(letters):
            result.append("".join(letters))
            return

        for i in range(index, len(letters)):
            # Put a letter into the current index slot
            letters[index], letters[i] = letters[i], letters[index]

            # Move to the next slot (index + 1)
            backtrack(index + 1)

            # Swap them back so the next loop starts fresh
            letters[index], letters[i] = letters[i], letters[index]

    backtrack(0)
    return result


string = "ABC"
permutations = permute(list(string))
print(permutations)
# Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
array = [1, 2, 3]
permutations_array = permute([str(num) for num in array])
print(permutations_array)
# Output: ['123', '132', '213', '231', '312', '321']
