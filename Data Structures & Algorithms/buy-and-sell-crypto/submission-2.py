class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        max_sell = [0] * n

        for i in range(n-2, -1, -1):
            max_sell[i] = max(max_sell[i+1], prices[i+1])

        for i in range(n):
            max_profit = max(max_profit, max_sell[i] - prices[i])
        return max_profit

