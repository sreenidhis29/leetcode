class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one way to make sum 0

        # Try all numbers from 1 up to the largest i such that i^x <= n
        i = 1
        while i**x <= n:
            power = i**x
            for j in range(n, power - 1, -1):
                dp[j] = (dp[j] + dp[j - power]) % MOD
            i += 1

        return dp[n]

