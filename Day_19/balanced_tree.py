# Problem: 59
# Problem: Balanced Tree
# Author: Kiranraj R.
# Date: 09/01/2026
# --------------------------------------------
# We recursively visit each node and compute the height of its left and
# right subtrees. If at any node the height difference is greater than 1,
# the tree is unbalanced. The base case is: if the node is None, return
# height 0. Otherwise, return 1 + max(left_height, right_height).
#
# Although the recursion starts at the root, the balance decision is made
# only after computing subtree heights, so the solution is bottom-up.
#
# ----------------------------------------------
# Time complexity: O(n)
# Space complexity: O(h)


# To create tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_height(root):

    def dfs(node):
        if node is None:
            return 0

        # Compute left subtree height
        left_height = dfs(node.left)
        if left_height == -1:
            return -1

        # Compute right subtree height
        right_height = dfs(node.right)
        if right_height == -1:
            return -1

        # If current node is unbalanced, return -1
        if abs(left_height - right_height) > 1:
            return -1

        # Otherwise return current subtree height
        # current node itself counts as a level
        return 1 + max(left_height, right_height)

    return dfs(root) != -1


bt1 = TreeNode(1)
bt1.left = TreeNode(2)
bt1.right = TreeNode(3)
bt1.left.left = TreeNode(4)
bt1.left.right = TreeNode(5)
bt1.right.left = TreeNode(6)
bt1.right.right = TreeNode(7)
print(get_height(bt1))


bt2 = TreeNode(1)
bt2.left = TreeNode(2)
bt2.right = TreeNode(3)
bt2.left.left = TreeNode(4)
bt2.left.right = TreeNode(5)
bt2.right.left = TreeNode(6)
bt2.right.right = TreeNode(7)
bt2.right.right.right = TreeNode(8)
bt2.right.right.right.right = TreeNode(9)
print(get_height(bt2))
