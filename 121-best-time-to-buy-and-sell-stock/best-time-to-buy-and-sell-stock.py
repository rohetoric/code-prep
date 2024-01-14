class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0

        for p in prices:
            if p < buy_price:
                buy_price = p
            elif max_profit < p - buy_price:
                max_profit = p - buy_price
    
        return max_profit



        