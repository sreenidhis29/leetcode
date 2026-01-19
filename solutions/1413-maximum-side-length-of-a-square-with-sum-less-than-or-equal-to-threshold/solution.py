class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + mat[i][j]

        def square_sum(x, y, k):
            return ps[x + k][y + k] - ps[x][y + k] - ps[x + k][y] + ps[x][y]

        lo, hi, ans = 0, min(m, n), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            found = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if square_sum(i, j, mid) <= threshold:
                        found = True
                        break
                if found:
                    break
            if found:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
