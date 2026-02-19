class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        if len(nums) == 1: return nums
        mid = len(nums) // 2
        arr1 = self.sortArray(nums[:mid])
        arr2 = self.sortArray(nums[mid:])
        return self.merge(arr1, arr2)

    def merge(self, arr1, arr2):
        res = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(arr1) and ptr2 < len(arr2):
            if arr1[ptr1] < arr2[ptr2]: 
                res.append(arr1[ptr1])
                ptr1 += 1
            else:
                res.append(arr2[ptr2])
                ptr2 += 1
        if ptr1 < len(arr1):
            res.extend(arr1[ptr1:])
        if ptr2 < len(arr2):
            res.extend(arr2[ptr2:])
        return res