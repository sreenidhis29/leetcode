class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[0] = 1
        pref[0] = 1

        maxdq = deque()
        mindq = deque()
        l = 0

        for r in range(n):
            while maxdq and nums[maxdq[-1]] <= nums[r]:
                maxdq.pop()
            maxdq.append(r)
            while mindq and nums[mindq[-1]] >= nums[r]:
                mindq.pop()
            mindq.append(r)
            while maxdq and mindq and nums[maxdq[0]] - nums[mindq[0]] > k:
                if maxdq and maxdq[0] == l:
                    maxdq.popleft()
                if mindq and mindq[0] == l:
                    mindq.popleft()
                l += 1

            left_pref = pref[l - 1] if l > 0 else 0
            dp[r + 1] = (pref[r] - left_pref) % MOD
            pref[r + 1] = (pref[r] + dp[r + 1]) % MOD

        return dp[n] % MOD
