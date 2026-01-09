# Problem: 11
# Problem: Tree DS - Inorder traversal
# Author: Kiranraj R.
# Date: 27/12/2025
# --------------------------------------------
# Time	O(n)	Each node is visited once
# Space O(h)	Height of tree due to recursion stack
#
# Inorder: Left -> Root -> Right


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        print(str(self.val), "=> ", end="")

        if self.right:
            self.right.inorder_traversal()


class Node1:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(str(root.val), "=>", end="")
        inorder_traversal(root.right)


root = Node1(20)
root.left = Node1(10)
root.right = Node1(30)
root.left.left = Node1(5)
root.left.right = Node1(15)
root.right.left = Node1(25)
root.right.right = Node1(35)

inorder_traversal(root)
