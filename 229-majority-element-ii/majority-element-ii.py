class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map = {}
        target = math.floor(len(nums)/3)
        res = []
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 0
            map[nums[i]] = map[nums[i]] + 1
        for num in map:
            if map[num] > target:
                res.append(num)
                if len(res) == 2: break
        return res

