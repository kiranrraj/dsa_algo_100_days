# Problem: 44
# Problem: Baseball game
# Author: Kiranraj R.
# Data: 03/01/2026
# --------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)


def baseball_game(arr):
    stack = []

    for op in arr:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)


print(baseball_game([1, 2, "+", 4, "D", 5, 6, "+", "D"]))
