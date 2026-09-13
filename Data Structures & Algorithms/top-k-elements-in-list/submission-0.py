from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numberCounts = Counter(nums)
        
        return [pair[0] for pair in numberCounts.most_common(k)]
