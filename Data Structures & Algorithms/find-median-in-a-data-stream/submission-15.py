import heapq

class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        self.n = 0
        

    def addNum(self, num: int) -> None:
        self.n += 1

        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (-self.low[0] + self.high[0]) / 2

        return -self.low[0]