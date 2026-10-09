"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return

        seen = {}

        stack = [node]
        seen[1] = Node(1, [])
        while stack:
            curr = stack.pop()
            for neighbor in curr.neighbors:
                if neighbor.val not in seen:
                    stack.append(neighbor)
                    seen[neighbor.val] = Node(neighbor.val, [])
                seen[curr.val].neighbors.append(seen[neighbor.val])

        return seen[1]

