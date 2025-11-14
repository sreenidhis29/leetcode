class Solution:
    def findSubsequences(self, nums):
        res = []
        path = []
        n = len(nums)
        def dfs(start):
            if len(path) >= 2:
                res.append(path[:])
            used = set()
            for i in range(start, n):
                if (path and nums[i] < path[-1]) or nums[i] in used:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res

