class Solution:
    def grayCode(self, n: int):
        res = [0]
        for i in range(n):
            x = 1 << i
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] | x)
        return res
