# Problem           : 59
# Problem           : Remove Outermost Parentheses
# Difficulty Level  : Easy
# DSA type          : Stack / Counter
# Author            : Kiranraj R.
# Date              : 08/01/2026
# --------------------------------------------
# Given a valid parentheses string made of primitive parts, remove the outermost ( and ) of every primitive.

# Time Complexity: O(n)
# Space Complexity: O(n)


def remove_outermost_parentheses(s):
    stack = []
    depth = 0

    for char in s:
        if char == "(":
            if depth > 0:
                stack.append(char)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                stack.append(char)

    return "".join(stack)


tests = ["(()())(())", "(()())(())(()(()))", "()()", "", "(()))", "()"]
for t in tests:
    print(f"input={t!r} output={remove_outermost_parentheses(t)!r}")
