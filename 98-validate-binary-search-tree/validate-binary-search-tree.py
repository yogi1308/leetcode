# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def getMin(root, val):
            if not root: return True
            if root.val <= val: return False
            return getMin(root.left, val) and getMin(root.right, val)
        
        def getMax(root, val):
            if not root: return True
            if root.val >= val: return False
            return getMax(root.left, val) and getMax(root.right, val)

        def checkEveryNode(root):
            if not root: return True
            if not getMin(root.right, root.val) or not getMax(root.left, root.val): return False
            return checkEveryNode(root.left) and checkEveryNode(root.right)
        
        return checkEveryNode(root)


        