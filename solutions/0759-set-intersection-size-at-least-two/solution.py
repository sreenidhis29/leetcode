class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        p1 = p2 = -1
        ans = 0
        for s, e in intervals:
            if s > p1:
                ans += 2
                p2 = e - 1
                p1 = e
            elif s > p2:
                ans += 1
                p2 = p1
                p1 = e
        return ans
