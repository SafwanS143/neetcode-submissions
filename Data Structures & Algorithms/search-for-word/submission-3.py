class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def backtrack(row, col, path, index):
            if index == len(word):
                return True

            r, c = row, col
            possiblePaths = []

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in path:
                    continue

                validRow = 0 <= nr < len(board)
                validCol = 0 <= nc < len(board[0])

                if validRow and validCol and board[nr][nc] == word[index]:
                    possiblePaths.append((nr, nc))

            for x, y in possiblePaths:
                path.add((x, y))
                if backtrack(x, y, path, index + 1): return True
                path.remove((x, y))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, {(i, j)}, 1):
                        return True

        return False
