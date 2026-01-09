# Problem: 20
# Problem: Tree DS - Delete Value in BST (inorder successor)
# Author: Kiranraj R.
# Date: 27/12/2025
# ----------------------------------------------------------------
# FUNCTION delete_node(root, key):
#     IF root is NULL:
#         RETURN NULL
#
#     IF key < root.val:
#         root.left = delete_node(root.left, key)
#         RETURN root
#
#     ELSE IF key > root.val:
#         root.right = delete_node(root.right, key)
#         RETURN root
#
#     ELSE:
#         # Case 1: No children
#         IF root.left == NULL AND root.right == NULL:
#             RETURN NULL
#         # Case 2: One child (right only)
#         IF root.left == NULL:
#             RETURN root.right
#         # Case 2: One child (left only)
#         IF root.right == NULL:
#             RETURN root.left
#         # Case 3: Two children
#         successor = findMin(root.right)   # smallest in right subtree
#         root.val = successor.val
#         root.right = delete_node(root.right, successor.val)
#         RETURN root
#
# FUNCTION findMin(node):
#     WHILE node.left IS NOT NULL:
#         node = node.left
#     RETURN node


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Inorder traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(str(root.val), "=>", end="")
        inorder_traversal(root.right)


# Find the smallest value as we go down the left side
def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def delete_node(root, key):
    if root is None:
        return None

    # To find the key
    if key < root.val:
        root.left = delete_node(root.left, key)
        return root
    elif key > root.val:
        root.right = delete_node(root.right, key)
        return root
    else:
        # Node found

        # No children case
        # After deletion, the subtree rooted at Node(key) should be empty.
        if root.left is None and root.right is None:
            return None

        # One child case
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Go to the right subtree, Find the smallest value there
        # That node is the next larger value than root
        successor = find_min(root.right)
        # copying the successor’s value.
        root.val = successor.val
        # Delete the successor node from right subtree
        # Since successor came from the right subtree,
        # the delete call must also happen in the right subtree
        root.right = delete_node(root.right, successor.val)
        return root


root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.left.left.left = Node(2)
root.right.left = Node(25)
root.right.right = Node(35)
root.right.right.right = Node(40)

root = delete_node(root, 15)
inorder_traversal(root)
# 2 =>5 =>10 =>20 =>25 =>30 =>35 =>40 =>None
