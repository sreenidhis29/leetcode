class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_l = list(s)
        n = len(s_l)

        for i in range (0, n, 2 * k):
            l = i
            r = min(i + k - 1, n - 1)

            while l < r:
                s_l[l], s_l[r] = s_l[r], s_l[l]
                l += 1
                r -= 1

        return "".join(s_l)
        
