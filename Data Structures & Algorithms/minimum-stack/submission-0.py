class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
