# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque([root])
        depth = 0

        while q:
            level = []
            for _ in range(len(q)):
                curNode = q.popleft()

                if curNode.left is not None: q.append(curNode.left)
                if curNode.right is not None: q.append(curNode.right)

            depth += 1

        return depth