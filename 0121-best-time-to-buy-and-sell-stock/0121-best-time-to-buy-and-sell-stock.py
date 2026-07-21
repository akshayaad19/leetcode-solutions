class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0 
        minprice = prices[0]
        for i in range(0, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            profit = prices[i]- minprice
            if profit > maxprofit:
                maxprofit = profit
        return maxprofit