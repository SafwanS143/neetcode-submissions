from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        output = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(coords: set(List[int])) -> List[List[int]]:
            q = deque(coords)
            cells = []

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    validRow = 0 <= nr < len(heights)
                    validCol = 0 <= nc < len(heights[0])

                    if validRow and validCol and heights[nr][nc] >= heights[r][c] and [nr, nc] not in cells:
                        cells.append([nr, nc])
                        q.append([nr, nc])

            return cells


        pacificUp = set()
        atlanticUp = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):

                if i == 0 or j == 0:
                    pacificUp.add((i, j))

                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    atlanticUp.add((i, j))
        
        for coords in bfs(pacificUp):
            pacificUp.add((coords[0], coords[1]))
        for coords in bfs(atlanticUp):
            atlanticUp.add((coords[0], coords[1]))

        for coords in pacificUp:
            if coords in atlanticUp:
                output.append(coords)

        return output