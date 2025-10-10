from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        t_map = Counter(t)
        required = len(t_map)
        left = 0
        right = 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None  # length, left, right

        while right < len(s):
            c = s[right]
            window_counts[c] = window_counts.get(c, 0) + 1

            if c in t_map and window_counts[c] == t_map[c]:
                formed += 1

            while left <= right and formed == required:
                c = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                window_counts[c] -= 1
                if c in t_map and window_counts[c] < t_map[c]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
