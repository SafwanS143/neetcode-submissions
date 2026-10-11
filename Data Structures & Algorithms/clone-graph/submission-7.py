"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clone = {}
        clone[1] = Node(1, [])

        q = deque([node])

        while q:
            curr = q.popleft()
            for nxt in curr.neighbors:
                if nxt.val not in clone:
                    q.append(nxt)
                    clone[nxt.val] = Node(nxt.val, [])
                clone[curr.val].neighbors.append(clone[nxt.val])

        return clone[1]