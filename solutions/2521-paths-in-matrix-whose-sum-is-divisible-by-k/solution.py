from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp_prev = [[0] * k for _ in range(n)]
        for i in range(m):
            dp_curr = [[0] * k for _ in range(n)]
            for j in range(n):
                v = grid[i][j] % k
                if i == 0 and j == 0:
                    dp_curr[0][v] = 1
                else:
                    if i > 0:
                        for r in range(k):
                            cnt = dp_prev[j][r]
                            if cnt:
                                dp_curr[j][(r + v) % k] = (dp_curr[j][(r + v) % k] + cnt) % mod
                    if j > 0:
                        for r in range(k):
                            cnt = dp_curr[j - 1][r]
                            if cnt:
                                dp_curr[j][(r + v) % k] = (dp_curr[j][(r + v) % k] + cnt) % mod
            dp_prev = dp_curr
        return dp_prev[n - 1][0]
