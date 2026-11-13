from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        visited = set()
        stack = [(0, -1)]

        while stack:
            curr, currParent = stack.pop()
            if curr in visited: return False
            visited.add(curr)

            for neighbour in graph[curr]:
               if neighbour != currParent: stack.append((neighbour, curr))

        return len(visited) == n