class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26
        for i, c in enumerate(s):
            idx = ord(c) - 97
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
        ans = 0
        for c in range(26):
            if first[c] != -1 and last[c] > first[c]:
                seen = set()
                for i in range(first[c] + 1, last[c]):
                    seen.add(s[i])
                ans += len(seen)
        return ans
