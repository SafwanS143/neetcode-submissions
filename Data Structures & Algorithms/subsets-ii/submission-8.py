class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)

        def backtrack(start, path):
            if start == len(nums):
                results.append(path[:])
                return None

            
            path.append(nums[start])
            backtrack(start + 1, path)
            path.pop()

            while start + 1 < len(nums) and nums[start + 1] == nums[start]:
                start += 1
            backtrack(start + 1, path)

        backtrack(0, [])
        return results