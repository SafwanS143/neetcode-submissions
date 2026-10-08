class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int):
            stack = [(r, c)]
            grid[r][c] = 0
            currArea = 1

            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    validRow = 0 <= nr < len(grid)
                    validCol = 0 <= nc < len(grid[0])
                    if validRow and validCol and grid[nr][nc] == 1:
                        stack.append((nr, nc))
                        grid[nr][nc] = 0
                        currArea += 1

            return currArea


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea