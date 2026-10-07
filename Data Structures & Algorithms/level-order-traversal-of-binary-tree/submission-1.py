# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        output = []

        if root is None:
            return []

        while q:
            level = []
            
            for _ in range(len(q)):
                curNode = q.popleft()

                if curNode.left: q.append(curNode.left)
                if curNode.right: q.append(curNode.right)

                level.append(curNode.val)
            
            output.append(level)
        
        return output