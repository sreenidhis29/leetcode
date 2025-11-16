class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 1, x // 2
        while l <= r:
            m = (l + r) // 2
            sq = m * m
            if sq == x:
                return m
            if sq < x:
                l = m + 1
            else:
                r = m - 1
        return r
