# Problem: 63
# Problem: Lowest Common Ancestor (Binary Tree - NOT BST)
# Author: Kiranraj R.
# Date: 09/01/2026
# ---------------------------------------------
# - If current node is None -> return None
# - If current node is p or q -> return current node
# - Recurse left and right:
#     left = dfs(node.left)
#     right = dfs(node.right)
# - If both left and right are non-null, it means:
#     p found in one side and q found in the other -> current node is LCA
# - Otherwise return whichever side is non-null
# -----------------------------------------------

# Time Complexity:  O(n)  (visit each node at most once)
# Space Complexity: O(h)  (recursion stack; h = height of tree)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    def dfs(node):
        if node is None:
            return None

        # If we hit either p or q, return it upward
        if node == p or node == q:
            return node

        left = dfs(node.left)
        right = dfs(node.right)

        # If p is in one subtree and q is in the other, this node is LCA
        if left is not None and right is not None:
            return node

        # Otherwise, return the node found in left OR right (or None)
        return left if left is not None else right

    return dfs(root)


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left
q = root.left.right.right

ans = lowestCommonAncestor(root, p, q)
print(ans.val)
