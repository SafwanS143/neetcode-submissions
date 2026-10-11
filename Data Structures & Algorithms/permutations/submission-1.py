class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(path, used):
            if len(path) == len(nums):
                output.append(path[:])
                return

            for i in range(0, len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                backtrack(path, set(used))
                path.pop()
                used.remove(nums[i])

        
        backtrack([], set())
        return output