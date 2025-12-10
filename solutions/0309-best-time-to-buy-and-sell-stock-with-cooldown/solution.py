class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        hold = -prices[0]
        sold = float('-inf')
        rest = 0
        for i in range(1, n):
            price = prices[i]
            new_hold = max(hold, rest - price)
            new_sold = hold + price
            new_rest = max(rest, sold)
            hold, sold, rest = new_hold, new_sold, new_rest
        return max(rest, sold)
