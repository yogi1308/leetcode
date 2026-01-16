class Solution:
    def search(self, nums: List[int], target: int) -> int:
        base_idx = 0
        while nums:
            mid = round(len(nums) / 2)
            if nums[mid] == target:
                return base_idx + mid
            elif nums[mid] < target:
                nums = nums[mid + 1:]
                base_idx += mid + 1
            else:
                nums = nums[:mid]
                base_idx += 0
        return -1