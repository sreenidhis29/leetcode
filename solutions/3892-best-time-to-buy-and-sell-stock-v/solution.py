class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        INF = 10**30
        dp0 = [0] * (k + 1)
        dpL = [-INF] * (k + 1)
        dpS = [-INF] * (k + 1)
        for price in prices:
            for t in range(k, -1, -1):
                dp0[t] = max(
                    dp0[t],
                    dpL[t] + price,
                    dpS[t] - price
                )
                if t > 0:
                    dpL[t] = max(dpL[t], dp0[t - 1] - price)
                    dpS[t] = max(dpS[t], dp0[t - 1] + price)
        return max(dp0)
