# Problem: 17
# Problem: Tree DS - Min, Max Value in BST
# Author: Kiranraj R.
# Date: 27/12/2025
# ----------------------------------------------------------------
# In a BST, the lowest value is always at the deepest left node and
# the highest value is always at the deepest right node.
#
# Time Complexity:  O(h)
# Space Complexity: O(h)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_min(root):
    if root is None:
        return None
    if root.left is None:
        return root.val
    return find_min(root.left)


def find_max(root):
    if root is None:
        return None
    if root.right is None:
        return root.val
    return find_max(root.right)


def find_min_max(root):
    return (find_min(root), find_max(root))


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.left.left.left = Node(2)
root.right.left = Node(25)
root.right.right = Node(35)
root.right.right.right = Node(40)

print(find_min_max(root))
