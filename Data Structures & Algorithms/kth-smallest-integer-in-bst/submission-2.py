# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        
        def dfsInOrder(node: Optional[TreeNode]):
            nonlocal vals

            if len(vals) == k:
                return vals[-1]

            if node.left: dfsInOrder(node.left)
            vals.append(node.val)
            if node.right: dfsInOrder(node.right)

            return

        dfsInOrder(root)
        return vals[k - 1]