class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, subset):
            if sum(subset) >= target:
                if sum(subset) == target:
                    res.append(subset.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                dfs(i + 1, subset)
                subset.pop()
        dfs(0, [])
        return res