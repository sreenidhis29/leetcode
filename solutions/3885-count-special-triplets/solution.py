from collections import Counter
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAXV = 200000       
        right = [0] * (MAXV + 1)
        left = [0] * (MAXV + 1)

        for x in nums:
            right[x] += 1
        ans = 0
        for x in nums:
            right[x] -= 1
            doubled = x * 2
            if doubled <= MAXV:
                ans += left[doubled] * right[doubled]
                ans %= MOD
            left[x] += 1
        return ans
