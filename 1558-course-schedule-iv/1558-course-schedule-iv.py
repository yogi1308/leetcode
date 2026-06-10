class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        hmap = {i: set() for i in range(numCourses)}
        
        for crs, prereq in prerequisites:
            hmap[crs].add(prereq)

        prereqMap = {}
        def dfs(crs):
            if crs in prereqMap: return prereqMap[crs]
            prereqMap[crs] = set()
            for prq in hmap[crs]:
                prereqMap[crs].add(prq)
                prereqMap[crs] |= dfs(prq)
            return prereqMap[crs]

        for crs, prereq in queries:
            dfs(crs)

        return [prereq in prereqMap[crs] for crs, prereq in queries]