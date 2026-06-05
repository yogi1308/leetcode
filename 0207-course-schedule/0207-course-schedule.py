class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = {}
        dfsDone = set()
        def dfs(prereqs, visited):
            for course in prereqs:
                if course in visited:
                    return False
                elif course in dfsDone: continue
                else: 
                    visited.add(course)
                    found = False
                    if course in hmap:
                        if not dfs(hmap[course], visited): return False
                    dfsDone.add(course)
                    visited.remove(course)
            return True

        for course, prereq in prerequisites:
            hmap.setdefault(course, []).append(prereq)

        for prereq in hmap:
            if prereq not in dfsDone:
                if not dfs(hmap[prereq], {prereq}): return False

        return True