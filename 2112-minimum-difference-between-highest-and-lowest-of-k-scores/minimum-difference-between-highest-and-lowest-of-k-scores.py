class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, k
        nums = sorted(nums)
        min_diff = max(nums)
        while r < len(nums)  + 1:
            min_diff = min(min_diff, max(nums[l : r]) - min(nums[l : r]))
            l, r = l + 1, r + 1
        return min_diff
                