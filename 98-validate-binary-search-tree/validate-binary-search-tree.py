# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        boolean, past = self.traversal(root, None)
        return boolean

    def traversal(self, node, past):
        if not node:
            return True, past

        boolean, past = self.traversal(node.left, past)
        if past is not None:
            if past>=node.val:
                return False, past
        if boolean:
            past = node.val
            return self.traversal(node.right, past)
        return False, past