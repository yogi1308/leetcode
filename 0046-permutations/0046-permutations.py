class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                print("ran")
                return
            for i in range(len(nums)):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    dfs(subset)
                    subset.pop()
        dfs([])
        return res