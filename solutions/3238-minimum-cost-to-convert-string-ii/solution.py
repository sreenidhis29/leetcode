class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:
        INF = 10**18
        n = len(source)

        # Collect all strings
        all_strings = set(original) | set(changed)
        idx = {s: i for i, s in enumerate(all_strings)}
        m = len(all_strings)

        # Floyd–Warshall over string graph
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)

        for k in range(m):
            for i in range(m):
                if dist[i][k] == INF:
                    continue
                for j in range(m):
                    if dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Group originals by length
        by_len = {}
        for o in original:
            by_len.setdefault(len(o), set()).add(o)

        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue

            # No-op if characters already match
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            # Try only relevant substring lengths
            for L, group in by_len.items():
                if i + L > n:
                    continue
                s_sub = source[i:i + L]
                if s_sub not in group:
                    continue
                t_sub = target[i:i + L]
                if t_sub not in idx:
                    continue

                d = dist[idx[s_sub]][idx[t_sub]]
                if d < INF:
                    dp[i + L] = min(dp[i + L], dp[i] + d)

        return dp[n] if dp[n] < INF else -1
