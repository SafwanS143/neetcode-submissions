from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(heap)

        cooldown = deque(list())
        time = 0

        while heap or cooldown:

            if heap:
                timesRemaining = -heapq.heappop(heap)
                if timesRemaining - 1 > 0: cooldown.append([timesRemaining - 1, time + n])

            if cooldown:
                if cooldown[0][1] == time:
                    heapq.heappush(heap, -cooldown[0][0])
                    cooldown.popleft()


            time += 1
        
        return time