# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfsValid(node: Optional[TreeNode], min: int, max: int) -> bool:
            isLeftValid = dfsValid(node.left, min, node.val) if node.left else True
            isRightValid = dfsValid(node.right, node.val, max) if node.right else True

            return node.val > min and node.val < max and isRightValid and isLeftValid

        return dfsValid(root, -1000000000, 1000000000)