from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(board), len(board[0])

        def bfs(i: int, j: int, safeSet):
            q = deque([(i, j)])
            safeSet.add((i, j))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    validRow = 0 <= nr < rows
                    validCol = 0 <= nc < cols

                    if validRow and validCol and board[nr][nc] == "O" and (nr, nc) not in safeSet:
                        q.append((nr, nc))
                        safeSet.add((nr, nc))

        notSurrounded = set()

        borders = [(0, j) for j in range(cols)] + [(rows - 1, j) for j in range(cols)] + [(i, 0) for i in range(rows)] + [(i, cols - 1) for i in range(rows)]

        for i, j in borders:
            if board[i][j] == "O" and (i, j) not in notSurrounded:
                bfs(i, j, notSurrounded)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in notSurrounded:
                    board[i][j] = "X"
