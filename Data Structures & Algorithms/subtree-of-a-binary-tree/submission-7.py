# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None: return False
        if root.val == subRoot.val:
            found = self.isSameTree(root, subRoot)
            if found: return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, a, b):
        if a is None and b is None: return True

        if a is None or b is None: return False
        
        return (a.val == b.val and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right))