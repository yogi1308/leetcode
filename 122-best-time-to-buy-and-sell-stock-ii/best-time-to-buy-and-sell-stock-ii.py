class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = 0
        hold = False
        for i in range(len(prices)):
            if i != len(prices) - 1:
                if prices[i] < prices[i + 1] and not hold:
                    bought = prices[i]
                    hold = True
                elif bought < prices[i] and prices[i] > prices[i + 1] and hold:
                    profit += prices[i] - bought
                    hold = False
            else: 
                if prices[i] > bought and hold:
                    profit += prices[i] - bought
        return profit

