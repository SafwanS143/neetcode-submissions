from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        
        inDegrees = [0] * numCourses
        for course, preReq in prerequisites:
            inDegrees[course] += 1
            graph[preReq].append(course)

        q = deque(i for i in range(numCourses) if inDegrees[i] == 0)
        coursesDone = 0

        while q:
            curr = q.popleft()
            coursesDone += 1

            for next in graph[curr]:
                inDegrees[next] -= 1

                if inDegrees[next] == 0:
                    q.append(next)

        
        return coursesDone == numCourses