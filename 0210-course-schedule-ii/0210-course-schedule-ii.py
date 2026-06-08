class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDeg = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        res = []
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDeg[course] += 1
        
        q = deque()
        for course in range(numCourses): 
            if inDeg[course] == 0: q.append(course)

        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in graph[node]:
                inDeg[neighbor] -= 1
                if inDeg[neighbor] == 0:
                    q.append(neighbor)
        
        return res if len(res) == numCourses else []