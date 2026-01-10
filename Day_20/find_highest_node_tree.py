# Problem: 65
# Problem: Find highest value in the tree (Not BST)
# Author: Kiranraj R.
# Date: 10/01/2026
# -------------------------------------------
#
# Time Complexity:  O(n)
# Space Complexity: O(h)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_max(root):
    if root is None:
        return float("-inf")

    left_max = find_max(root.left)
    right_max = find_max(root.right)

    return max(root.val, left_max, right_max)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)

print(find_max(root))
