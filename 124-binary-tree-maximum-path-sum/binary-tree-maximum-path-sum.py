# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = root.val

        def maxSubtree(root):
            if not root: return float('-inf')

            l = maxSubtree(root.left)
            r = maxSubtree(root.right)

            val = max(
                root.val,
                r + root.val,
                l + root.val
                )

            nonlocal maxPath
            maxPath = max(
                maxPath, val,
                l + r + root.val,
                l, r
                )

            return val
        
        maxSubtree(root)
        return maxPath

