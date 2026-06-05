class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = {}
        dfsDone = set()
        found = False
        def dfs(prereqs, visited):
            nonlocal found
            if found: return False
            for course in prereqs:
                if course in visited:
                    found = True
                elif course in dfsDone: continue
                else: 
                    visited.add(course)
                    if course in hmap: dfs(hmap[course], visited)
                    dfsDone.add(course)
                    visited.remove(course)
            return True

        for course, prereq in prerequisites:
            if course not in hmap:
                hmap[course] = []
            hmap[course].append(prereq)

        for prereq in hmap:
            if prereq not in dfsDone:
                dfs(hmap[prereq], {prereq})
                if found: return False

        return False if found else True