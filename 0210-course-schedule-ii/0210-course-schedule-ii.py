class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDeg = {}
        graph = {}
        q = deque()
        res = []
        for course in range(numCourses):
            inDeg[course] = 0
            graph[course] = []
            q.append(course)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
            inDeg[prereq] = inDeg[prereq] + 1
            if prereq in q: q.remove(prereq)
        
        while q:
            course = q.popleft()
            res.append(course)
            for prereq in graph[course]:
                inDeg[prereq] = inDeg[prereq] - 1
                if inDeg[prereq] == 0: q.append(prereq)
        
        res.reverse()
        return res if len(res) == numCourses else []