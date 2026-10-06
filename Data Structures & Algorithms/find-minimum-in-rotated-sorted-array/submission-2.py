class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (right + left) // 2

            if nums[mid] <= nums[-1]:
                right = mid
            
            else:
                left = mid + 1
        
        return nums[left]