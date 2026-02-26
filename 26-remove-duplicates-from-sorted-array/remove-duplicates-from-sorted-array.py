class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1, ptr2 = 0, 1
        for i in range(len(nums)):
            if ptr2 >= len(nums): break
            if nums[ptr1] != nums[ptr2]:
                ptr1 += 1
                ptr2 += 1
            else: del nums[ptr2]
        return len(nums)