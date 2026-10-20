# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodesCounter = 0

        def dfs(node, maxAbove):
            nonlocal goodNodesCounter
            if node.val >= maxAbove:
                goodNodesCounter += 1
            
            if node.left: dfs(node.left, max(maxAbove, node.val))
            if node.right: dfs(node.right, max(maxAbove, node.val))

        dfs(root, float('-inf'))

        return goodNodesCounter