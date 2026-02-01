class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary  = {}
        mark = len(nums) / 2
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
            if dictionary[num] > mark: return num