class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                price = prices[j] - prices[i]
                if price > max:
                    max = price

        return max

                



        