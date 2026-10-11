class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)

        def backtrack(start, path):
            if start == len(nums):
                if path not in results:
                    results.append(path[:])
                return None

            
            path.append(nums[start])
            backtrack(start + 1, path)
            path.pop()


            backtrack(start + 1, path)

        backtrack(0, [])
        return results