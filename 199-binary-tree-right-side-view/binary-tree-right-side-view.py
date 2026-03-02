# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root: res.append(root.val)

        def bfs(nodes):
            if not nodes or nodes == [None]: 
                return
            vals = []
            for node in nodes:
                if node.left: vals.append(node.left)
                if node.right: vals.append(node.right)
            print(res)
            if vals: res.append(vals[-1].val)
            return bfs(vals)

        bfs([root])
        return res