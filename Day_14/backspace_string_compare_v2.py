# Problem: 46
# Problem: Backspace String Compare
# Author: Kiranraj R.
# Date: 04/01/2026
# --------------------------------------------
# Given two strings s and t, where # means “backspace” (delete the previous character if any),
# return true if they become equal after processing.
# --------------------------------------------
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)


def backspaceCompare_v1(s: str, t: str) -> bool:
    string_1_stack = []
    string_2_stack = []

    for ch in s:
        if ch == "#":
            if string_1_stack:
                string_1_stack.pop()
        else:
            string_1_stack.append(ch)

    for ch in t:
        if ch == "#":
            if string_2_stack:
                string_2_stack.pop()
        else:
            string_2_stack.append(ch)

    return string_1_stack == string_2_stack


print(backspaceCompare_v1("ab#c", "ad#c"))
print(backspaceCompare_v1("ab##", "c#d#"))
print(backspaceCompare_v1("a#c", "b"))
print(backspaceCompare_v1("a##c", "#a#c"))
