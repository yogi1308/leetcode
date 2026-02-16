# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        arr = []
        def preorder(root):
            if not root: return
            if root.left and root.right: 
                temp = root.left
                root.left = root.right
                root.right = temp
            elif root.left and not root.right:
                root.right = root.left
                root.left = None
            elif not root.left and root.right:
                root.left = root.right
                root.right = None
            preorder(root.left)
            preorder(root.right)
        preorder(root)

        return root
        # if not arr: return
        # new_root = TreeNode(arr.pop(0))
        # for val in arr:
        #     new

