class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        hmap = {i: set() for i in range(numCourses)}
        
        for crs, prereq in prerequisites:
            hmap[crs].add(prereq)

        res = [False] * len(queries)
        def dfs(crs, prereq, visited):
            if crs in visited: return False
            visited.add(crs)
            if prereq in hmap[crs]: return True
            for prq in hmap[crs]:
                if dfs(prq, prereq, visited): return True

        i = 0
        for crs, prereq in queries:
            if dfs(crs, prereq, set()): res[i] = True
            i += 1
        return res