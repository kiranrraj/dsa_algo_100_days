# Problem: 62
# Problem: Check two binary trees are identical
# Author: Kiranraj R.
# Date: 09/01/2026
# ---------------------------------------------
# Two binary trees are identical if:
# 1. Both are empty, OR
# 2. Root values are equal AND
# 3. Left subtrees are identical AND
# 4. Right subtrees are identical
# ----------------------------------------------
# Time Complexity:  O(n)
# Space Complexity: O(h)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def are_identical(root1, root2):
    # If both nodes are None, trees match here
    if root1 is None and root2 is None:
        return True

    # If one is None and the other is not, trees differ
    if root1 is None or root2 is None:
        return False

    # Check current node value and recurse on children
    return (
        root1.val == root2.val
        and are_identical(root1.left, root2.left)
        and are_identical(root1.right, root2.right)
    )


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)
t3 = TreeNode(1)
t3.left = TreeNode(2)
t3.right = TreeNode(4)

print(are_identical(t1, t2))
print(are_identical(t1, t3))
