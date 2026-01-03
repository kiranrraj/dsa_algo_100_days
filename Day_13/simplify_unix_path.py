# Problem: 45
# Problem: Baseball game
# Author: Kiranraj R.
# Data: 03/01/2026
# --------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)


def simplify_unix_path(path):
    stack = []
    parts = path.split("/")
    for part in parts:
        if part == "." or part == "":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)


path = "/neetcode/practice//...///../courses"
print(simplify_unix_path(path))

path = "/a/./b/../../c/"
print(simplify_unix_path(path))
