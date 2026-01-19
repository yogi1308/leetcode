class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        min_val = high
        while low <= high:
            test = math.floor((high + low) / 2)
            sum_val = 0
            for bananas in piles:
                if bananas <= test: sum_val += 1
                else: sum_val += math.ceil(bananas/test)
            if sum_val <= h:
                if test < min_val: min_val = test
                high = test - 1
                print(low, test, high)
            else:
                low = test + 1
                print(low, test, high)
        return min_val



