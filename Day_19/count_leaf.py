# Problem: 60
# Problem: Count Leaf Nodes in a Binary Tree
# Author: Kiranraj R.
# Date: 09/01/2026
# -------------------------------------------
# Idea:
# - Traverse the tree recursively
# - If node is None → no leaf → return 0
# - If node has no children → it is a leaf → return 1
# - Otherwise, sum leaf counts from left and right subtrees
#
# Time Complexity:  O(n)
# Space Complexity: O(h)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def countLeafNodes(root):
    if root is None:
        return 0

    # If both children are None, this is a leaf node
    if root.left is None and root.right is None:
        return 1

    # Otherwise, count leaves in left and right subtrees
    return countLeafNodes(root.left) + countLeafNodes(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

print(countLeafNodes(root))
