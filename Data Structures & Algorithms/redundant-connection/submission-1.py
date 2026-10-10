class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parents = [n for n in range(len(edges) + 1)]
        print(parents)

        def find(x):
            og = x
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(a, b):
            parA, parB = find(a), find(b)

            if parA == parB:
                return False
            
            if parA > parB:
                parA, parB = parB, parA

            parents[parB] = parA
            return True

        for first, second in edges:
            if (first, second) == (1, 3):
                print(parents[3], parents[1])
            if union(first, second) == False:
                return [first, second]