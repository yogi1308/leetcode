class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        heapq.heapify(nums)
        largest = nums[0]
        for i in range(k):
            largest = heapq.heappop(nums)
        return largest * -1