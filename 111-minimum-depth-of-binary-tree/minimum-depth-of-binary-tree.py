# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def minD(root):
            if not root: return float('inf')
            if not root.left and not root.right: return 1
            return 1 + min(minD(root.left), minD(root.right))
        
        return minD(root)