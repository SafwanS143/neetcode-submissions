# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        valsSeen = 0
        kthVal = -1
        
        def dfsInOrder(node: Optional[TreeNode]):
            nonlocal valsSeen, kthVal 

            if node is None or valsSeen == k:
                return

            dfsInOrder(node.left)

            valsSeen += 1
            if valsSeen == k: 
                kthVal = node.val
                return

            dfsInOrder(node.right)

            return

        dfsInOrder(root)
        return kthVal