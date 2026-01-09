# Problem: 60
# Problem: Balanced Tree (Top Down Approach)
# Author: Kiranraj R.
# Date: 09/01/2026
# --------------------------------------------
# At each node:
#   1. Compute height of left subtree
#   2. Compute height of right subtree
#   3. If height difference > 1 → unbalanced
#   4. Otherwise, recursively check left and right subtrees
# --------------------------------------------
# Time Complexity:  O(n^2)
# Space Complexity: O(h)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Returns height of the tree rooted at node
def height(node):
    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))


# Top-down approach to check if tree is balanced
def isBalanced(root):
    if root is None:
        return True

    # compute heights
    left_height = height(root.left)
    right_height = height(root.right)

    # balance at current node
    if abs(left_height - right_height) > 1:
        return False

    # check subtrees
    return isBalanced(root.left) and isBalanced(root.right)


# Balanced tree
bt1 = TreeNode(1)
bt1.left = TreeNode(2)
bt1.right = TreeNode(3)
bt1.left.left = TreeNode(4)
bt1.left.right = TreeNode(5)
bt1.right.left = TreeNode(6)
bt1.right.right = TreeNode(7)
print(isBalanced(bt1))


# Unbalanced tree
bt2 = TreeNode(1)
bt2.left = TreeNode(2)
bt2.left.left = TreeNode(3)
bt2.left.left.left = TreeNode(4)
print(isBalanced(bt2))
