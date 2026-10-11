from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q = deque([[]])
        
        for num in nums:
            for _ in range(len(q)):
                curr = q.popleft()
        
                q.append(curr + [num])
                q.append(curr)

        return list(q)