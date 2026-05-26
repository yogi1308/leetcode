class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        table = {i: set() for i in range(1, n + 1)}
        for i in trust: 
            table[i[0]].add(i[1])
        candidate = -1
        for i in table:
            if table[i] == set(): 
                candidate = i
                break
        for i in table:
            if i == candidate: continue
            if candidate not in table[i]:
                return -1
        return candidate