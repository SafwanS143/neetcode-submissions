# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque([root])
        output = []

        while q:
            level = []
            for _ in range(len(q)):
                curNode = q.popleft()

                if curNode.left: q.append(curNode.left)
                if curNode.right: q.append(curNode.right)

                level.append(curNode)

            output.append(level[-1].val)

        return output