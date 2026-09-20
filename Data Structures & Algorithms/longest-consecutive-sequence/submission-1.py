class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest = 0
        
        for i in range(len(nums)):
            if nums[i] - 1 not in seen:
                currentSeq = 1
                while nums[i] + currentSeq in seen:
                    currentSeq += 1
                    
                longest = max(currentSeq, longest)
        
        return longest
