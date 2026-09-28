class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = dict(zip(position, speed))

        stack = []
        for p in sorted(cars, reverse = True):
            time = (target - p) / cars[p]
            stack.append([p, time])
            if len(stack) >= 2 and stack[-1][1] <= stack[-2][1]:
                stack.pop()
        
        return len(stack)