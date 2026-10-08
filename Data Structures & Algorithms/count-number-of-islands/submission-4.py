class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row: int, col: int):
            for dr, dc in directions:
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
                    return

                grid[row][col] = "0"
                for dr, dc in directions:
                    dfs(row + dr, col + dc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)


        return islands