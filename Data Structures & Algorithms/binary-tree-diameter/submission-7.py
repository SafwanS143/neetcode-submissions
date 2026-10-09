# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal maxDiameter

            if node is None:
                return 0

            heightLeft = dfs(node.left)
            heightRight = dfs(node.right)

            maxDiameter = max(maxDiameter, heightLeft + heightRight)

            return max(heightLeft, heightRight) + 1

        dfs(root)
        return maxDiameter

            