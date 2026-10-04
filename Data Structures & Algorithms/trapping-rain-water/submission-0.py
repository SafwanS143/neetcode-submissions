class Solution:
    def trap(self, height: List[int]) -> int:
        maxSeen = 0
        maxLeft = []
        maxRight = [0] * len(height)
        totalWater = 0

        for i, length in enumerate(height):
            maxLeft.append(maxSeen)
            maxSeen = max(maxSeen, length)

        maxSeen = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = maxSeen
            maxSeen = max(maxSeen, height[i])

        for i in range(len(height)):
            waterCap = min(maxLeft[i], maxRight[i]) - height[i]
            if waterCap > 0:
                totalWater += waterCap

        return totalWater