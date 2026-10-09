from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDegrees = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegrees[course] += 1

        q = deque(i for i in range(numCourses) if inDegrees[i] == 0)
        order = []

        while q:
            curr = q.popleft()
            order.append(curr)

            for nxt in graph[curr]:
                inDegrees[nxt] -= 1
                if inDegrees[nxt] == 0:
                    q.append(nxt)

        return order if len(order) == numCourses else []