class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)

            if profit <= 0:
                l = r
            r +=1
        
        return maxP


