class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = 0
        hold = False
        for i in range(len(prices) - 1):
            if not hold and prices[i] < prices[i + 1]:
                bought = prices[i]
                hold = True
            elif hold and bought < prices[i] and prices[i] > prices[i + 1]:
                profit += prices[i] - bought
                hold = False

        if prices[len(prices) - 1] > bought and hold:
            profit += prices[len(prices) - 1] - bought
        return profit

