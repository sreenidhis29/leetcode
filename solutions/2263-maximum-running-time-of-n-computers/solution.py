from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries) // n
        while left < right:
            mid = (left + right + 1) // 2
            total = 0
            need = n * mid
            for b in batteries:
                if b >= mid:
                    total += mid
                else:
                    total += b
                if total >= need:
                    break
            if total >= need:
                left = mid
            else:
                right = mid - 1
        return left
