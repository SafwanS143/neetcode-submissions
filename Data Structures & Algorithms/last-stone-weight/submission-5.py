import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest, secondLargest = - heapq.heappop(stones), - heapq.heappop(stones)

            if largest > secondLargest:
                heapq.heappush(stones, -(largest - secondLargest))

        return -heapq.heappop(stones) if len(stones) == 1 else 0