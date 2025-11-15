class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[-1][j - 1] + res[-1][j]
            res.append(row)
        return res

