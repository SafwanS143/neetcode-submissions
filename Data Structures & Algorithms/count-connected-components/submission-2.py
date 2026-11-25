class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        rank = [0] * n

        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        
        count = n

        for a, b in edges:
            ra, rb = find(a), find(b)

            if ra != rb:
                if ra > rb:
                    ra, rb = rb, ra
                parents[rb] = ra

                count -= 1
        return count