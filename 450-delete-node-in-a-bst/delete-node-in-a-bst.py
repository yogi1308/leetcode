# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        nodesToAdd = []
        def preorder(root):
            if not root: return
            nodesToAdd.append(root.val)
            preorder(root.left)
            preorder(root.right)
            return
        
        def searchNode(root, val, parent):
            if not root: return None, parent
            if val == root.val: return (root, parent)
            elif val < root.val: return searchNode(root.left, val, root)
            else: return searchNode(root.right, val, root)
        
        def addToBST(root, val):
            if not root: return
            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                else: addToBST(root.right, val)
            else: 
                if not root.left: 
                    root.left = TreeNode(val)
                    return
                else: addToBST(root.left, val)
            return

        nodeToDelte, parent = searchNode(root, key, None)
        nodeReplacedBy = None
        if not nodeToDelte: return root
        if root == nodeToDelte:
            if root.left: preorder(root.left)
            if root.right: preorder(root.right)
            if not nodesToAdd: return
            newRoot = TreeNode(nodesToAdd.pop())
            for node in nodesToAdd:
                addToBST(newRoot, node)
            return newRoot

        if parent.left == nodeToDelte:
            if nodeToDelte.left:
                parent.left = nodeToDelte.left
                nodeReplacedBy = nodeToDelte.left
                preorder(nodeToDelte.right)
            else:
                parent.left = nodeToDelte.right
                nodeReplacedBy = nodeToDelte.right
                preorder(nodeToDelte.left)
        else:
            if nodeToDelte.left:
                parent.right = nodeToDelte.left
                nodeReplacedBy = nodeToDelte.left
                preorder(nodeToDelte.right)
            else: 
                parent.right = nodeToDelte.right
                nodeReplacedBy = nodeToDelte.right
                preorder(nodeToDelte.left)

        print(nodesToAdd)
        for node in nodesToAdd:
            addToBST(nodeReplacedBy, node)

        return root

            