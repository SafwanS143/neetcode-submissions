from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numberCounts = Counter(nums)
        
        freq = [[] for i in range(len(nums) + 1)]

        for num in numberCounts:
            freq[numberCounts[num]].append(num)
        
        out = []

        for i in range(len(nums), 0, -1):
            if len(freq[i]) > 0:
                for num in freq[i]:
                    out.append(num)
                    if len(out) == k:
                        return out


        return out
