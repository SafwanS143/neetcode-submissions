class Node:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, self.head, None)
        self.head.next = self.tail
        self.cap = capacity

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]

    def addNode(self, node):
        self.tail.prev.next = node
        self.cache[node.key] = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value = self.cache[key].value

        self.removeNode(self.cache[key])
        self.addNode(Node(key, value, None, None))

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        
        self.addNode(Node(key, value, None, None))

        if self.cap < len(self.cache):
            self.removeNode(self.head.next)