class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        idx = -1
        base_idx = 0
        while not found and nums:
            mid = round(len(nums) / 2)
            if nums[mid] == target:
                idx = base_idx + mid
                found = True
            elif nums[mid] < target:
                nums = nums[mid + 1:]
                base_idx += mid + 1
            else:
                nums = nums[:mid]
                base_idx += 0
        return idx

