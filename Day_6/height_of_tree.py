# Problem: 14
# Problem: Tree DS - Height of tree
# Author: Kiranraj R.
# Date: 27/12/2025
# --------------------------------------------
# Time	O(n)
# Space O(h)
#


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height_of_tree(root):
    if root == None:
        return -1

    lheight = height_of_tree(root.left)
    rheight = height_of_tree(root.right)

    return 1 + max(lheight, rheight)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(35)
root.right.right.right = Node(40)

print(height_of_tree(root))
