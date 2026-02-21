class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map = {}
        res = []
        target = math.floor(len(nums)/3)
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 0
            map[nums[i]] = map[nums[i]] + 1
            if len(map) > 2:
                copyMap = map.copy()
                for num in copyMap:
                    map[num] = map[num] - 1
                    if map[num] == 0:
                        map.pop(num)


        for num in map:
            if nums.count(num) > target:
                res.append(num)
        return res
