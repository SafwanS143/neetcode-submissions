from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        totalMins = 0
        ripeFruit = 0
        ripeFruitSeen = 0
        rottenFruit = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(rotten: List[tuple()]) -> int:
            nonlocal ripeFruitSeen
            q = deque(rotten)
            currMins = 0

            while q:
                for _ in range(len(q)): 
                    curr = q.popleft()
                    r, c = curr[0], curr[1]

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        validHor = 0 <= nc < len(grid[0])
                        validVert = 0 <= nr < len(grid)

                        if validHor and validVert and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            ripeFruitSeen += 1
                            q.append((nr, nc))
                
                if q: currMins += 1

            return currMins

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ripeFruit += 1

                elif grid[i][j] == 2:
                    rottenFruit.append((i, j))

        totalMins = bfs(rottenFruit)

        if ripeFruitSeen != ripeFruit:
            return -1

        return totalMins

