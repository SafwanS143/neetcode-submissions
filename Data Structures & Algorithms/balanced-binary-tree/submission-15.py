# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfsHeightBalance(node):
            if node is None:
                return [True, 0]
            
            leftBal, leftHeight = dfsHeightBalance(node.left)
            rightBal, rightHeight = dfsHeightBalance(node.right)

            return [leftBal and rightBal and abs(leftHeight - rightHeight) < 2, max(leftHeight, rightHeight) + 1]

        return dfsHeightBalance(root)[0]