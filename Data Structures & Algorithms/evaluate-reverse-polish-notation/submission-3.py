import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+" : operator.add, 
            "-" : operator.sub, 
            "*" : operator.mul, 
            "/" : operator.truediv}

        stack = []

        for char in tokens:
            if char in ops:
                temp = ops[char](int(stack[-2]), int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(temp)
            else:
                stack.append(char)

        return int(stack[0])