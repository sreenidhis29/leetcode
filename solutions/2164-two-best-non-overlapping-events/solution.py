from typing import List
from collections import deque
from operator import itemgetter

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=itemgetter(0))
        end_sorted = deque(sorted(events, key=itemgetter(1)))
        ans = 0
        end_max = 0
        for start, end, value in events:
            while end_sorted and end_sorted[0][1] < start:
                _, _, v = end_sorted.popleft()
                end_max = max(end_max, v)
            ans = max(ans, value + end_max)
        return ans
