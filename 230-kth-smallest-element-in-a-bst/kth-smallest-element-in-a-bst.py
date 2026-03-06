# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        def preorder(root):
            if not root: return
            vals.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        vals.sort()
        print(vals)
        return vals[k-1]
