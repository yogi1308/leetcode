class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, k
        nums.sort()
        min_diff = float("inf")
        while r < len(nums)  + 1:
            arr = nums[l : r]
            min_diff = min(min_diff, max(arr) - min(arr))
            l, r = l + 1, r + 1
        return min_diff
                