class Solution:
    def minDeletionSize(self, strs):
        rows = len(strs)
        cols = len(strs[0])
        ans = 0
        for c in range(cols):
            for r in range(1, rows):
                if strs[r][c] < strs[r - 1][c]:
                    ans += 1
                    break
        return ans
