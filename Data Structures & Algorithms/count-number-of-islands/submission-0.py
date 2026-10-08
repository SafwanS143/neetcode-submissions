class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def dfs(row: int, col: int):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    dfs(nr, nc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)


        return islands