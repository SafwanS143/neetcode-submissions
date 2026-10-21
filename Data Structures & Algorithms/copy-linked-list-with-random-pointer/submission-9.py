"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None

        def isAlrMade(node, nodeList):
            if node and node in nodeList:
                return nodeList[node]

            elif node is None:
                return None
            
            created[node] = Node(node.val)
            return created[node]
        
        created = {head: Node(head.val)}
        curr = head
        newHead = created[curr]
        print(curr.val)

        while curr:
            
            created[curr].next = isAlrMade(curr.next, created)
            created[curr].random = isAlrMade(curr.random, created)

            curr = curr.next

        return newHead