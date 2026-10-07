# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0 

        def treeHeight(node: Optional[TreeNode]) -> int:
            nonlocal maxDiameter
            height = 0
            
            if node is None:
                return 0

            rightSum = treeHeight(node.right)
            leftSum = treeHeight(node.left)

            maxDiameter = max(maxDiameter, rightSum + leftSum)

            return 1 + max(rightSum, leftSum)

        treeHeight(root)

        return maxDiameter

        