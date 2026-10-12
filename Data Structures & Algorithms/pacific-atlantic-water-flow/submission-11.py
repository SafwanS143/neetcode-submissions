from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
       
        def populateUpstream(upstream):
            upstream = set(upstream)
            q = deque(upstream)

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    validRow = 0 <= nr < rows
                    validCol = 0 <= nc < cols

                    if validRow and validCol and heights[nr][nc] >= heights[r][c] and (nr, nc) not in upstream:
                        q.append((nr, nc))
                        upstream.add((nr, nc))

            return upstream

        pacific = [(0,i) for i in range(cols)] + [(i,0) for i in range(1, rows)]
        atlantic = [(rows - 1,i) for i in range(cols)] + [(i, cols - 1) for i in range(0, rows - 1)]

        return [[x, y] for x, y in populateUpstream(pacific) & populateUpstream(atlantic)]