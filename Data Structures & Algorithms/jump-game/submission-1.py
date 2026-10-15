class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mostRecentSafe = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= mostRecentSafe:
                mostRecentSafe = i

        return mostRecentSafe == 0

