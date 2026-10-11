class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(start, path):
            if sum(path) == target:
                return output.append(path[:])

            if sum(path) > target:
                return None

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path)
                path.pop()

            
        backtrack(0, [])
        return output