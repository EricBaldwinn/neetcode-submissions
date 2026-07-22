class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        low = 0

        for sell in range(len(prices)):
            if prices[sell] < prices[low] and sell > 0:
                low = sell
            difference = prices[sell] - prices[low]
            profit = max(profit, difference)
        
        return profit
        