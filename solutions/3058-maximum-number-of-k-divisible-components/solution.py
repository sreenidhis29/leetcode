from typing import List
import sys
sys.setrecursionlimit(1_000_000)

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        cuts = 0
        def dfs(u: int, p: int) -> int:
            nonlocal cuts
            s = values[u] % k
            for v in g[u]:
                if v == p:
                    continue
                sc = dfs(v, u)
                if sc % k == 0:
                    cuts += 1
                else:
                    s = (s + sc) % k
            return s
        dfs(0, -1)
        return cuts + 1
