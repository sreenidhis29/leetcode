class Solution:
    def maxSubarraySum(self, nums, k: int) -> int:
        n = len(nums)
        pref = 0
        INF = 10**30
        min_pref = [INF] * k
        min_pref[0] = 0
        ans = -INF
        for j, v in enumerate(nums, 1):
            pref += v
            r = j % k
            if min_pref[r] != INF:
                ans = max(ans, pref - min_pref[r])
            if pref < min_pref[r]:
                min_pref[r] = pref
        return ans
