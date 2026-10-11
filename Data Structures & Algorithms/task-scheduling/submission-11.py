from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(heap)
        timer = 0
        cooldown = deque()

        while heap or cooldown:
            timer += 1
            
            if heap:
                cnt = heapq.heappop(heap)
                if cnt + 1 < 0:
                    cooldown.append([cnt + 1, timer + n])

            if cooldown and cooldown[0][1] == timer:
                heapq.heappush(heap, cooldown.popleft()[0])

        return timer