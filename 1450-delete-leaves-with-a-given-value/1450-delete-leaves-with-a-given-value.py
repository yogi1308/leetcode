# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        firstTime = 1
        removed = False
        mamaRoot = root
        def dfs(root, parent, dir):
            if not root: return
            if root and not root.left and not root.right and root.val == target: 
                nonlocal removed, mamaRoot
                if dir == "left": parent.left = None
                elif dir == "right": parent.right = None
                else: mamaRoot = None
                removed = True
                print(removed)
            if root: dfs(root.left, root, "left")
            if root: dfs(root.right, root, "right")
        while (removed and root) or (firstTime == 1):
            firstTime += 1
            removed = False
            dfs(mamaRoot, None, None)
            print(removed, root.val)
        print(firstTime)
        return mamaRoot
