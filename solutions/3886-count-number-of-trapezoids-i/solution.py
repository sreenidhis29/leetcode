from collections import Counter

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ys = Counter()
        for x, y in points:
            ys[y] += 1
        seg_counts = []
        for cnt in ys.values():
            if cnt >= 2:
                seg_counts.append(cnt * (cnt - 1) // 2)
        if not seg_counts:
            return 0
        total = sum(seg_counts) % MOD
        total_sq = sum((c % MOD) * (c % MOD) % MOD for c in seg_counts) % MOD
        inv2 = (MOD + 1) // 2
        ans = ( (total * total - total_sq) % MOD ) * inv2 % MOD
        return ans
