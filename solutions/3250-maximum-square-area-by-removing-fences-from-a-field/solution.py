from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])

        heights = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                heights.add(h[j] - h[i])

        widths = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                widths.add(v[j] - v[i])

        possible = heights & widths
        if not possible:
            return -1

        side = max(possible)
        return (side * side) % MOD
