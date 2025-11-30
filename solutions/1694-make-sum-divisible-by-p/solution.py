class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums) % p
        if total == 0:
            return 0
        n = len(nums)
        best = n
        pref = 0
        last = {0: -1}
        for i, v in enumerate(nums):
            pref = (pref + v) % p
            need = (pref - total) % p
            if need in last:
                best = min(best, i - last[need])
            last[pref] = i
        return best if best < n else -1
