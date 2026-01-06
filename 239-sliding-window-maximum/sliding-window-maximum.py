class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        if k == 1:
            return nums
        dp = collections.deque()
        result = []
        for i in range(len(nums)):
            while dp and dp[0] < i-k+1:
                dp.popleft()
            while dp and nums[dp[-1]] < nums[i]:
                dp.pop()
            dp.append(i)
            if i >= k-1:
                result.append(nums[dp[0]])
        return result
