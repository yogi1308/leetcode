class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = float('inf')
        hold = False
        for i in range(len(prices)):
            if i != len(prices) - 1:
                if prices[i] < prices[i + 1] and not hold:
                    bought = prices[i]
                    hold = True
                    print("bought: ", bought)
                elif bought < prices[i] and prices[i] > prices[i + 1]:
                    profit += prices[i] - bought
                    bought = float('inf')
                    hold = False
                    print("sold: ", prices[i] - bought, i, prices[i])
            else: 
                if prices[i] > bought:
                    profit += prices[i] - bought
        return profit

