# Problem: 10
# Problem: Valid Parentheses
# Author: Kiranraj R.
# Data: 26/12/2025
# --------------------------------------------
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def validParentheses(s):
    string_list = list(s)
    stack = []
    parenthese_dict = {")": "(", "}": "{", "]": "["}

    for i in string_list:
        if i in parenthese_dict:
            if not stack or stack.pop() != parenthese_dict[i]:
                return False
        else:
            stack.append(i)
    return len(stack) == 0


print(validParentheses("()[]{}"))
