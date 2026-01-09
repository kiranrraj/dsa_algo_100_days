# Problem: 18
# Problem: Tree DS - Search Value in BST
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


def search_node(root, key):
    if root == None:
        return False
    if root.val == key:
        return True
    if key < root.val:
        return search_node(root.left, key)
    else:
        return search_node(root.right, key)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.left.left.left = Node(2)
root.right.left = Node(25)
root.right.right = Node(35)
root.right.right.right = Node(40)

print(search_node(root, 40))
print(search_node(root, 44))
