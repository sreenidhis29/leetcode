class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        ans = 0
        cur = 0
        for c in s:
            if c == '1':
                cur += 1
            else:
                if cur:
                    ans = (ans + cur * (cur + 1) // 2) % mod
                    cur = 0
        if cur:
            ans = (ans + cur * (cur + 1) // 2) % mod
        return ans
