# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(nodes):
            if not nodes or nodes == [None]: return
            n = []
            vals = []
            for node in nodes:
                if node:
                    vals.append(node.val)
                    if node.left: n.append(node.left)
                    if node.right: n.append(node.right)
            res.append(vals)
            bfs(n)
        
        bfs([root])
        return res