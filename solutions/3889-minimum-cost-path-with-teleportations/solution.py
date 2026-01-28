class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        import heapq

        m, n = len(grid), len(grid[0])
        INF = 10**18

        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()

        idx_map = {(i, j): idx for idx, (_, i, j) in enumerate(cells)}

        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        pq = [(0, 0, 0, 0)]
        expanded = [0] * (k + 1)

        while pq:
            cost, i, j, used = heapq.heappop(pq)
            if cost > dist[i][j][used]:
                continue
            if i == m - 1 and j == n - 1:
                return cost

            if i + 1 < m:
                nc = cost + grid[i + 1][j]
                if nc < dist[i + 1][j][used]:
                    dist[i + 1][j][used] = nc
                    heapq.heappush(pq, (nc, i + 1, j, used))

            if j + 1 < n:
                nc = cost + grid[i][j + 1]
                if nc < dist[i][j + 1][used]:
                    dist[i][j + 1][used] = nc
                    heapq.heappush(pq, (nc, i, j + 1, used))

            if used < k:
                curVal = grid[i][j]
                ptr = expanded[used]
                while ptr < len(cells) and cells[ptr][0] <= curVal:
                    _, x, y = cells[ptr]
                    if cost < dist[x][y][used + 1]:
                        dist[x][y][used + 1] = cost
                        heapq.heappush(pq, (cost, x, y, used + 1))
                    ptr += 1
                expanded[used] = ptr

        return -1
