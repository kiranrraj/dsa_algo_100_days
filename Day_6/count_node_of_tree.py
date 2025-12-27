# Problem: 15
# Problem: Tree DS - Number of nodes
# Author: Kiranraj R.
# Data: 27/12/2025
# --------------------------------------------
# Time Complexity:   O(n)
# Space Complexity:  O(h) Due to recursive call


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_Nodes(root):
    if root == None:
        return 0
    return 1 + count_Nodes(root.left) + count_Nodes(root.right)


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.left.left.left = Node(2)
root.right.left = Node(25)
root.right.right = Node(35)
root.right.right.right = Node(40)

print(count_Nodes(root))
