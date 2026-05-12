class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(subset, idx):
            res.append(subset.copy())
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: continue
                subset.append(nums[i])
                dfs(subset, i + 1)
                subset.pop()
        dfs([], 0)
        return res