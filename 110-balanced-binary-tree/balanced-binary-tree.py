# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
    
        def height(root):
            if not root: return 0
            l = height(root.left) + 1
            r = height(root.right) + 1
            if abs(l-r) > 1:
                nonlocal isBalanced
                isBalanced = False
            return max(l, r)

        height(root)
        return isBalanced
            