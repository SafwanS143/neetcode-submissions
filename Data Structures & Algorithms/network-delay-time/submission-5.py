from collections import defaultdict, deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(list)

        for start, stop, time in times:
            nodes[start].append((time, stop))
        
        heap = []
        heapq.heappush(heap, (0, k))
        seen = set()

        while heap:
            time, currNode = heapq.heappop(heap)
            if currNode in seen: continue
            seen.add(currNode)

            if len(seen) == n: return time

            for nxtTime, nxt in nodes[currNode]:
                if nxt in seen: continue
                heapq.heappush(heap, (nxtTime + time, nxt))

        return -1
