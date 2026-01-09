# Problem: 19
# Problem: Tree DS - Insert Value in BST
# Author: Kiranraj R.
# Date: 27/12/2025
# ----------------------------------------------------------------
# Time Complexity: O(h)
# Space Complexity: O(h)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_node(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert_node(root.left, key)
    if key > root.val:
        root.right = insert_node(root.right, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, "=>", end="")
        inorder(root.right)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.left.left.left = Node(2)
root.right.left = Node(25)
root.right.right = Node(35)
root.right.right.right = Node(40)

root = insert_node(root, 12)
inorder(root)
# 2 =>5 =>10 =>12 =>15 =>20 =>25 =>30 =>35 =>40 =>
