class Solution:
    def solveNQueens(self, n: int):
        res = []
        cols = set()
        d1 = set()
        d2 = set()
        board = [["."] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or r - c in d1 or r + c in d2:
                    continue
                cols.add(c)
                d1.add(r - c)
                d2.add(r + c)
                board[r][c] = "Q"
                backtrack(r + 1)
                board[r][c] = "."
                cols.remove(c)
                d1.remove(r - c)
                d2.remove(r + c)
        backtrack(0)
        return res
