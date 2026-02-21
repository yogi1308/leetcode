class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 0
            map[nums[i]] = map[nums[i]] + 1
        for num in map:
            if map[num] > math.floor(len(nums)/3):
                res.append(num)
        return res

