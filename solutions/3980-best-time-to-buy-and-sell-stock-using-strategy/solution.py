class Solution:
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        base = sum(strategy[i] * prices[i] for i in range(n))
        best = base
        half = k // 2
        delta = [0] * (n + 1)
        for i in range(n):
            delta[i] = strategy[i] * prices[i]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + delta[i]
        sell_prefix = [0] * (n + 1)
        for i in range(n):
            sell_prefix[i + 1] = sell_prefix[i] + prices[i]
        for l in range(0, n - k + 1):
            mid = l + half
            r = l + k
            removed = prefix[r] - prefix[l]
            added = (sell_prefix[r] - sell_prefix[mid])
            best = max(best, base - removed + added)
        return best
