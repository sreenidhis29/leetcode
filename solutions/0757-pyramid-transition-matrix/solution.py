class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict
        rules = defaultdict(set)
        for a, b, c in allowed:
            rules[a + b].add(c)
        memo = {}

        def dfs(row: str) -> bool:
            if row in memo:
                return memo[row]
            if len(row) == 1:
                return True
            def backtrack(i, path):
                if i == len(row) - 1:
                    return dfs(path)

                pair = row[i:i+2]
                if pair not in rules:
                    return False
                for ch in rules[pair]:
                    if backtrack(i + 1, path + ch):
                        return True
                return False
            memo[row] = backtrack(0, "")
            return memo[row]

        return dfs(bottom)
