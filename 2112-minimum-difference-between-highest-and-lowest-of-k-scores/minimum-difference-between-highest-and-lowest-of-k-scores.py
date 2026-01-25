class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, k - 1
        nums.sort()
        min_diff = float("inf")
        print(nums)
        while r < len(nums):
            min_diff = min(min_diff, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return min_diff
                