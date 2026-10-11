from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []

        q = deque([[]])
        
        for i, num in enumerate(nums):
            for _ in range(len(q)):
                curr = q.popleft()
        
                q.append(curr + [num])
                q.append(curr)
        
        for comb in q:
            combinations.append(comb)

        return combinations