class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []

        def backtrack(start, path):
            if start == len(nums):
                return combinations.append(path[:])

            for i in range(start, len(nums)):

                path.append(nums[i])
                if path in combinations:
                    path.pop()
                    continue
                    
                backtrack(i + 1, path)
                path.pop()

                backtrack(i + 1, path)

        backtrack(0, [])
        return combinations