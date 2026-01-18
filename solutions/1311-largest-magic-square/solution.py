class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_ps = [[0] * (n + 1) for _ in range(m)]
        col_ps = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_ps[i][j + 1] = row_ps[i][j] + grid[i][j]
                col_ps[i + 1][j] = col_ps[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        def check(r, c, k):
            target = row_ps[r][c + k] - row_ps[r][c]
            if diag1[r + k][c + k] - diag1[r][c] != target:
                return False
            if diag2[r + k][c] - diag2[r][c + k] != target:
                return False
            for i in range(k):
                if row_ps[r + i][c + k] - row_ps[r + i][c] != target:
                    return False
                if col_ps[r + k][c + i] - col_ps[r][c + i] != target:
                    return False
            return True

        for size in range(min(m, n), 1, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if check(i, j, size):
                        return size
        return 1
