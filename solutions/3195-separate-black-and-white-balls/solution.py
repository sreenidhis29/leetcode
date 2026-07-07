class Solution:
    def minimumSteps(self, s: str) -> int:
        slow = 0
        swaps = 0

        for fast in range(len(s)):
            if s[fast] == '0':
                swaps += fast - slow
                slow += 1

        return swaps
