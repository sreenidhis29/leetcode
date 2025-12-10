class NumMatrix:

    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.pref = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += matrix[i][j]
                self.pref[i+1][j+1] = self.pref[i][j+1] + row_sum

    def sumRegion(self, row1, col1, row2, col2):
        p = self.pref
        return p[row2+1][col2+1] - p[row1][col2+1] - p[row2+1][col1] + p[row1][col1]
