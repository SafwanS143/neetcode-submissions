# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfsHeight(root: Optional[TreeNode]) -> int:
            if root is None:
                return [True, 0]

            heightLeft = dfsHeight(root.left)
            heightRight = dfsHeight(root.right)

            balanced = (heightLeft[0] and heightRight[0] and abs(heightLeft[1] - heightRight[1]) < 2)

            return [balanced, 1 + max(heightLeft[1], heightRight[1])]

        
        return dfsHeight(root)[0]