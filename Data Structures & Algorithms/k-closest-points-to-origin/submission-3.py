from collections import defaultdict
import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointDistances = defaultdict(list)
        heap = []
        output = []

        for x, y in points:
            dist = sqrt(x**2 + y**2)
            pointDistances[dist].append([x, y])

            heapq.heappush(heap, -dist)
            if len(heap) > k:
                heapq.heappop(heap)

        for dist in heap:
            output.append(pointDistances[-dist].pop())

        return output