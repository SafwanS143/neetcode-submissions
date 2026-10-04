class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left != right:
            maxArea = max(maxArea, min(heights[left], heights[right]) * (right - left))
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea