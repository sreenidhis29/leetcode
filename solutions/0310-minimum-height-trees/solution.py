class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        from collections import defaultdict, deque

        graph = defaultdict(set)
        degree = [0] * n

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque(i for i in range(n) if degree[i] == 1)

        remaining = n
        while remaining > 2:
            size = len(leaves)
            remaining -= size
            for _ in range(size):
                leaf = leaves.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)

        return list(leaves)
