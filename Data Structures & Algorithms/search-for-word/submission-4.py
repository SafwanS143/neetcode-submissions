class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, path, index):
            if index == len(word):
                return True

            if not (0 <= r < rows) or not (0 <= c < cols) or board[r][c] != word[index] or (r, c) in path:
                return False

            path.add((r, c))
            found = any(backtrack(r + dr, c + dc, path, index + 1) for dr, dc in directions)
            path.remove((r, c))

            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, set(), 0): return True

        return False
