class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        subsetTotal = sum(nums) // k
        subset = [0] * k
        if subsetTotal != total / k:
            return False
        nums.sort(reverse=True)
        def backtrack(i):
            if i == len(nums):
                return True
            
            seen = set()
            for j in range(k):
                if subset[j] not in seen and subset[j] + nums[i] <= subsetTotal:
                    seen.add(subset[j])
                    subset[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    subset[j] -= nums[i]
            return False
        return backtrack(0)