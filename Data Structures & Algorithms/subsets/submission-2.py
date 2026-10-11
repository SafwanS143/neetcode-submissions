class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []

        def backtrack(start, path):
            if start == len(nums):
                return combinations.append(path[:])

            path.append(nums[start])
            backtrack(start + 1, path)
            path.pop()

            backtrack(start + 1, path)

        backtrack(0, [])
        return combinations