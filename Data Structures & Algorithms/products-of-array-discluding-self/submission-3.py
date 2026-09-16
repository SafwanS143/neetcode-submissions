class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            out[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(len(nums))):
            out[i] *= suffix
            suffix *= nums[i]

        return out