# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkRoot(lnode, rnode):
            if not lnode and not rnode: return True
            if not lnode and rnode: return False
            if lnode and not rnode: return False

            leftSymmetric = checkRoot(lnode.left, rnode.right)
            rightSymmetric = checkRoot(lnode.right, rnode.left)

            return leftSymmetric and rightSymmetric and lnode.val == rnode.val

        if not root: return True
        return checkRoot(root.left, root.right)
