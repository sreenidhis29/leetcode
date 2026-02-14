class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_row + 2)
        dp[0] = float(poured)

        for r in range(query_row):
            for c in range(r, -1, -1):
                overflow = max(0.0, dp[c] - 1.0)
                if overflow > 0:
                    share = overflow / 2.0
                    dp[c] = share
                    dp[c + 1] += share
                else:
                    dp[c] = 0.0

        return min(1.0, dp[query_glass])
