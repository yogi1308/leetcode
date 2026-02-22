# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        
        def hasPOrQ(root, p, q):
            if not root: return False
            left = hasPOrQ(root.left, p, q)
            right = hasPOrQ(root.right, p, q)
            isRoot = (root == p or root == q)
            if left and right or (isRoot and (left or right)):
                nonlocal lca
                lca = root
            return left or right or isRoot

        hasPOrQ(root, p, q)
        return lca

# Works but is inefficient O(n^2)