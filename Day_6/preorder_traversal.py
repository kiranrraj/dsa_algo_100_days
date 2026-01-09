# Problem: 12
# Problem: Tree DS - Preorder traversal
# Author: Kiranraj R.
# Date: 27/12/2025
# --------------------------------------------
#
# Time	O(n)	Each node is visited once
# Space O(h)	Height of tree due to recursion stack
#
# Preorder: Root -> Left -> Right


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    if root:
        print(root.val, "->", end="")
        preorder(root.left)
        preorder(root.right)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(35)

preorder(root)
