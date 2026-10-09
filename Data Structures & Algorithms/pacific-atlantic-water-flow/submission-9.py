from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(heights), len(heights[0])

        def bfs(coords):
            q = deque(coords)
            cells = set(coords)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    validRow = 0 <= nr < len(heights)
                    validCol = 0 <= nc < len(heights[0])

                    if validRow and validCol and heights[nr][nc] >= heights[r][c] and (nr, nc) not in cells:
                        cells.add((nr, nc))
                        q.append((nr, nc))

            return cells

        pacificUp = [(0, i) for i in range(cols)] + [(i, 0) for i in range(rows)]
        atlanticUp = [(i, cols - 1) for i in range(rows)] + [(rows - 1, i) for i in range(cols)]

        return [list(coords) for coords in bfs(pacificUp) & bfs(atlanticUp)]