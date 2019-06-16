# Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit, profit = 0, 0 
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
                continue
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit