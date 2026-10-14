from collections import defaultdict, deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = defaultdict(list)

        for source, target, time in times:
            neighbors[source].append((time, target))

        seen = set()
        heap = [(0, k)]

        while heap:
            travelTime, node = heapq.heappop(heap)
            if node in seen: continue
            seen.add(node)
            if len(seen) == n: return travelTime
            
            for nxt in neighbors[node]:
                if nxt[1] in seen: continue
                heapq.heappush(heap, (nxt[0] + travelTime, nxt[1]))
        
        return -1