# Problem: 47
# Problem: Backspace String Compare
# Author: Kiranraj R.
# Data: 04/01/2026
# --------------------------------------------
# Given two strings s and t, where # means “backspace” (delete the previous character if any),
# return true if they become equal after processing.
# --------------------------------------------
# Time Complexity: O(n + m)
# Space Complexity: O(1)


def backspaceCompare_v2(s: str, t: str) -> bool:
    # Start from the end
    i, j = len(s) - 1, len(t) - 1
    # To track skip count
    skip_count_s, skip_count_t = 0, 0

    # We use OR because one string may still have pending
    # characters/backspaces even if the other ended.
    while i >= 0 or j >= 0:
        while i >= 0:

            # Case: 1
            # If char is # then increment skip count, reduce i
            if s[i] == "#":
                skip_count_s += 1
                i -= 1

            # Case: 2
            # if skip count greater than 0, means the char is not #
            # and we have pending to delete, reduce skip count and reduce the
            # value of i so the character is skipper for comparison.
            elif skip_count_s > 0:
                skip_count_s -= 1
                i -= 1
            # Case: 3
            # Char is not # or nothing pending to delete, process the character as
            # it is
            else:
                break
        # Same as above
        while j >= 0:
            if t[j] == "#":
                skip_count_t += 1
                j -= 1
            elif skip_count_t > 0:
                skip_count_t -= 1
                j -= 1
            else:
                break

        # After skipping deleted characters, if both pointers are valid,
        # the characters must match; if only one is valid, the strings differ.
        if i >= 0 and j >= 0:
            # Case A:
            # Both pointers are pointing to valid characters
            if s[i] != t[j]:
                return False

        elif i >= 0 or j >= 0:
            # Case B:
            # One string still has a valid character
            # The other string has no characters left
            return False

        # move both pointers left to continue searching for the next valid characters.
        i -= 1
        j -= 1

    return True


print(backspaceCompare_v2("ab#c", "ad#c"))
print(backspaceCompare_v2("ab##", "c#d#"))
print(backspaceCompare_v2("a#c", "b"))
print(backspaceCompare_v2("a##c", "#a#c"))
