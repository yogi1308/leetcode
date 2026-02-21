# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def height(root):
            if not root: return 0
            l = height(root.left)
            r = height(root.right)

            self.maxDiameter = max(self.maxDiameter, l + r)

            
            return max(l, r) + 1
        
        height(root)
        return self.maxDiameter