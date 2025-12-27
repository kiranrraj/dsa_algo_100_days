# Problem: 13
# Problem: Tree DS - Postorder traversal
# Author: Kiranraj R.
# Data: 27/12/2025
# --------------------------------------------
#
# Time	O(n)	Each node is visited once
# Space O(h)	Height of tree due to recursion stack
#
# Postorder: Left -> Right -> Root


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, "->", end="")


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(35)

postorder(root)
