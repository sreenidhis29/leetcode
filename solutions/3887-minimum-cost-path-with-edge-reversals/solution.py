class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        import heapq
        from collections import defaultdict

        adj = defaultdict(list)
        incoming = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            incoming[v].append((u, w))

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            if u == n - 1:
                return cost

            for v, w in adj[u]:
                nc = cost + w
                if nc < dist[v]:
                    dist[v] = nc
                    heapq.heappush(pq, (nc, v))

            for v, w in incoming[u]:
                nc = cost + 2 * w
                if nc < dist[v]:
                    dist[v] = nc
                    heapq.heappush(pq, (nc, v))

        return -1
