# Problem: 64
# Problem: Count half nodes in a Binary Tree
# Author: Kiranraj R.
# Date: 10/01/2026
# -------------------------------------------
#
# Time Complexity:  O(n)
# Space Complexity: O(h)


# Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_half_node(root):
    if root is None:
        return 0

    count = 0
    # Full node will have both left and right children
    if (root.left is None and root.right is not None) or (
        root.left is not None and root.right is None
    ):
        count = 1

    return count + count_half_node(root.left) + count_half_node(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

print(count_half_node(root))
