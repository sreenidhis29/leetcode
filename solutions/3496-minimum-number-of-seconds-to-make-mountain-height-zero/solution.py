class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        lo, hi = 1, 10**16

        while lo < hi:
            mid = (lo + hi) >> 1
            tot = 0
            for t in workerTimes:
                tot += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)
                if tot >= mountainHeight: break
            if tot >= mountainHeight:
                hi = mid
            else:
                lo = mid + 1

        return lo
