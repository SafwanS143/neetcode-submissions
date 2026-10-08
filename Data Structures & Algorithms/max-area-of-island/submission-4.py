from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r: int, c: int):
            stack = [(r, c)]
            grid[r][c] = 0
            currArea = 1

            while stack:
                curr = stack.pop()
                r, c = curr[0], curr[1]
                for dr, dc in directions:
                    validRow = 0 <= r + dr < len(grid)
                    validCol = 0 <= c + dc < len(grid[0])
                    if validRow and validCol and grid[r + dr][c + dc] == 1:
                        stack.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = 0
                        currArea += 1

            return currArea


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = maxArea = max(maxArea, bfs(i, j))

        return maxArea