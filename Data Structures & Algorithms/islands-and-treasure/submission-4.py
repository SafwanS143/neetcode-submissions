from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        chests = deque([])
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    chests.append((row, col))
                    visited.add((row, col))
        
        dist = 1

        while chests:
            for _ in range(len(chests)):
                r, c = chests.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    validRow = 0 <= nr < len(grid)
                    validCol = 0 <= nc < len(grid[0])

                    if validRow and validCol and (nr, nc) not in visited and grid[nr][nc] not in [-1, 0]:
                        grid[nr][nc] = min(grid[nr][nc], dist)
                        visited.add((nr, nc))
                        chests.append((nr, nc))
            dist += 1

        

                