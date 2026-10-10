from collections import deque

class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(board), len(board[0])

        def bfs(i: int, j: int):
            q = deque([[i, j]])
            region = {(i, j)}

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    validRow = 0 <= nr < rows
                    validCol = 0 <= nc < cols

                    if validRow and validCol and board[nr][nc] == "O" and (nr, nc) not in region and (nr, nc):
                        q.append([nr, nc])
                        region.add((nr, nc))

            for r, c in region:
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    return region

            for r, c in region:
                board[r][c] = "X"
            return None


        notSurrounded = set()

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if board[i][j] == "O" and (i, j) not in notSurrounded:
                    safeRegion = bfs(i, j)
                    if safeRegion:
                        notSurrounded.add(region for region in safeRegion)
