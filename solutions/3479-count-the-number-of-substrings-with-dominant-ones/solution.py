class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [i for i, c in enumerate(s) if c == '0']
        ans = 0
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1
        import math
        limit = int(math.isqrt(n)) + 2
        m = len(zeros)

        def pairs_lt(A, B, t):
            if t <= 0:
                return 0
            max_sum = (A - 1) + (B - 1)
            if t >= max_sum + 1:
                return A * B
            if A > B:
                A, B = B, A
            up = t - 1
            res = 0
            r1 = min(up, A - 1)
            if r1 >= 0:
                res += (r1 + 1) * (r1 + 2) // 2
            if B - 1 >= A and up >= A:
                low2 = A
                high2 = min(up, B - 1)
                if high2 >= low2:
                    res += (high2 - low2 + 1) * A
            if up >= B:
                low3 = B
                high3 = min(up, A + B - 2)
                if high3 >= low3:
                    cnt = high3 - low3 + 1
                    res += cnt * (A + B - 1) - (low3 + high3) * cnt // 2
            return res

        for z in range(1, min(limit, m) + 1):
            for k in range(m - z + 1):
                p = zeros[k]
                q = zeros[k + z - 1]
                prev = -1 if k == 0 else zeros[k - 1]
                nxt = n if k + z - 1 == m - 1 else zeros[k + z]
                base_len = q - p + 1
                max_extra_l = p - (prev + 1)
                max_extra_r = (nxt - 1) - q
                A = max_extra_l + 1
                B = max_extra_r + 1
                need = z * z - base_len + z
                if need <= 0:
                    ans += A * B
                    continue
                max_sum = max_extra_l + max_extra_r
                if need > max_sum:
                    continue
                total = A * B
                ans += total - pairs_lt(A, B, need)
        return ans

