class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(', ']' : '[', '}' : '{'}

        stack = []
        for char in s:

            if char in brackets:
                if not stack or brackets[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            
            else:
                stack.append(char)
        
        return len(stack) == 0