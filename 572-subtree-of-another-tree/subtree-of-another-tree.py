# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        return self.treesEqual(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def treesEqual(self, root, subRoot):
        if not root and not subRoot: return True
        if not root and subRoot: return False
        if root and not subRoot: return False
        return root.val == subRoot.val and self.treesEqual(root.left, subRoot.left) and self.treesEqual(root.right, subRoot.right)