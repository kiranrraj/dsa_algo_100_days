# Problem: 63
# Problem: Count Full Nodes in a Binary Tree
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


def count_full_node(root):
    if root is None:
        return 0

    count = 0
    # Full node will have both left and right children
    if root.left is not None and root.right is not None:
        count = 1

    return count + count_full_node(root.left) + count_full_node(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

print(count_full_node(root))
