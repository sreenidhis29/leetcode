class Solution:
    def permute(self, nums):
        res = []
        used = [False] * len(nums)
        path = []
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack()
                    path.pop()
                    used[i] = False
        backtrack()
        return res
