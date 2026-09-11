class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices);
        min_price = prices[0];
        max_profit = 0;
        for i in range(n):
            new_profit = prices[i] - min_price;
            if new_profit > max_profit:
                max_profit = new_profit;
            if min_price > prices[i]:
                min_price = prices[i];
        return max_profit;
            
        