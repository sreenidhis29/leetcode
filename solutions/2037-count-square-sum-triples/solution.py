import math
class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a * a + b * b
                c = int(math.isqrt(c2))
                if c * c == c2 and 1 <= c <= n:
                    cnt += 1
        return cnt
