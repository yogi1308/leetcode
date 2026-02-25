# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder: return

        root = preorder[0]
        index = inorder.index(root)

        inorder_left = inorder[0:index]
        inorder_right = inorder[index+1:]
        preorder_left = preorder[1:index+1]
        preorder_right = preorder[index+1:]

        root = TreeNode(root)
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root