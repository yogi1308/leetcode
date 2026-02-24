# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        depthSet = 1
        
        def hasPOrQ(root, p, q, depth):
            if not root: return False
            nonlocal depthSet
            left = hasPOrQ(root.left, p, q, depth + 1)
            right = hasPOrQ(root.right, p, q, depth + 1)
            isRoot = (root.val == p.val or root.val == q.val)
            if (left and right or (isRoot and (left or right))) and (depth > depthSet):
                nonlocal lca
                lca = root
                depthSet = depth
                print(depthSet)
            return left or right or isRoot

        hasPOrQ(root, p, q, 1)
        return lca

# Works but is inefficient O(n^2)