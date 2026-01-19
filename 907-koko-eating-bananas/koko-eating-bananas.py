class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            test = (high + low) // 2
            sum_val = 0
            for bananas in piles:
                sum_val += math.ceil(bananas/test)
                if sum_val > h: break
            if sum_val <= h:
                high = test - 1
            else:
                low = test + 1
        return low




