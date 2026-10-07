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

        heightLeft = self.heightTree(root.left)
        heightRight = self.heightTree(root.right)

        print(heightLeft, heightRight, root.val)

        return abs(heightLeft - heightRight) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def heightTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0

        q = deque([root])
        
        depth = 0
        while q:
            for _ in range(len(q)):
                curNode = q.popleft()

                if curNode.left: q.append(curNode.left)
                if curNode.right: q.append(curNode.right)

            depth += 1

        return depth