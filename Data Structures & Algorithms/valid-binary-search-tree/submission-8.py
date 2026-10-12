# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, min, max):
            if node is None:
                return True

            rightValid = validate(node.left, min, node.val)
            leftValid = validate(node.right, node.val, max)

            return rightValid and leftValid and min < node.val < max


        return validate(root, -1000000000, 1000000000)