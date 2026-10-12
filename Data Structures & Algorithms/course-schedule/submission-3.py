from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        inDegrees = [0] * numCourses

        for a, b in prerequisites:
            courseMap[b].append(a)
            inDegrees[a] += 1

        q = deque([])
        for i, val in enumerate(inDegrees):
            if val == 0:
                q.append(i)

        courseCounter = 0
        while q:
            curr = q.popleft()

            for course in courseMap[curr]:
                inDegrees[course] -= 1
                if inDegrees[course] == 0:
                    q.append(course)
                    
            courseCounter += 1

        return True if courseCounter == numCourses else False