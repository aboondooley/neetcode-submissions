class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        days = len(prices)
        if days < 2: return max_price
        l, r = 0, 1
        while r < days:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > max_price:
                    max_price = profit
            else:
                l = r
            r+=1
        return max_price

