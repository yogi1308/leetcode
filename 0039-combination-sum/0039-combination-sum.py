class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, subset):
            if sum(subset) >= target:
                if sum(subset) == target:
                    res.append(subset.copy())
                return
            for num in range(len(nums[idx:])):
                subset.append(nums[idx + num])
                dfs(idx + num, subset)
                subset.pop()
        dfs(0, [])
        return res